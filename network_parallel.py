import numpy as np
from numba import njit,prange

percentile_list = [0.6007499999999999, 0.5907499999999999, 0.5800000000000002, 0.5705, 0.5562499999999998, 0.5389999999999998, 0.5247499999999998, 0.5150000000000001, 0.5087499999999999, 0.5047499999999999]

for scale in range(0,10):
    file_path = '../timescale' + str(scale) + '/correlation_coefficient_0.dat'
    print('The data is being Imported: ', file_path)
    data = np.loadtxt(file_path)
    print('Data Imported !')
    N = len(data[0])
    A = np.zeros((N, N))
    percentile_val = percentile_list[scale]
    print('The value of correlation for the 75th percentile is ', percentile_val)

    @njit(parallel = True)
    def adj_cons(data, A, N):
        for i in prange(N):
            for j in prange(i, N):
                if data[i,j] > percentile_val:
                    A[i,j] = 1
                    A[j,i] = 1
        return A

    AA = adj_cons(data, A, N)

    np.savetxt('../timescale' + str(scale) +'/adj75_' + str(scale) + '.txt', AA, fmt = '%i')
