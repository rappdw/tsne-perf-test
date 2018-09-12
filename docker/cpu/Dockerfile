FROM continuumio/miniconda3

RUN apt-get update && apt-get install -y \
        less \
        git \
        build-essential \
        libatlas-base-dev \
        time \
        vim \
        wget \
        zip \
    && apt-get clean && \
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

# get and extract resero-labs version
RUN wget -q -O resero-labs.zip https://github.com/resero-labs/tsne/archive/v0.1.12.zip \
    && unzip -q resero-labs.zip tsne-0.1.12/tsne/bh_sne_src/* -d tsne.resero-labs \
    && mv tsne.resero-labs/tsne-0.1.12/tsne/bh_sne_src/* tsne.resero-labs \
    && rm -rf tsne.resero-labs/tsne-0.1.12 \
    && rm resero-labs.zip \
    && cp -r tsne.resero-labs tsne.resero-labs.noopenmp # create a non openmp version

# get and extract 10XDev version
RUN wget -q -O 10XDev.zip https://github.com/10XDev/tsne/archive/1858079dac9682ac38951db3143b825a4ed9d098.zip \
    && unzip -q 10XDev.zip tsne-1858079dac9682ac38951db3143b825a4ed9d098/tsne/bh_sne_src/* -d tsne.10XDev \
    && mv tsne.10XDev/tsne-1858079dac9682ac38951db3143b825a4ed9d098/tsne/bh_sne_src/* tsne.10XDev \
    && rm -rf tsne.10XDev/tsne-1858079dac9682ac38951db3143b825a4ed9d098 \
    && rm 10XDev.zip

# get and extract lvdmaaten
RUN wget -q -O lvdmaaten.zip https://github.com/lvdmaaten/bhtsne/archive/ff73828c476ba079fb53a50ad74f52ca01457d16.zip \
    && unzip -q lvdmaaten.zip -d tsne.lvdmaaten \
    && mv tsne.lvdmaaten/bhtsne-ff73828c476ba079fb53a50ad74f52ca01457d16/* tsne.lvdmaaten \
    && rm -rf tsne.lvdmaaten/bhtsne-ff73828c476ba079fb53a50ad74f52ca01457d16 \
    && rm lvdmaaten.zip

# get and extract danielfrg
RUN wget -q -O danielfrg.zip https://github.com/danielfrg/tsne/archive/0.1.8.zip \
    && unzip -q danielfrg.zip tsne-0.1.8/tsne/bh_sne_src/* -d tsne.danielfrg \
    && mv tsne.danielfrg/tsne-0.1.8/tsne/bh_sne_src/* tsne.danielfrg/ \
    && rm -rf tsne.danielfrg/tsne-0.1.8 \
    && rm danielfrg.zip

#RUN conda install numpy cython

ADD docker/cpu/Makefile.resero-labs.openmp /sandbox/tsne.resero-labs/Makefile
RUN cd /sandbox/tsne.resero-labs; make clean all

ADD docker/cpu/Makefile.resero-labs.noopenmp /sandbox/tsne.resero-labs.noopenmp/Makefile
RUN cd /sandbox/tsne.resero-labs.noopenmp; make clean all

ADD docker/cpu/Makefile.10XDev /sandbox/tsne.10XDev/Makefile
RUN cd /sandbox/tsne.10XDev; make clean all

ADD docker/cpu/Makefile.lvdmaaten.variants /sandbox/tsne.lvdmaaten/Makefile
RUN cd /sandbox/tsne.lvdmaaten; make clean all

ADD docker/cpu/main.cpp /sandbox/tsne.danielfrg/
ADD docker/cpu/Makefile.danielfrg /sandbox/tsne.danielfrg/Makefile
RUN cd /sandbox/tsne.danielfrg; cat main.cpp >>tsne.cpp; make clean all

RUN conda update -n base conda \
    && conda create -n py35 python=3.5 numpy cython --no-default-packages \
    && conda create -n py36 python=3.6 numpy cython --no-default-packages  \
    && conda create -n py37 python=3.7 numpy cython --no-default-packages \
    && conda create -n resero-labs python=3.6 numpy cython --no-default-packages \
    && conda create -n 10XDev python=3.6 numpy cython --no-default-packages \
    && conda create -n pypi python=3.6 numpy cython --no-default-packages \
    && conda create -n umap python=3.7 numpy scipy numba scikit-learn cython --no-default-packages

RUN mkdir perfutils
COPY perfutils/* ./perfutils/
ADD setup.py .
RUN ["/bin/bash", "-c", "source activate resero-labs; pip install tsne-mp ."]
RUN ["/bin/bash", "-c", "source activate 10XDev; pip install git+git://github.com/10XDev/tsne.git#egg=tsne ."]
RUN ["/bin/bash", "-c", "source activate pypi; pip install tsne ."]
RUN ["/bin/bash", "-c", "source activate umap; pip install umap-learn ."]

ADD docker/cpu/tsne-perf-test.py .
ADD docker/cpu/python-*-perf-test.py ./
ADD docker/cpu/gen-mnist-scatter.py .

# If you want to throw in a newly built wheel, do it here
#ADD "tsne_mp-0.1.9+5.gc45737d-cp36-cp36m-manylinux1_x86_64.whl" .
#RUN ["/bin/bash", "-c", "source activate py36; pip install /sandbox/tsne_mp-0.1.9+5.gc45737d-cp36-cp36m-manylinux1_x86_64.whl"]

ENV PYTHONUNBUFFERED=TRUE

ENTRYPOINT ["/sandbox/tsne-perf-test.py"]
CMD ["--help"]

