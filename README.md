Performance Comparision of Several TSNE Implementations
-------------------------------------------------------

This docker image allows for head to head performance comparisions
between different implementations of BH-tSNE.

The versions that are compared are:
* [lvdmaaten](https://github.com/lvdmaaten/bhtsne.git) (e53ec46d9...)
* [10XDev](https://github.com/10XDev/tsne.git) (1858079da...)
* [rappdw](https://github.com/rappdw/tsne.git) (d7447950...)

To run the test:
1) Build to docker image: `docker build -t tsne-perf .`
2) Run the image, specifying which data set to use, e.g. `docker run -it tsne-perf iris`

# On an EC2 M4.4xlarge instance
## 2500 Instance MNIST Data 

| Repo | Wall Time (s) | Max Memory (kb) | Cumulative CPU % |
| ---- | ------------- | ----------- | ---------------- |
| lvdmaaten | 18.54 | 14676 | 100 |
| 10XDev | 10.19 | 14916 | 100 |
| rappdw | 8.05 | 16964 | 4560 |

## 70,000 Instance MNIST Data 

| Repo | Wall Time (s) | Max Memory (kb) | Cumulative CPU % |
| ---- | ------------- | ----------- | ---------------- |
| lvdmaaten | 5646.54 | 1426872 | 99 |
| 10XDev | 3758.63 | 1426960 | 99 |
| rappdw | 490.05 | 1449816 | 4360 |

