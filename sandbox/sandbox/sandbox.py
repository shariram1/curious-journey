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


def initLog(configFileName, logFileName):
    fileConfig(configFileName)
    logger = logging.getLogger()
    return logger

def main():
    
    programName     = os.path.splitext(os.path.basename(__file__))[0]
    homedirectory   = os.path.join(os.getenv('HOME', './'))
    configFileName  = os.path.join(homedirectory, programName + ".ini")
    logFileName     = os.path.join(os.getenv('LOG_DIR', os.path.join(homedirectory,  'log')), programName + ".log")
    
    # Initial Validation
    if not os.path.isfile(configFileName):
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), configFileName)
    
    # Read Config
    config = initConfig(configFileName)
    
    print ("programName = {}".format(programName))
    print ("configFileName = {}".format(configFileName))
    print ("logFileName = {}".format(logFileName))

    # Initialize Logger
    log = initLog(configFileName, logFileName)
    log.info("---------------")
    log.info("SANDBOX Utility")
    log.info("---------------")
    

if __name__ == '__main__':
    main()