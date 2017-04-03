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

#Things still to try

* See: [Choosing the right threading framework](https://software.intel.com/en-us/articles/choosing-the-right-threading-framework) 
and determine if we should try either TBB or C++11 Threadind

* Check compiler options

* Add Maximmsch2 and Ulyanov to the mix

* Compare visualization output of the various implementations

* From conversation with Brian: 
```
[11:33 AM] Brian Jones: can you break down the total time into these stages (they are sequential):
[11:33 AM] Brian Jones: 1) vptree construction  2) vptree usage (knn calc)  3) objective function optimization
[11:34 AM] Brian Jones: if the first 2 stages dominate for the full mnist, then parallelization won't help that much, which is what the overall timing suggests
however, you can do steps 1&2 just once for a particular dataset and then run step3 mutliple times to try to find the best settings, so parallelization would still help a lot in that usage pattern
[11:35 AM] Brian Jones: we can replace the vptree with LSH if necessary
[11:35 AM] Brian Jones: the latter is only an approx knn, but much faster to construct
[11:36 AM] Brian Jones: vptree also is not n log n worst case, which i am surprised he didn't mention in his paper
hrmm, there are lots of references but i think what we would need is a c++ implementation which i don't know of off the top of my head, perhaps the FLANN library
[11:39 AM] Brian Jones: if we were to use this stuff in production, i would split out the knn stage from the tsne stage
[11:40 AM] Brian Jones: kind of like how glove separates out the cooccurence matrix calc from the optimization
[11:41 AM] Brian Jones: stage 1)  data -> knn graph.   stage 2) knn graph -> classification, clustering, viz
[11:41 AM] Brian Jones: sklearn has a ball tree for stage 1
[11:41 AM] Brian Jones: and an lshforest
[11:41 AM] Brian Jones: https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=python+lsh&...
[11:43 AM] Daniel Rapp: THis looks interesting: http://www.mit.edu/~andoni/LSH/
[11:43 AM] Brian Jones: yea Indyk and co have done a lot in the LSH field
[11:43 AM] Brian Jones: i used their euclidean lsh in the past
[11:44 AM] Brian Jones: (the most common lsh is for cosine, or angle, distance)
```
* https://www.quora.com/What-are-some-good-LSH-implementations