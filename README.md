Performance Comparision of Several TSNE Implementations
-------------------------------------------------------

This docker image allows for head to head performance comparisions
between different implementations of BH-tSNE.

The versions that are compared are:
* [lvdmaaten](https://github.com/lvdmaaten/bhtsne.git) (e53ec46d9...)
* [10XDev](https://github.com/10XDev/tsne.git) (1858079da...)
* [rappdw](https://github.com/rappdw/tsne.git) (0792618da...)

To run the test:
1) Build to docker image: `docker build -t tsne-perf .`
2) Run the image, specifying which data set to use, e.g. `docker run -it tsne-perf iris`

# On an EC2 M4.large instance
## 2500 Instance MNIST Data 

| Repo | Wall Time (s) | Max Memory (kb) | Cumulative CPU % |
| ---- | ------------- | ----------- | ---------------- |
| lvdmaaten | 20.26 | 14572 | 99 |
| 10XDev | 11.23 | 15148 | 99 |
| rappdw | 10.24 | 15172 | 182 |

## 70,000 Instance MNIST Data 

| Repo | Wall Time (s) | Max Memory (kb) | Cumulative CPU % |
| ---- | ------------- | ----------- | ---------------- |
| lvdmaaten | 5712.88 | 1426888 | 99 |
| 10XDev | 4938.13 | 1427264 | 99 |
| rappdw | 4858.7 | 1427336 | 106 |

# On an EC2 M4.4xlarge instance
## 2500 Instance MNIST Data 

| Repo | Wall Time (s) | Max Memory (kb) | Cumulative CPU % |
| ---- | ------------- | ----------- | ---------------- |
| lvdmaaten | 19.61 | 14708 | 99 |
| 10XDev | 9.69 | 15204 | 99 |
| rappdw | 7.99 | 15164 | 3992 |

## 70,000 Instance MNIST Data 

| Repo | Wall Time (s) | Max Memory (kb) | Cumulative CPU % |
| ---- | ------------- | ----------- | ---------------- |
| lvdmaaten | 5646.54 | 1426872 | 99 |
| 10XDev | 4995.76 | 1427456 | 100 |
| rappdw | 4802.48 | 1427456 | 140 |
