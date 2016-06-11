#!/bin/bash
for f in rest.csv
do
    mysql --local-infile -e "load data local infile '$f' into table dj.damejidloRestaurants fields terminated by ',' lines terminated by '\n' ignore 1 lines" -u root -p`cat  mysqlpassword`
    echo $f
done
