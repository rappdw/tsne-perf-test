Performance Comparision of Several TSNE Implementations
-------------------------------------------------------

This docker image allows for head to head performance comparisions
between different implementations of BH-tSNE.

The versions that are compared are:
* [lvdmaaten](https://github.com/lvdmaaten/bhtsne.git) (e53ec46d9...)
* [10XDev](https://github.com/10XDev/tsne.git) (1858079da...)
* [danielfrg](https://github.com/danielfrg/tsn.git) (v0.1.8)
* [rappdw](https://github.com/rappdw/tsne.git) (d7447950...)

To run the test:
1) Build to docker image: `docker build -t tsne-perf .`
2) Run the image, specifying which data set to use, e.g. `docker run -it tsne-perf iris`

# On an EC2 M5.xlarge instance
## 2500 Instance MNIST Data 

| Repo      | Wall Time (s) | Max Memory (kb) | Cumulative CPU % |
| --------- | ------------- | --------------- | ---------------- |
| lvdmaaten | 16.42         | 14700           | 99               |
| danielfrg | 7.83          | 34028           | 99               |
| 10XDev    | 7.61          | 14544           | 99               |
| rappdw    | 4.68          | 15388           | 371              |

## 70,000 Instance MNIST Data 

| Repo      | Wall Time (s) | Max Memory (kb) | Cumulative CPU % |
| --------- | ------------- | --------------- | ---------------- |
| lvdmaaten | 6475.31       | 1426732         | 99               |
| 10XDev    | 3886.93       | 1426704         | 99               |
| danielfrg | 2153.05       | 1426356         | 99               |
| rappdw    | 1428.57       | 1430140         | 379              |

