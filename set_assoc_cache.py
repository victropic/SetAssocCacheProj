import math;

### Class that holds all data for a set associative cache
### 	direct mapped cache can be created with sets as number of block and only one way
###		fully associative can be created with one set and ways as the number of blocks 
class Cache :

	### Constructor
	###    sets: number of sets
	###    ways: number of ways
	###    blockSize: size of a block/cache line in the cache
	def __init__(self, sets, ways, blockSize):
	
		# check that args are all powers of two
		if sets <= 0 or not checkPowerOfTwo(sets):
			sets = 32;
	
		if ways <= 0 or not checkPowerOfTwo(ways):
			ways = 2;
			
		if blockSize <= 0 or not checkPowerOfTwo(blockSize):
			blockSize = 64;
	
		self.ways = ways;
		self.sets = sets//ways;
		self.blockSize = blockSize;
		self.setArray = [Set(ways) for _ in range(sets)];
		
		# vars for number of accesses and cache misses to output results
		self.accesses = 0;
		self.misses = 0;
		
	
	### Operator overload for indexing (e.g. array[index]) so object can be treated as an array
	def __getitem__(self, virtualAddr):
		virtualAddr //= 1;
		clIndex = virtualAddr%self.blockSize;
		setIndex = (virtualAddr//self.blockSize)%self.sets;
		tag = virtualAddr//(self.blockSize * self.sets);
		
				
		
		return 0;
		
### class for set in cache
class Set :
	
	### Constructor
	def __init__(self, ways) :
	
		# lruQueue attribute is used to find
		self.lruQueue = [];
		self.blocks = ways * [None];
	
	### adds a new block to the set
	def access(self, tag) :
		
		for b in self.blocks) :
			if b != None and tag == b.tag:
				return {'hit' : True, 'block': b};
		
		block = self.replace(tag);
		return {'hit': False, 'block' : block}
		
	def replace(self, tag) :
		
		# Create new block (block.data would be assigned if we were actually accessing memory locs)
		block = Block();
		block.tag = tag;
		
		# Find an invalid way in the set (invalid blocks have the value None)
		for i in range(len(self.blocks)) :
			if self.blocks[i] == None :
				self.blocks[i] = block;
				
				self.updateQueue(tag)
				return block;
		
		# If no invalid ways check the end of the queue
		if len(self.lruQueue) != 0 :
			repTag = self.lruQueue[len(self.lruQueue) - 1];
			for i in range(len(self.blocks)) :
				if(self.blocks[i].tag == repTag) :
					
			
	
	def updateQueue(self, tag) :
		self.lruQueue.insert(0, tag);
		if len(self.lruQueue) > len(self.blocks) :
			del self.lruQueue[len(self.blocks) - 1];
		
### class for individual cache line/block in cache
class Block :

	def __init__(self) :
		self.tag = 0;
		self.data = 0;
	
### checkPowerOfTwo(n) checks if a number is a power of 2
def checkPowerOfTwo(n) :
	return n%1 == 0 and math.log(n, 2)%1 == 0;
	