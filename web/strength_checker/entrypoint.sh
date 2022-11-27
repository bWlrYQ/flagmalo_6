#!/bin/bash

apache2-foreground & 
python3 /var/www/html/strengthChecker.py --password "$FLAG"
