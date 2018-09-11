#! /usr/bin/env python3
import argparse
import time
from tsnecuda import TSNE
from perfutils.read_data import read_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", help="data file to use for test")
    args = parser.parse_args()

    X, y, _, _, _, _ = read_data(args.data_file)
    t = TSNE(n_components=2)

    start = time.time()
    X_2d = t.fit_transform(X)
    end = time.time()

    print("tsne duration: " + str((end - start)))
