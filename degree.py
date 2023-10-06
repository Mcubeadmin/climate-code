import numpy as np 

for scale in range(0,10):
    file_path = '../timescale' + str(scale) + '/adj75_' + str(scale) + '.txt'
    print('Importing data: ', file_path) 
    data = np.loadtxt(file_path)
    print('Data imported!')
    
    degree = np.sum(data, axis = 1)
    
    savepath = '../timescale' + str(scale) + '/degree75_' + str(scale) + '.txt'
    print('Saving file at ', savepath)
    np.savetxt(savepath, degree)
