import numpy as np
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.style as mplstyle
mplstyle.use('dark_background')

for scale in range(0, 10):
    path = 'timescale' + str(scale) + '/correlation_coefficient_0.dat'
    print('Importing data: ', path)
    data = np.loadtxt(path)
    print('Data imported !')

    dissolved = []
    for x in range(17280):
	    for y in range(x, 17280):
		    dissolved.append(data[x, y])

    dissolved = np.array(dissolved)
    print('Array Dissolved !')
    n_bins = 100
    fig, axs = plt.subplots(1, 1, figsize = (10, 7), tight_layout = True)
    axs.hist(dissolved, bins = n_bins)
    axs.set_xlim(-1,1)
    axs.set_ylim(0,10e6)
    axs.set_title('Timescale: ' + str(scale + 1), fontsize = 22)
    axs.set_xlabel('Correlation', fontsize = 18)
    axs.tick_params(axis = 'x', labelsize = 14)
    axs.tick_params(axis = 'y', labelsize = 14)
    save_path = 'histogram' + str(scale) + '.png'
    print('Saving plot: ', save_path)
    plt.savefig(save_path)

