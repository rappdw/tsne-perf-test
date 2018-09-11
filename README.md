# Performance Comparision of Several TSNE Implementations

This docker image allows for head to head performance comparisions
between different implementations of BH-tSNE.

The versions that are compared are:
* [lvdmaaten](https://github.com/lvdmaaten/bhtsne.git) (e53ec46d9...)
* [10XDev](https://github.com/10XDev/tsne.git) (1858079da...)
* [danielfrg](https://github.com/danielfrg/tsn.git) (v0.1.8) (This is the library on pypi)
* [resero-labs](https://github.com/rappdw/tsne.git) (v0.1.9) (This is now available on pypi as tsne-mp)
* [tsne-cuda](https://github.com/CannyLab/tsne-cuda) (This is available on pypi as tsnecuda)

To run the test:

* pre-requisites
  1) python 3.6 or greater
  2) dockerutils (`pip install dockerutils`)
  3) setup EC2 instances (M5 and P3 for CPU and GPU testing)

* Build & run
  1) build tsne-cuda python wheel and libfaiss.so, place them in ./docker/gpu (tsne-cuda is under active development 
  and getting the correct version of the wheel and libfaiss.so is a bit tricky, see dwr/explorations branch on 
  [this fork](https://github.com/rappdw/tsne-cuda) of tsne-cuda)
  2) `build-image all` (builds two docker images, tsne-perf-test-cpu and tsne-perf-test-gpu)
  3) For CPU test, `run-image cpu -c full.mnist` (or iris, or 2500.mnist or cifar)
  4) for GPU test, `run-image -g gpu -c full.mnist`

## vs. scikit-learn impl
Because of implementation differences I don't include scikit-learn in the performance test. scikit-learn performs significantly slower than any of these implementations (approximately
twice as long as the lvdmaaten implementation with informal testing).

## On an EC2 m5.12xlarge instance
### 2500 Instance MNIST Data 

| Repo        | Wall Time (s) | Max Memory (kb) | Cumulative CPU % |
| ----------- | ------------- | --------------- | ---------------- |
| lvdmaaten   | 16.04         | 14516           | 99               |
| danielfrg   | 7.80          | 34096           | 99               |
| 10XDev      | 7.69          | 14612           | 99               |
| resero-labs | 3.15          | 13020           | 3948             |

### 70,000 Instance MNIST Data 

| Repo        | Wall Time (s) | Max Memory (kb) | Cumulative CPU % |
| ----------- | ------------- | --------------- | ---------------- |
| lvdmaaten   | 6064.91       | 1426784         | 99               |
| 10XDev      | 3753.59       | 1426692         | 99               |
| danielfrg   | 2100.58       | 1426288         | 99               |
| resero-labs | 329.98        | 1436172         | 3588             |

## On an EC2 p3.2xlarge instance

### 70,000 Instance MNIST Data
| Repo        | Wall Time (s) | Max Memory (kb) | Cumulative CPU % |
| ----------- | ------------- | --------------- | ---------------- |
| resero-labs | 798.18        | 1504632         | 714              |
| tsne-cuda   | 22.59         | 2456588         | 123              |

### Results from these runs

#### Resero-labs tsne-mp
![resero-labs](./mnist.full.tsnemp.png "Resero-labs tsne embedding")

#### tsne-cuda
![tsne-cuda](./mnist.full.tsnecuda.png "tsne-cuda tsne embedding")

## Conclusions

If you have a gpu and you are willing to work with early days code, the tsne-cuda implementation beats all others
handsdown.

If you don't have a gpu, then use the resero-labs implementation or consider [umap](https://github.com/lmcinnes/umap)
instead of tsne.
