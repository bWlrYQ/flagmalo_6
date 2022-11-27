#!/bin/bash
php /var/www/html/create_db.php
rm create_db.php
apache2 -D FOREGROUND
