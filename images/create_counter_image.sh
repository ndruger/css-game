#!/bin/bash

for i in {0..100}; do
	padded=`printf %03d $i`
	convert +append `expr ${i} / 100`.png `expr ${i} / 10`.png `expr ${i} % 10`.png ${padded}.png
	all="${all} ${padded}.png"
done
convert -append ${all} counter_image.png
rm ${all}
