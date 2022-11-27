#!/bin/bash
/etc/init.d/ssh start
while :
do
    socat TCP-LISTEN:7000,reuseaddr,fork EXEC:'/challenge/lowlevel';
done