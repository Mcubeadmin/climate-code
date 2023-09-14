import numpy as np

batch = [200,300,400,500,700,1000,1500,2000,2500,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,14000,15000,16000,17000,17280]
data = np.loadtxt('batch100-timescale-6.txt')

for node in batch:
    file_path = 'batch' + str(node) + '-timescale-6.txt'
    print('Importing file: ', file_path)
    data = np.concatenate((data, np.loadtxt(file_path)), axis = 1)
    print(data.shape)
    print('Data appended !')

print('Saving Combined File')
np.savetxt('combine-timescale-6.txt', data)
    
