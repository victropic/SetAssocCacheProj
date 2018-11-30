import math;

import set as Set
### Class that holds all data for a set associative cache
### 	direct mapped cache can be created with sets as number of block and only one way
###		fully associative can be created with one set and ways as the number of blocks 
class Cache :

	### Constructor
	###    size: size of the entire cache (number of sets * ways * cache line size)
	###    ways: number of ways
	###    blockSize: size of a block/cache line in the cache
	def __init__(self, size, ways, blockSize) :
	
		# check that args are all powers of two
		if size <= 0 or not checkPowerOfTwo(sets):
			size = 2048;
	
		if ways <= 0 or not checkPowerOfTwo(ways):
			ways = 2;
			
		if blockSize <= 0 or not checkPowerOfTwo(blockSize):
			blockSize = 64;
	
		self.ways = ways;
		self.sets = size//(ways * blockSize);
		self.blockSize = blockSize;
		self.setArray = [Set.Set(ways) for _ in range(sets)];
		
		# vars for number of accesses and cache misses to output results
		self.accesses = 0;
		self.misses = 0;
		
	
	### Operator overload for indexing (e.g. array[index]) so object can be treated as an array
	def __getitem__(self, virtualAddr) :
		virtualAddr //= 1;
		offset = virtualAddr%self.blockSize;
		setIndex = (virtualAddr//self.blockSize)%self.sets;
		tag = virtualAddr//(self.blockSize * self.sets);
		
		retval = self.setArray[setIndex].access(tag);
		
		self.accesses += 1;
		self.misses += 0 if retval['hit'] else 1;
		
		return retval['block'];
	
### checkPowerOfTwo(n) checks if a number is a power of 2
def checkPowerOfTwo(n) :
	return n%1 == 0 and math.log(n, 2)%1 == 0;
	