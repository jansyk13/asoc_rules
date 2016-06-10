#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import ConfigParser
import argparse


def generate_where_expression(statement):
    return ""


def find_in_config(config, statement):
    return ""


def generate_inner_select(config, a, a_bool, b, b_bool):
    return ""


def generate_update(config, a, a_bool, b, b_bool):
    sql=list()
    inner_select=generate_inner_select(config=config, a=a, a_bool=a_bool, b=b, b_bool=b_bool)
    sql.append("UPDATE SET %s=(%s) WHERE rule=%s" % (a, inner_select, b))
    return "".join(sql)


def generate_updates(config, combs, a_bool, b_bool):
    updates=list()
    for i in combs:
        for j in combs: 
            if not i == j:
                updates.append(generate_update(config=config, a=i, a_bool=a_bool, b=j, b_bool=b_bool))
    return updates

        
def generate_inserts(type, combs):
    inserts=list()
    for i in combs:
        inserts.append("INSERT INTO asoc_rules_%s (rule) VALUES (%s)" % (type, i))
    return inserts


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


def generate_combinations(config):
    combinations=[]
    for each_section in config.sections():
        for (each_key, each_val) in config.items(each_section):
            if not each_key == 'meta':
                combinations.append("%s$%s" % (each_section, each_val))
    return combinations


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

    inserts = generate_inserts(type='a', combs=combs)
    for i in inserts:
        print i

    updates = generate_updates(config=config, combs=combs, a_bool=True, b_bool=False)
    for i in updates:
        print i


def main():
    try:
        main_wrapper()
    except Exception:
        print "Asoc_rules tool run ended with"
        raise


if __name__ == "__main__":
    main()

