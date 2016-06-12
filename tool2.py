#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os
import ConfigParser
import argparse
import sys
import MySQLdb
import multiprocessing 

db = None

def generate_where_interval_expression(left_side, right_side, boolean, meta):
    sql = list()

    right_side_left = right_side.split('_')[0]
    right_side_right = right_side.split('_')[1]

    if boolean:
        if not right_side_left == 'UNDEF':
            if not right_side_right == 'UNDEF':
                sql.append("(`%s`>%s AND `%s`<=%s)" % (left_side, right_side_left, left_side, right_side_right))
            else:
                sql.append("(`%s`>%s)" % (left_side, right_side_left))
        else:
            if not right_side_right == 'UNDEF':
               sql.append("(`%s`<=%s)" % (left_side, right_side_right))
            else:
               raise Exception
    else:
        if not right_side_left == 'UNDEF':
            if not right_side_right == 'UNDEF':
                sql.append("(`%s`<=%s OR `%s`>%s)" % (left_side, right_side_left, left_side, right_side_right))
            else:
                sql.append("(`%s`<=%s)" % (left_side, right_side_left))
        else:
            if not right_side_right == 'UNDEF':
               sql.append("(`%s`>%s)" % (left_side, right_side_right))
            else:
               raise Exception
    return "".join(sql)


def generate_where_expression(statement, boolean, meta):
    sql = list()
    left_side = statement.split('$')[0]
    right_side = statement.split('$')[1]
    if meta == 'values':
        if boolean:
            sql.append("`%s`='%s' COLLATE utf8_unicode_ci" % (left_side, right_side))
        else:
            sql.append("`%s`!='%s' COLLATE utf8_unicode_ci" % (left_side, right_side))
    elif meta == 'interval':
        sql.append(generate_where_interval_expression(left_side=left_side, right_side=right_side, boolean=boolean, meta=meta))
    else:
        raise Exception('meta=%s' % meta)
    return "".join(sql)


def find_meta_in_config(config, statement):
    section = statement.split('$')[0]
    for k,v in config.items(section):
        if k == 'meta':
            return v
    raise Exception('Not found meta in config  statement=%s' % statement)


def generate_inner_select(config, a, a_bool, b, b_bool):
    sql = list()
    meta_a = find_meta_in_config(config=config, statement=a)
    meta_b = find_meta_in_config(config=config, statement=b)
    exp_a = generate_where_expression(a, a_bool, meta_a)
    exp_b = generate_where_expression(b, b_bool, meta_b)
    sql.append("(SELECT COUNT(*) FROM source_data2 WHERE %s AND %s)" % (exp_a, exp_b))
    return "".join(sql)


def execute_sql(sql):
    print "execute_sql"

    try:
        cursor = db.cursor()
        cursor.execute('SET NAMES utf8;')
        cursor.execute('SET CHARACTER SET utf8;')
        cursor.execute('SET character_set_connection=utf8;')
        cursor.execute(sql)
    except Exception as e:
        print ("sql=%s msg=%s" % (sql, e))


def generate_data(db, config, combs):
    pool = multiprocessing.Pool(10)
    inserts = list()
    for i in combs:
        for j in combs:
            if not i == j:
                sql = list()
                sql.append("INSERT INTO asoc_rules VALUES ('%s', '%s', " % (i, j))
                sql.append(generate_inner_select(config=config, a=i, a_bool=True, b=j, b_bool=True))
                sql.append(", ")
                sql.append(generate_inner_select(config=config, a=i, a_bool=True, b=j, b_bool=False))
                sql.append(", ")
                sql.append(generate_inner_select(config=config, a=i, a_bool=False, b=j, b_bool=True))
                sql.append(", ")
                sql.append(generate_inner_select(config=config, a=i, a_bool=False, b=j, b_bool=False))
                sql.append(");")

                insert = "".join(sql)
                inserts.append(insert)
                print ("%s %s" % (i, j))
    pool.map(execute_sql, inserts)


def generate_table(db):
    cur = db.cursor()
    cur.execute("CREATE TABLE asoc_rules ( ant VARCHAR(255) CHARACTER SET utf8, suk VARCHAR(255) CHARACTER SET utf8, a LONG, b LONG, c LONG, d LONG) CHARACTER SET utf8, COLLATE utf8_general_ci;")


def drop_table(db):
    cur = db.cursor()
    cur.execute("DROP TABLE asoc_rules;")


def connect_to_db():
    db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="password",
                     db="dj")
    db.set_character_set('utf8')
    return db


def generate_combinations(config):
    combinations=[]
    for each_section in config.sections():
        for (each_key, each_val) in config.items(each_section):
            if not each_key == 'meta' and not each_val == 'values' and not each_val  == 'interval':
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
    
    global db

    db = connect_to_db()
    drop_table(db=db)
    generate_table(db=db)
    generate_data(db=db, config=config, combs=combs)


def main():
    reload(sys)
    sys.setdefaultencoding("UTF-8")
    try:
        main_wrapper()
    except Exception:
        print "Asoc_rules tool run ended with"
        raise


if __name__ == "__main__":
    main()
