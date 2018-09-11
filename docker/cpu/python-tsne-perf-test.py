#! /usr/bin/env python3
import argparse
import time
from tsne import bh_sne
from perfutils.read_data import read_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", help="data file to use for test")
    args = parser.parse_args()

    X, _, theta, perplexity, _, _ = read_data(args.data_file)

    start = time.time()
    X_2d = bh_sne(X, perplexity=perplexity, theta=theta)
    end = time.time()

    print("tsne duration: " + str((end - start)))
