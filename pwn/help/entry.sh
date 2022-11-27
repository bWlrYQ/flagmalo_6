#!/bin/bash

while :
do
	socat TCP-LISTEN:11337,reuseaddr,fork EXEC:'/ctf/chall';
done

