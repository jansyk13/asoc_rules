#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import ConfigParser
import argparse

def generate_updates (combs)

def generate_combinations(config):
    combinations=[]
    for each_section in config.sections():
        for (each_key, each_val) in config.items(each_section):
            if not each_key is 'meta':
               print ("%s %s" % (each_section, each_val)) 
               combinations.append("%s %s" % (each_section, each_val))
    return combinations


def generate_table(config, type, combs):
    sql=list()
    sql.append("CREATE TABLE asoc_rules_%s ( rules VARCHAR(255), " % type)
    i=1
    for dim in combs: 
        sql.append("%s LONG" % dim)
        if i != len(combs):
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

    combs = generate_combinations(config)

    print generate_table(config=config, type='a', combs=combs)


def main():
    try:
        main_wrapper()
    except Exception:
        print "Asoc_rules tool run ended with"
        raise


if __name__ == "__main__":
    main()

