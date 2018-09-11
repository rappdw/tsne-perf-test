#!/usr/bin/env python3
'''
Converts cifar to the lvmaaten dat file definition (https://lvdmaaten.github.io/tsne/User_guide.pdf)
'''
import pickle

import numpy as np

from pack_data import pack

def unpickle_cifar(file):
    '''unpickle the cifar data files'''
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
        # this dict has keys: b'batch_label', b'labels', b'data', and b'filenames'
        # data == X; labels == y
    return dict

if __name__ == "__main__":
    # input_file = sys.argv[1]
    # output_file = input_file + '.dat'
    #
    # open(output_file, 'wb').write(pack(unpickle_cifar(input_file)[b'data']))

    X = None
    y = None
    for i in range(1, 6):
        cifar = unpickle_cifar(f'/workspace/cifar/cifar-10-batches-py/data_batch_{i}')
        X_i = cifar[b'data']
        y_i = cifar[b'labels']
        if X is None:
            X = X_i
            y = y_i
        else:
            X = np.concatenate((X, X_i))
            y = np.concatenate((y, y_i))
    open('/workspace/cifar/cifar-10-batches-py/data.cifar.dat', 'wb').write(pack(X))
    np.save('/workspace/cifar/cifar-10-batches-py/labels.cifar', y)
