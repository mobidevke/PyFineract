#!/usr/bin/env bash

docker exec CONTAINER_ID /usr/bin/mysqldump -u root --password=mysql mifostenant-default  > fineract-instance/mysql/02-load_sample_data.sql