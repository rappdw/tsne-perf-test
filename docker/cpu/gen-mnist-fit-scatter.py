#! /usr/bin/env python3
from fitsne import FItSNE
from perfutils.read_data import read_data
from perfutils.gen_scatter import gen_scatter_plot


if __name__ == '__main__':
    X, y, theta, perplexity, _, _ = read_data('data.full.mnist.dat', label_file='labels.full.mnist.npy')
    X = FItSNE(X, fft_not_bh=True, ann_not_vptree=True)
    gen_scatter_plot(X, y, '/data/mnist.full.fitsne.png')