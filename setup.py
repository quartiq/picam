#!/usr/bin/env python3

import sys
from setuptools import setup
from setuptools import find_packages


setup(
    name="picam",
    version="0.1",
    description="PICam Python wrappers for Princeton Instruments PICam library",
    long_description=open("README.rst").read(),
    author="QUARTIQ GmbH",
    author_email="rj@quartiq.de",
    url="https://github.com/quartiq/picam",
    download_url="https://github.com/quartiq/picam",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "aqctl_picam = picam.aqctl_picam:main",
        ],
    },
    # test_suite="picam.test",
    license="LGPLv3+",
)
