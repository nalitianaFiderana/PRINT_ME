#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import argparse as arg

__version__ = "1.0.0"

parser = arg.ArgumentParser(prog="ppf", description="A CLI tool that will create and print your Portfolio with the help of commmand line", epilog="You will just need to create a json file in your portfolio or create it here")

parser.add_argument('-v', '--version', action='version', version=f'%(prog)s {__version__}')
args = parser.parse_args()

print(args)