#!/usr/bin/env python

#user_submitted = raw_input("Enter Password: ")i
#
#if len(user_submitted) != 10:
#  print "Wrong"
#  exit()
#
#
k = [193, 35, 9, 33, 1, 9, 3, 33, 9, 225]
#user_arr = []
#for char in user_submitted:
#  # '<<' is left bit shift
#  # '>>' is right bit shift
#  # '|' is bit-wise or
#  # '^' is bit-wise xor
#  # '&' is bit-wise and
#  user_arr.append( (((ord(char) << 5) | (ord(char) >> 3)) ^ 111) & 255 )
#
op = lambda char: (((char << 5) | (char >> 3)) ^ 111) & 255

for j in k:
    for y in  range(1000): 
            if op(y) == j:
                print chr(y)
                break

#if (user_arr == verify_arr):
#  print "Success"
#else:
#  print "Wrong"
