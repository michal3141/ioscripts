import os, commands
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate

def main():
    alphas = []
    deltas = []
    values = []
    for filename in sorted(os.listdir('out')):
        print 'filename: ', filename
        #output = commands.getstatusoutput('tail -1 out/%s' % filename)
        #print 'output: ', output
    
        vals = []
        with open(os.path.join('out', filename), 'r') as f:
            for line in f:
                vals.append(float(line.replace('Percentage of cooperations', "").strip()))

        # Average cooperation percentage
        avg = sum(vals) / len(vals)
        
        alpha, delta, iters = filename.split('_')

        alphas.append(float(alpha))
        deltas.append(float(delta))
        values.append(avg)

    x = np.array(deltas)
    y = np.array(alphas)
    z = np.array(values)

    # Set up a regular grid of interpolation points
    xi, yi = np.linspace(x.min(), x.max(), 100), np.linspace(y.min(), y.max(), 100)
    xi, yi = np.meshgrid(xi, yi)

    # Interpolate
    rbf = scipy.interpolate.Rbf(x, y, z, function='linear')
    zi = rbf(xi, yi)

    plt.imshow(zi, vmin=z.min(), vmax=z.max(), origin='lower',
                   extent=[x.min(), x.max(), y.min(), y.max()])
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    plt.xlabel(r'Continuation probability $\delta$')
    plt.ylabel(r'Population structure $\alpha$')
    plt.scatter(x, y, c=z)
    cb = plt.colorbar()
    cb.set_label('Cooperation')
    plt.show()

if __name__ == '__main__':
    main()
