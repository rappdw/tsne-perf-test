# Performance Comparision of Several TSNE Implementations

This docker image allows for head to head performance comparisions
between different implementations of BH-tSNE.

The versions that are compared are:
* [lvdmaaten](https://github.com/lvdmaaten/bhtsne.git) (e53ec46d9...)
* [10XDev](https://github.com/10XDev/tsne.git) (1858079da...)
* [danielfrg](https://github.com/danielfrg/tsn.git) (v0.1.8) (This is the library on pypi)
* [rappdw](https://github.com/rappdw/tsne.git) (d7447950...)

To run the test:
1) Build to docker image: `docker build -t tsne-perf .`
2) Run the image, specifying which data set to use, e.g. `docker run -it tsne-perf iris`
**NOTE: do not run -d, for some reason, this slows things down significatnly. if you need to detach, use ctl-p, ctrl-q**

## vs. scikit-learn impl
Because of implementation differences I don't include scikit-learn in the performance test. Because of the implementation
chosen in scikit-learn, it performs significantly slower than any of these implementations (approximately
twice as long as the lvdmaaten implementation).

## On an EC2 m5.12xlarge instance
### 2500 Instance MNIST Data 

| Repo      | Wall Time (s) | Max Memory (kb) | Cumulative CPU % |
| --------- | ------------- | --------------- | ---------------- |
| lvdmaaten | 16.04         | 14516           | 99               |
| danielfrg | 7.80          | 34096           | 99               |
| 10XDev    | 7.69          | 14612           | 99               |
| rappdw    | 3.15          | 13020           | 3948             |

### 70,000 Instance MNIST Data 

| Repo      | Wall Time (s) | Max Memory (kb) | Cumulative CPU % |
| --------- | ------------- | --------------- | ---------------- |
| lvdmaaten | 6064.91       | 1426784         | 99               |
| 10XDev    | 3753.59       | 1426692         | 99               |
| danielfrg | 2100.58       | 1426288         | 99               |
| rappdw    | 329.98        | 1436172         | 3588             |

