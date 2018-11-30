### class for set in cache
class Set :
	
	### Constructor
    def __init__(self, ways) :
	
		# lruQueue attribute is used to find way to replace in cache miss
        self.lruQueue = [];
        self.blocks = ways * [None];
	
	### adds a new block to the set
    def access(self, tag) :
		
        print("access: " + str(tag));

        for b in self.blocks :

            if b != None and tag == b.tag :
                self.updateQueue(tag);
                return {'hit' : True, 'block': str(b)};
		
        block = self.add(tag);
        return {'hit': False, 'block' : str(block)}
		
    def add(self, tag) :
		
        print("adding " + str(tag) + " to set");
		
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
                    print("had to replace " + str(repTag))
                    self.blocks[i] = block
                    self.updateQueue(tag);
                    return block;
			
	
    def updateQueue(self, tag) :

        for i in range(len(self.lruQueue)) :
            if self.lruQueue[i] == tag :
                del self.lruQueue[i];
                print("removing " + str(tag) + " from queue");

        print("adding " + str(tag) + " to queue");
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