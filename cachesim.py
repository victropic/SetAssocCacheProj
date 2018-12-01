import sys;
import re;
import set_assoc_cache as Cache;

argc = len(sys.argv);

if argc < 2:
	print("ERROR: incorrect number of arguments.");
	print("usage: cachesim [input_file]");
	exit();
	
file = open(sys.argv[1]);

if argc == 5 :
	cacheSize = int(sys.argv[2]);
	ways = int(sys.argv[3]);
	cacheLineSize = int(sys.argv[4]);
else :
	cacheSize = 1024;
	ways = 16;
	cacheLineSize = 64;
	
cache = Cache.Cache(cacheSize, ways, cacheLineSize);

for line in file :
	match = re.match('(?:0x)?([A-Za-z0-9]*): (?:W|R) (?:0x)?([A-Za-z0-9]*)', line);
	if match :
		#print(str(cache[int(match[2], 16)]));
		cache[int(match.group(2), 16)];
		#print("");
	
#print("");

if cache.accesses != 0 :
	print("miss rate: " + str((cache.misses/cache.accesses) * 100) + "%");
	print("non compulsary miss rate: " + str((cache.nonCompMisses/cache.accesses) * 100) + "%");