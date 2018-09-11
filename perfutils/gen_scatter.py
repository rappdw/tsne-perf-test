import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
plt.style.use('ggplot')
mpl.rcParams['figure.figsize'] = 20, 20

def gen_scatter_plot(X, y, image_file):
    plt.scatter(X[:, 0], X[:, 1], c=y)
    plt.savefig(image_file)
