### class for set in cache
class Set :
	
	### Constructor
    def __init__(self, ways) :
	
		# lruQueue attribute is used to find way to replace in cache miss
        self.lruQueue = [];
        self.blocks = ways * [None];
	
	### adds a new block to the set
    def access(self, tag) :
		
        #print("access: " + str(tag));

        for b in self.blocks :

            if b != None and tag == b.tag :
                self.updateQueue(tag);
                return {'hit' : True, 'replace' : False, 'block': str(b)};
		
        rv = self.add(tag);
        block = rv[1];
        return {'hit': False, 'replace' : rv[0], 'block' : str(block)}
		
	### add(tag)
	### 	DESCRIPTION:
	### 		Inserts a new cache line into the set. Either places it in an empty space or replaces the least recently used cache line.
	###		ARGUMENTS:
	###			tag - Tag of the cache line to be added.
	###		RETURN VALUE:
	###			A list with: [boolean for replaced or not, block added]
    def add(self, tag) :
		
        #print("adding " + str(tag) + " to set");
		
    	# Create new block (block.data would be assigned if we were actually accessing memory locs)
        block = Block();
        block.tag = tag;
		
		# Find an invalid way in the set (invalid blocks have the value None)
        for i in range(len(self.blocks)) :
            if self.blocks[i] == None :
                self.blocks[i] = block;
				
                self.updateQueue(tag)
                return [False, block];
		
		# If no invalid ways check the end of the queue
        if len(self.lruQueue) != 0 :
            repTag = self.lruQueue[len(self.lruQueue) - 1];
            for i in range(len(self.blocks)) :
                if(self.blocks[i].tag == repTag) :
                    #print("had to replace " + str(repTag))
                    self.blocks[i] = block;
                    self.updateQueue(tag);
                    return [True, block];
			
	### updateQueue(tag)
	###		DESCRIPTION:
	###			Adds a tag to replacement queue, if already in replacement queue, delete the older value
	###		ARGUMENTS:
	###			tag - tag to be added
    def updateQueue(self, tag) :

        for i in range(len(self.lruQueue)) :
            if self.lruQueue[i] == tag :
                del self.lruQueue[i];
                #print("removing " + str(tag) + " from queue");
                break;

        #print("adding " + str(tag) + " to queue");
        self.lruQueue.insert(0, tag);
        if len(self.lruQueue) > len(self.blocks) :
            del self.lruQueue[len(self.lruQueue) - 1];
		
### class for individual cache line/block in cache
class Block :

    def __init__(self) :
        self.tag = 0;
        self.valid = False;
        self.data = 0;

    def __str__(self) :
        return "(" + str(self.tag) + ", " + str(self.valid) + ", " + str(self.data) + ")";