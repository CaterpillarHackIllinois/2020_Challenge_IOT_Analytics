import h5py
import os
import numpy as np
import matplotlib.pyplot as plt
cwd = os.getcwd()

#Open the data file
filepath = cwd + '\\demo.hdf'
f = h5py.File(filepath, 'r')

#Show all channels available in file
chanIDs = f['DYNAMIC DATA']

print("Channels available in this data file")
print(list(chanIDs.keys()))

#Plot a sample dataset
ChannelName = 'ch_0'
dset = chanIDs[ChannelName]['MEASURED']
plt.hist(dset, bins='auto')  # arguments are passed to np.histogram
plt.title("Histogram ch0 (without noise reduction)")
plt.xlabel("Datapoint #")
plt.ylabel("Frequency")
plt.show()

print("Max of dataset: " + str(max(dset)))
print("Min of dataset: " + str(min(dset)))

# Determined that initial 0 values are noise because of .....???
# They may not be noise. They may be noise. You may need to make your own determination of what is and isn't noise
# How do you determine what's noise? Great question! The answer is.....
plt.hist(dset[6:-1], bins='auto')  # arguments are passed to np.histogram
plt.title("Histogram ch0 (with noise reduction)")
plt.xlabel("Datapoint #")
plt.ylabel("Frequency")
plt.show()

print("Max of dataset (wo noise): " + str(max(dset[6:-1])))
print("Min of dataset (wo noise): " + str(min(dset[6:-1])))

#Close the file
f.close()