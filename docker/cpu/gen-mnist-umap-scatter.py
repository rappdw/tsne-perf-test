#! /usr/bin/env python3
import umap
from perfutils.read_data import read_data
from perfutils.gen_scatter import gen_scatter_plot


if __name__ == '__main__':
    X, y, theta, perplexity, _, _ = read_data('data.full.mnist.dat', label_file='labels.full.mnist.npy')
    u = umap.UMAP(n_neighbors=5, min_dist=0.3, metric='correlation')
    X = u.fit_transform(X)
    gen_scatter_plot(X, y, '/data/mnist.full.umap.png')