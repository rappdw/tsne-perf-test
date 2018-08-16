#! /usr/bin/env python3
import argparse
import numpy as np
import time
import struct
from tsne import bh_sne


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", help="data file to use for test")
    args = parser.parse_args()

    start = time.time()
    data = open(args.data_file, 'rb').read()
    (N, D, theta, perplexity, no_dims, max_iter) = struct.unpack("@iiddii", data[:32])
    X = np.reshape(np.fromstring(data[32:], np.float64), (N, D))
    after_load_start = time.time()
    X_2d = bh_sne(X, perplexity=perplexity, theta=theta)
    end = time.time()


    print("load duration: " + str((after_load_start - start)))
    print("tsne duration: " + str((end - after_load_start)))
