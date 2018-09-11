import struct

def pack(X, theta=0.5, perplexity=5.0, no_dims=2, max_iter=1000):
    (N, D) = X.shape
    X1d = X.flatten()
    return struct.pack(f'@iiddii{X1d.shape[0]}d', N, D, theta, perplexity, no_dims, max_iter, *X1d)
