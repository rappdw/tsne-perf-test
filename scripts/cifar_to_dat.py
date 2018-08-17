#!/usr/bin/env python3
'''
Converts files in other formats to the lvmaaten dat file definition
'''
import pickle
import struct
import sys

import numpy as np

def unpickle_cifar(file):
    '''unpickle the cifar data files'''
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
        # this dict has keys: b'batch_label', b'labels', b'data', and b'filenames'
        # data == X; labels == y
    return dict

def pack(X, theta=0.5, perplexity=5.0, no_dims=2, max_iter=1000):
    (N, D) = X.shape
    X1d = X.flatten()
    return struct.pack(f'@iiddii{X1d.shape[0]}d', N, D, theta, perplexity, no_dims, max_iter, *X1d)

if __name__ == "__main__":
    # input_file = sys.argv[1]
    # output_file = input_file + '.dat'
    #
    # open(output_file, 'wb').write(pack(unpickle_cifar(input_file)[b'data']))

    X = None
    for i in range(1, 6):
        X_i = unpickle_cifar(f'/workspace/cifar/cifar-10-batches-py/data_batch_{i}')[b'data']
        if X is None:
            X = X_i
        else:
            X = np.concatenate((X, X_i))
    open('/workspace/cifar/cifar-10-batches-py/data.cifar.dat', 'wb').write(pack(X))
