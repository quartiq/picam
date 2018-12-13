#!/usr/bin/env python3

import asyncio
import argparse
import logging

from artiq.protocols.pc_rpc import simple_server_loop
from artiq.tools import (verbosity_args, simple_network_args, init_logger,
                         bind_address_from_args)

from . import pi


logger = logging.getLogger(__name__)


class CameraCtrl(pi.Camera):
    def get(self, key):
        return pi.Camera.get(self, getattr(pi, "PicamParameter_{}".format(key)))

    def set(self, key, value):
        return pi.Camera.set(self, getattr(pi, "PicamParameter_{}".format(key)), value)

    def enum(self, key):
        return getattr(pi, key)

    def acquire(self, readout_count, readout_stride):
        data, errors = pi.Camera.acquire(self, readout_count)
        data = pi.Camera.get_data(data, readout_stride)
        return data, errors.value

    async def ping(self):
        try:
            self.get_id()
        except:
            logger.warning("ping failed", exc_info=True)
            return False
        return True


def get_argparser():
    parser = argparse.ArgumentParser(description="""PICam controller.

    Use this controller for PICam cameras (Princeton Instruments).""")
    simple_network_args(parser, 3258)
    parser.add_argument("--simulation", action="store_true",
                        help="use demo camera")
    verbosity_args(parser)
    return parser


def main():
    args = get_argparser().parse_args()
    init_logger(args)

    with pi.Library() as lib:
        cam = CameraCtrl()
        if args.simulation:
            cam.open(cam.connect_demo(
                pi.PicamModel_ProEMHS512BExcelon, "12345678"))
        else:
            cam.open_first()
        with cam:
            logger.info("Camera open, serving")
            simple_server_loop({"cam": cam}, bind_address_from_args(args),
                               args.port, description="")


if __name__ == "__main__":
    main()
