#!/bin/bash

BACKUP_DIR="/backup/configs"
mkdir -p $BACKUP_DIR

cp /etc/apache2/apache2.conf $BACKUP_DIR/
cp /etc/mysql/mysql.conf.d/mysqld.cnf $BACKUP_DIR/
cp /etc/systemd/system.conf $BACKUP_DIR/

