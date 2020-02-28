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

#Attempting to predict channel 0 with channel 10's data
# Try to predict by multiply by pi???
dset1_prediction = dset2[()] * np.pi


#Plot a sample dataset
plt.plot(np.arange(len(dset1[()])), dset1[()],np.arange(len(dset1_prediction)),dset1_prediction) # plotting by columns
plt.title("plot of ch0 and ch0 prediction")
plt.xlabel("Datapoint #")
plt.ylabel("Value")
plt.show()

error = np.mean(abs(dset1 - dset1_prediction))
print("Mean Absolute Error : " + str(error))

#Close the file
f.close()