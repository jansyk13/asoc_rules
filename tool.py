#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import ConfigParser
import argparse


def generateTable(config, type):
    sql=list()
    sql.append("CREATE TABLE asoc_rules_%s ( rules VARCHAR(255), " % type)
    i=1
    for each_section in config.sections(): 
        sql.append("%s LONG" % each_section)
        if i != len(config.sections()):
            sql.append(", ")
        i = i + 1
    sql.append(" );")
    return "".join(sql)


def read_config(path):
    config_file = os.path.join(path)
    config = ConfigParser.RawConfigParser()
    # disable ConfigParser behavior that lowercases all key names
    config.optionxform = str
    with io.open(config_file) as c:
        config.readfp(c)

    return config


def main_wrapper(argv=None):
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('-c', '--config_file', required=True,
                        help='path to config file')

    args = parser.parse_args()

    config = read_config(args.config_file)
    print generateTable(config=config, type='a')


def main():
    try:
        main_wrapper()
    except Exception:
        print "Asoc_rules tool run ended with"
        raise


if __name__ == "__main__":
    main()

