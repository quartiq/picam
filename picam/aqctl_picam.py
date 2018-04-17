#!/usr/bin/env python3

import argparse
import sys
import time

from . import pi

from artiq.protocols.pc_rpc import simple_server_loop
from artiq.tools import (verbosity_args, simple_network_args, init_logger,
    bind_address_from_args)


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
        lib
        cam = pi.Camera()
        if args.simulation:
            cam.open(cam.connect_demo(
                pi.PicamModel_ProEMHS512BExcelon, "12345678"))
        else:
            cam.open_first()
        with cam:
            simple_server_loop({"cam": cam}, bind_address_from_args(args),
                               args.port, description="")


if __name__ == "__main__":
    main()
