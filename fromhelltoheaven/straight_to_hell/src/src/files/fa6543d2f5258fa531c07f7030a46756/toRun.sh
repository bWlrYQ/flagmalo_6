#!/bin/bash
for f in ./pay*; do
	node bot.js $f;
done;
rm ./pay*;
