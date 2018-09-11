#! /usr/bin/env python3
import numpy as np
import time
import struct

def read_data(data_file, label_file=None):
    start = time.time()
    data = open(data_file, 'rb').read()
    (N, D, theta, perplexity, no_dims, max_iter) = struct.unpack("@iiddii", data[:32])
    X = np.reshape(np.fromstring(data[32:], np.float64), (N, D))
    y = None
    if label_file:
        y = np.load(label_file)
    end = time.time()
    print("load duration: " + str((end - start)))
    return X, y, theta, perplexity, no_dims, max_iter
