#!/usr/local/bin/python3
import os
import re

with open('long_dna.txt') as fi:
  file = fi.read().upper().rstrip('\n')

sp=list(re.finditer(r'A[AGTC]TAAT',file))
sd=list(re.finditer(r'GC[AG][AT]TG',file))
li=[0]
for i in sp:
  li.append(i.start()+3)
  li.append(i.end()-3)
for l in sd:
  li.append(l.start()+4)
  li.append(l.end()-2)
li.append(len(file))
li.sort()
print(li)
for m in range(0,len(li),2):
  print(file[li[m]:li[m+1]])
  print(len(file[li[m]:li[m+1]]))
  


