#!/usr/local/bin/python3
#coding=utf-8
import sys

quality_included=[0,1,4,5,9]
for line in sys.stdin: 
    line = line.strip()
    date = int(line[15:23])
    temperature = int(line[87:92])
    quality = int(line[92:93])
    #sys.stdout.write(str(quality)+'\n')
    #print(line, year, month, day, temperature, quality)
    if temperature != 9999 and quality in quality_included:
        #sys.stdout.write(str(temperature)+'\n')
        print('%s\t%d' % (date, temperature))