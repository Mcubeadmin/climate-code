import numpy as np

def pearson_correlation(x, y):
    # Calculate the mean of each time series
    mean_x = np.mean(x)
    mean_y = np.mean(y)

    # Calculate the standard deviation of each time series
    std_x = np.std(x)
    std_y = np.std(y)

    # Calculate the covariance between the two time series
    covariance = np.mean((x - mean_x) * (y - mean_y))

    # Calculate the Pearson correlation coefficient
    correlation = covariance / (std_x * std_y)

    return correlation

for scale in range(1,5):

    path = 'timescale-' + str(scale) + '.txt'
    print('Importing DATA ...', path)
    raw_data = np.loadtxt(path)
    print('DATA Imported!')
    

    rows = cols = len(raw_data[0])
    corr_mat = np.zeros((rows,cols))

    for x in range(len(raw_data[0])):
        print('Working on Node: ', x)
        for y in range(x, len(raw_data[0])):
            if x == y:
                corr_mat[x, y] = 1
            else:
                series1 = raw_data[:,x]
                series2 = raw_data[:,y]
                corr_coeff = pearson_correlation(series1, series2)
                corr_mat[x, y] = corr_coeff
                corr_mat[y, x] = corr_coeff 
    print('Saving file: correlation' + str(scale) + '.txt')
    np.savetxt('correlation' + str(scale) + '.txt', corr_mat)
            