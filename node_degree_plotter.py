import numpy as np
import matplotlib.pyplot as plt

for scale in range(0, 10):
    file_path = 'timescale' + str(scale) + '/degree' + str(scale) + '.txt'
    print('Importing Data: ', file_path)
    degree = np.loadtxt(file_path)
    
    nodes = np.arange(0, 17280)
    plt.figure(figsize = (10, 6))
    plt.plot(degree, nodes)
    plt.xlabel('Degree', fontsize = 14)
    plt.ylabel('Nodes', fontsize = 14)
    plt.title('Node - Degree plot at Timescale ' + str(scale + 1), fontsize = 18)
    save_path = 'node_degree_plot_' + str(scale) + '.png'
    print('Saving plot: ', save_path)
    plt.savefig(save_path)
    
    