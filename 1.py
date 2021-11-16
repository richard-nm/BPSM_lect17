#!/usr/local/bin/python3
import re

at=['xkn59438','yhdck2','eihd39d9','chdsye847','hedle3455','xjhd53e','45da','de37dp']
for i in at:
  if len(set(re.findall(r'[0-9]',i))) == 3:
    print(i)
