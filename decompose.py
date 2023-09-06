import numpy as np
from modwt import modwt

print('Importing DATA ...')
raw_data = np.loadtxt('trans_data_olr_day_avg.dat')
print('DATA Imported!')

lev, j, k = 5, len(raw_data), len(raw_data[0]) 

timescale = np.zeros((lev,j,k))
for nodes in range(0,100):#len(raw_data)):
    signal = raw_data[:,nodes]
    detail, approx = modwt(signal, 'sym4', lev)
    j = 0
    print("Working on Node ", nodes)
    for j in range(0,lev): 
        print("Decomposition Scale: ", j)
        timescale[j,:,nodes] = approx[j]

for file in range(lev):
    file_path = 'timescale-' + str(file) + '.txt'
    np.savetxt(file_path, timescale[file, :, :])
    print("File Saved: Timescale - ", file)
