FROM rappdw/nvidia-python:latest

ADD docker/gpu/install-mkl.sh /usr/local/bin/

RUN apt-get update; apt-get install -y \
        time \
        wget \
    ; \
    install-mkl.sh; \
    apt-get clean; \
    rm -rf /var/tmp/* /tmp/* /var/lib/apt/lists/*

WORKDIR /sandbox

# setup data
RUN wget -q https://s3-us-west-2.amazonaws.com/resero2/datasets/tsne-perf-test/data.2500.mnist.dat.gz; \
    wget -q https://s3-us-west-2.amazonaws.com/resero2/datasets/tsne-perf-test/labels.2500.mnist.npy; \
    wget -q https://s3-us-west-2.amazonaws.com/resero2/datasets/tsne-perf-test/data.full.mnist.dat.gz; \
    wget -q https://s3-us-west-2.amazonaws.com/resero2/datasets/tsne-perf-test/labels.full.mnist.npy; \
    wget -q https://s3-us-west-2.amazonaws.com/resero2/datasets/tsne-perf-test/data.iris.dat; \
    wget -q https://s3-us-west-2.amazonaws.com/resero2/datasets/tsne-perf-test/data.cifar.dat.gz; \
    wget -q https://s3-us-west-2.amazonaws.com/resero2/datasets/tsne-perf-test/labels.cifar.npy; \
    gunzip *.gz

# This assumes that you've built tsnecuda with mkl enabled and that the artifacts, tsnecuda-xxx.whl and libfaiss.so
# have been placed in the docker/gpu directory

# /usr/local/nvidia/lib is in LD_LIBRARY_PATH, place libfaiss.so there...
RUN mkdir -p /usr/local/nvidia/lib
COPY docker/gpu/libfaiss.so /usr/local/nvidia/lib
COPY docker/gpu/tsnecuda-0.1.0-py3-none-any.whl /tmp/

RUN mkdir perfutils
COPY perfutils/* ./perfutils/
ADD setup.py .
RUN . /.venv/bin/activate; \
    pip install /tmp/tsnecuda-0.1.0-py3-none-any.whl .

ADD docker/gpu/tsne-perf-test.py .
ADD docker/gpu/python-tsne-perf-test.py .
ADD docker/gpu/gen-mnist-scatter.py .

ENV PYTHONUNBUFFERED=TRUE

ENTRYPOINT ["/sandbox/tsne-perf-test.py"]
CMD ["--help"]
