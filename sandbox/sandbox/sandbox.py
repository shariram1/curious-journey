#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 12:33:53 2018

@author: shariram
"""

import errno
import configparser
import logging
import os

from logging.config import fileConfig


def initConfig(configFileName):
    config = configparser.ConfigParser()
    config.read(configFileName)
    return config


def initLog(configFileName):
    fileConfig(configFileName)
    logger = logging.getLogger()
    return logger


def main():

    programName = os.path.splitext(os.path.basename(__file__))[0]
    homedirectory = os.path.join(os.getenv("HOME", "./"))
    configFileName = os.path.join(homedirectory, programName + ".ini")

    # Initial Validation
    if not os.path.isfile(configFileName):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), configFileName)

    # Initialize Logger
    log = initLog(configFileName)
    log.info("---------------")
    log.info("SANDBOX Utility")
    log.info("---------------")

    # Read Config
    config = initConfig(configFileName)
    log.info("Reading config file: {}".format(configFileName))


if __name__ == "__main__":
    main()
