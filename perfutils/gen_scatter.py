import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def gen_scatter_plot(X, y, image_file):
    plt.scatter(X[:, 0], X[:, 1], c=y)
    plt.savefig(image_file)
