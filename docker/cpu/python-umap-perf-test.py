#! /usr/bin/env python3
import argparse
import time
import umap
from perfutils.read_data import read_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", help="data file to use for test")
    args = parser.parse_args()

    X, _, _, _, _, _ = read_data(args.data_file)
    u = umap.UMAP(n_neighbors=5, min_dist=0.3, metric='correlation')

    start = time.time()
    X_2d = u.fit_transform(X)
    end = time.time()

    print("tsne duration: " + str((end - start)))
