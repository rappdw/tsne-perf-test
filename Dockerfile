FROM gcc:6.3

RUN apt-get update && apt-get install -y \
        less \
        python3 \
        time \
        vim \
        wget \
    && apt-get clean && \
    rm -rf /var/tmp /tmp /var/lib/apt/lists/*


WORKDIR /sandbox
RUN git clone https://github.com/rappdw/tsne.git tsne.rappdw \
    && git clone https://github.com/10XDev/tsne.git tsne.10XDev \
    && git clone https://github.com/lvdmaaten/bhtsne.git tsne.lvdmaaten

ADD Makefile.10XDev.variants /sandbox/tsne.rappdw/tsne/bh_sne_src/Makefile
ADD Makefile.10XDev.variants /sandbox/tsne.10XDev/tsne/bh_sne_src/Makefile
ADD Makefile.lvdmaaten.variants /sandbox/tsne.lvdmaaten/Makefile

RUN cd /sandbox/tsne.rappdw/tsne/bh_sne_src; make clean all \
    && cd /sandbox/tsne.10XDev/tsne/bh_sne_src; make clean all \
    && cd /sandbox/tsne.lvdmaaten; make clean all

RUN wget -q https://s3-us-west-2.amazonaws.com/resero/datasets/tsne-perf-test/data.2500.mnist.dat \
    && wget -q https://s3-us-west-2.amazonaws.com/resero/datasets/tsne-perf-test/data.full.mnist.dat \
    && wget -q https://s3-us-west-2.amazonaws.com/resero/datasets/tsne-perf-test/data.iris.dat

ADD tsne-perf-test.py .

ENTRYPOINT ["/sandbox/tsne-perf-test.py"]
CMD ["--help"]

