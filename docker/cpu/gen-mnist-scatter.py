#! /usr/bin/env python3
from tsne import bh_sne
from perfutils.read_data import read_data
from perfutils.gen_scatter import gen_scatter_plot


if __name__ == '__main__':
    X, y, theta, perplexity, _, _ = read_data('data.2500.mnist.dat', label_file='labels.2500.mnist.npy')
    X = bh_sne(X, perplexity=perplexity, theta=theta)
    gen_scatter_plot(X, y, '/data/mnist.2500.png')