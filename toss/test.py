import re

pattern = re.compile(r'^[0-9,]+$')
if pattern.match('2---3,,,,24444'):
    print("match")
else:
    print("dfdf")
