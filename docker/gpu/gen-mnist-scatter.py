#! /usr/bin/env python3
from tsnecuda import TSNE
from perfutils.read_data import read_data
from perfutils.gen_scatter import gen_scatter_plot


if __name__ == '__main__':
    X, y, _, _, _, _ = read_data('data.2500.mnist.dat', label_file='labels.2500.mnist.npy')
    t = TSNE(n_components=2)
    X = t.fit_transform(X)

    gen_scatter_plot(X, y, '/data/mnist.2500.png')