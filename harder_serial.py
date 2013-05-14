#!/usr/bin/env python
# Looks like the serial number verification for space ships is similar to that
# of your robot. Try to find a serial that verifies for this space ship

import sys

  
def check_serial(serial):
#  if (not set(serial).issubset(set(map(str,range(10))))):
#    print ("only numbers allowed")
#    return False
  if len(serial) != 20:
    return False
  if int(serial[15]) + int(serial[4]) != 10:
    return False
  if int(serial[1]) * int(serial[18]) != 2:
    return False
  if int(serial[15]) / int(serial[9]) != 1:
    return False
  if int(serial[17]) - int(serial[0]) != 4:
    return False
  if int(serial[5]) - int(serial[17]) != -1:
    return False
  if int(serial[15]) - int(serial[1]) != 5:
    return False
  if int(serial[1]) * int(serial[10]) != 18:
    return False
  if int(serial[8]) + int(serial[13]) != 14:
    return False
  if int(serial[18]) * int(serial[8]) != 5:
    return False
  if int(serial[4]) * int(serial[11]) != 0:
    return False
  if int(serial[8]) + int(serial[9]) != 12:
    return False
  if int(serial[12]) - int(serial[19]) != 1:
    return False
  if int(serial[9]) % int(serial[17]) != 7:
    return False
  if int(serial[14]) * int(serial[16]) != 40:
    return False
  if int(serial[7]) - int(serial[4]) != 1:
    return False
  if int(serial[6]) + int(serial[0]) != 6:
    return False
  if int(serial[2]) - int(serial[16]) != 0:
    return False
  if int(serial[4]) - int(serial[6]) != 1:
    return False
  if int(serial[0]) % int(serial[5]) != 4:
    return False
  if int(serial[5]) * int(serial[11]) != 0:
    return False
  if int(serial[10]) % int(serial[15]) != 2:
    return False
  if int(serial[11]) / int(serial[3]) != 0:
    return False
  if int(serial[14]) - int(serial[13]) != -4:
    return False
  if int(serial[18]) + int(serial[19]) != 3:
    return False
  return True

from multiprocessing import Pool
from itertools import product,tee
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
k=product(
#0
range(7),
[1,2,3,6,9],
#2
range(10),
range(10),
#4
range(10),
range(9),
#6
range(7),
range(10),
#8
[1,5],
range(10),
#10
[1,2,3,6,9],
range(10),
#12
range(10),
range(10),
#14
range(6),
range(10),
#16
range(10),
range(10),
#18
[1,5],
range(4),
)

#N=6
#p=Pool(N)

#iters = tee(k,N)
#p.map(check_serial,iters)


for e in k:
    if(not check_serial(e)):
        print 'fail:',e
#        k+=1
        continue
    else:
        print 'FOUND ONE!!!!!!',e
        break

