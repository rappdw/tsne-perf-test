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
RUN wget -q https://s3-us-west-2.amazonaws.com/resero2/datasets/tsne-perf-test/data.2500.mnist.dat \
    && wget -q https://s3-us-west-2.amazonaws.com/resero2/datasets/tsne-perf-test/data.full.mnist.dat \
    && wget -q https://s3-us-west-2.amazonaws.com/resero2/datasets/tsne-perf-test/data.iris.dat

# get and extract rappdw version
RUN wget -q -O rappdw.zip https://github.com/rappdw/tsne/archive/v0.1.9.zip \
    && unzip -q rappdw.zip tsne-0.1.9/tsne/bh_sne_src/* -d tsne.rappdw \
    && mv tsne.rappdw/tsne-0.1.9/tsne/bh_sne_src/* tsne.rappdw \
    && rm -rf tsne.rappdw/tsne-0.1.9 \
    && rm rappdw.zip \
    && cp -r tsne.rappdw tsne.rappdw.noopenmp # create a non openmp version

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

ADD Makefile.rappdw.openmp /sandbox/tsne.rappdw/Makefile
RUN cd /sandbox/tsne.rappdw; make clean all

ADD Makefile.rappdw.noopenmp /sandbox/tsne.rappdw.noopenmp/Makefile
RUN cd /sandbox/tsne.rappdw.noopenmp; make clean all

ADD Makefile.10XDev /sandbox/tsne.10XDev/Makefile
RUN cd /sandbox/tsne.10XDev; make clean all

ADD Makefile.lvdmaaten.variants /sandbox/tsne.lvdmaaten/Makefile
RUN cd /sandbox/tsne.lvdmaaten; make clean all

ADD main.cpp /sandbox/tsne.danielfrg/
ADD Makefile.danielfrg /sandbox/tsne.danielfrg/Makefile
RUN cd /sandbox/tsne.danielfrg; cat main.cpp >>tsne.cpp; make clean all

RUN conda update -n base conda \
    && conda create -n py35 python=3.5 numpy cython --no-default-packages \
    && conda create -n py36 python=3.6 numpy cython --no-default-packages  \
    && conda create -n py37 python=3.7 numpy cython --no-default-packages \
    && conda create -n rappdw python=3.6 numpy cython --no-default-packages \
    && conda create -n 10XDev python=3.6 numpy cython --no-default-packages \
    && conda create -n pypi python=3.6 numpy cython --no-default-packages

RUN ["/bin/bash", "-c", "source activate rappdw; pip install git+git://github.com/rappdw/tsne.git@b0a6bb6d0f4d5636b023acfe3ed39c9294884656#egg=tsne-mp"]
RUN ["/bin/bash", "-c", "source activate 10XDev; pip install git+git://github.com/10XDev/tsne.git#egg=tsne"]
RUN ["/bin/bash", "-c", "source activate pypi; pip install tsne"]

ADD tsne-perf-test.py .
ADD python-tsne-perf-test.py .

ENTRYPOINT ["/sandbox/tsne-perf-test.py"]
CMD ["--help"]

