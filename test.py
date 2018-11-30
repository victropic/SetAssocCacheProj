#! /usr/bin/python


import sys
import re
import set_assoc_cache as CacheLib

#if len(sys.argv) != 2:
#    print("ERROR: incorrect number of arguments")
#    print("usage: cachesim [filename]")
#    sys.exit(1)
#file= open(sys.argv[1], "r")
file= open("file.txt")
#**Error check later**

#Initialize variables with the arguments (Later)

#cacheLnSz = sys.argv[4]
#cacheSz = sys.argv[2]
#ways = sys.argv[3]
cache = CacheLib.Cache()


while True:
  inputLine = file.readline()
	#Exit condition on empty line
  if inputLine == "":
      break
	#
  whiteSpaceMatch = re.match(r'^\s*$',inputLine)
  if whiteSpaceMatch != None:
      continue
  inputLine = inputLine.rstrip('\n')
	#Split current line into 3 tokens: PC, R/W, and memory address
  tokenM = inputLine.split()
	#Converting the string into an int, then a hexa. There may be
	#a more graceful method, but this works
  tempAddrInt = int(tokenM[2], 0)
  virtAddr = hex(tempAddrInt)
  RW = tokenM[1]
	#PC isn't important, this is just here for consistency
  PC = tokenM[0]

  cache[tempAddrInt]
	
  if cache.accesses != 0 :
    print("miss rate: " + str( (cache.misses/cache.accesses)*100 )+"%")
		