#!/usr/bin/env python3
'''
Converts mnist to the lvmaaten dat file definition (https://lvdmaaten.github.io/tsne/User_guide.pdf)
'''
import os
import struct
import numpy as np

from pack_data import pack

def read(dataset="training", path="."):
    if dataset is "training":
        fname_img = os.path.join(path, 'train-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 'train-labels-idx1-ubyte')
    elif dataset is "testing":
        fname_img = os.path.join(path, 't10k-images-idx3-ubyte')
        fname_lbl = os.path.join(path, 't10k-labels-idx1-ubyte')
    else:
        raise ValueError("dataset must be 'testing' or 'training'")

    # Load everything in some numpy arrays
    with open(fname_lbl, 'rb') as flbl:
        magic, num = struct.unpack(">II", flbl.read(8))
        lbl = np.fromfile(flbl, dtype=np.int8)

    with open(fname_img, 'rb') as fimg:
        magic, num, rows, cols = struct.unpack(">IIII", fimg.read(16))
        img = np.fromfile(fimg, dtype=np.uint8).reshape(len(lbl), rows, cols)

    return img, lbl

if __name__ == "__main__":

    X_training, y_training = read(path="/workspace/mnist", dataset="training")
    X_testing, y_testing = read(path="/workspace/mnist", dataset="testing")

    xform_1d = lambda X: np.reshape(X, (X.shape[0], X.shape[1] * X.shape[2]))

    X_training = xform_1d(X_training)
    X_testing = xform_1d(X_testing)

    full_mnist = np.concatenate((X_training, X_testing))
    full_mnist_labels = np.concatenate((y_training, y_testing))

    idx = np.random.choice(np.arange(X_training.shape[0]), 2500, replace=False)
    mnist_2500 = full_mnist[idx]
    mnist_2500_labels = full_mnist_labels[idx]

    open('/workspace/mnist/data.full.mnist.dat', 'wb').write(pack(full_mnist))
    open('/workspace/mnist/data.2500.mnist.dat', 'wb').write(pack(mnist_2500))

    np.save('/workspace/mnist/labels.full.mnist', full_mnist_labels)
    np.save('/workspace/mnist/labels.2500.mnist', mnist_2500_labels)
