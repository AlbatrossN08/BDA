class BloomFilter:
    def __init__(self, size, num_hash_functions=1):
        self.size = size
        self.bit_array = [0] * size
        self.num_hash_functions = num_hash_functions
        self.count = 0

    def hash(self, item):
        # Use a hash function to map the item to a bit index
        hash_value = hash(item) % self.size
        return hash_value

    def add(self, item):
        # Set the corresponding bit in the bit array for the item
        for i in range(self.num_hash_functions):
            bit_index = self.hash(item) % self.size
            self.bit_array[bit_index] = 1
        self.count += 1

    def check(self, item):
        # Check if the corresponding bit in the bit array is set for the item
        bit_index = self.hash(item) % self.size
        return self.bit_array[bit_index] == 1

bloom_filter = BloomFilter(1000)

# Add some items to the Bloom filter
bloom_filter.add("apple")
bloom_filter.add("banana")
bloom_filter.add("orange")

# Check if an item is in the Bloom filter
is_in_filter = bloom_filter.check("apple")

print(is_in_filter)
