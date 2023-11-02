from dgim import Dgim

# Create a new DGIM object
dgim= Dgim(N=32, error_rate=0.1)
for i in range(100):
  # Update the DGIM object with some new bits
  dgim.update(True)
  dgim.update(True)
  dgim.update(False)
  

#no. of 1s in the window
count = dgim.get_count()

print(count)

'''
def DGIM(window_size, stream):
    counter = 0
    queue = []
    buckets = []

    for bit in stream:
        queue.append(bit)
        if bit == '1':
            counter += 1

        if len(queue) > window_size:
            # Shift out the oldest bit
            if queue.pop(0) == '1':
                counter -= 1

        if len(queue) == window_size:
            # When the queue reaches the window size, add a new bucket
            buckets.append(counter)

    # Handle buckets that fall outside the window
    for i in range(len(buckets) - 1, -1, -1):
        if 2 ** i <= window_size:
            return buckets[i]

# Example usage:
stream = '100100111010011010110101010010101001'
window_size = 10
result = DGIM(window_size, stream)
print(result)
'''
