import sys;
import re;
import set_assoc_cache as Cache;

argc = len(sys.argv);

if argc < 2:
	print("ERROR: incorrect number of arguments.");
	print("usage: cachesim [input_file]");
	exit();
	
file = open(sys.argv[1]);

cache = Cache.Cache();

for line in file :
	match = re.match('0x([^:]*): W 0x(.*)', line);
	if match :
		print(match.groups());
	#if len(matches) == 2 :
	#	print(str(cache[int(matches[1], 16)]));
	
print("");

if cache.accesses != 0 :
	print("miss rate: " + str(cache.misses/cache.accesses));