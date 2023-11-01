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
