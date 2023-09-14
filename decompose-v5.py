import numpy as np 
from modwt import modwt 
print('Importing Info about the Data frame ...') 
file_path = 'trans_data_olr.dat'
#nodes = np.genfromtxt(file_path, delimiter = ' ', max_rows = 1).shape[0]
#Manual entry of nodes
initial = int(input('Enter the initial node: ')) 
final = int(input('Enter the final node: '))

# for the data I use here, the j (no. of observations) is 87663
# for other data, replace the number with this function
#j = np.genfromtxt(file_path, delimiter = ' ', usecols = 1).shape[0]
j = 87664

print('Nodes = ' + str(initial) + ' - ' + str(final))
print('Time Points = ', j)
lev = 10
print(str(lev) + ' levels of wavelet decomposition')
data = np.genfromtxt(file_path, delimiter = " ", usecols = range(initial,final))
timescale = np.zeros((lev,j,int(final - initial)))
print('Timescale Matrix with shape ' + str(timescale.shape) + ' generated !')

for i in range(0, int(final - initial)):
    print('\nLoading Node ', initial + i)
    signal = data[:,i]
    detail, approx = modwt(signal, 'sym4', lev)
    j = 0
    print("\nWorking on Node ", initial + i)
    print("batch - Nodes = " + str(initial) + ' - ' + str(final) +"  Decomposition Scale: ")
    for j in range(0,lev): 
        print(j, end=" ")
        timescale[j,:,i] = approx[j]
print('\nNodes = ' + str(initial) + ' - ' + str(final))
for file in range(lev):
    file_path = 'decompose1/batch' + str(final) + '-timescale-' + str(file) + '.txt'

    np.savetxt(file_path, timescale[file, :, :])
    print("File Saved: Batch - " + str(final) + " | Timescale - ", file)
