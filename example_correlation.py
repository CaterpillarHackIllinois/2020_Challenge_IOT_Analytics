import h5py
import os
import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import pearsonr
# seed random number generator

cwd = os.getcwd()

#Open the data file
filepath = cwd + '\\demo.hdf'
f = h5py.File(filepath, 'r')


#Show all channels available in file
chanIDs = f['DYNAMIC DATA']

#Plot a sample dataset
ChannelNameA = 'ch_0'
ChannelNameB = 'ch_10'
dset1 = chanIDs[ChannelNameA]['MEASURED']
dset2 = chanIDs[ChannelNameB]['MEASURED']

corr, _ = pearsonr(dset1, dset2)
print('Pearsons correlation: %.3f' % corr)

#Plot a sample dataset
plt.plot(np.arange(len(dset1[()])), dset1[()],np.arange(len(dset2[()])),dset2[()]) # plotting by columns
plt.title("plot of ch0 and ch10")
plt.xlabel("Datapoint #")
plt.ylabel("Value")
plt.show()


#Close the file
f.close()