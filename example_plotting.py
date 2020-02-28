import h5py
import os
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
plt.plot(dset[()]) # plotting by columns
plt.title("Value of " + ChannelName)
plt.xlabel("Datapoint #")
plt.ylabel("Value")
plt.show()

#Close the file
f.close()