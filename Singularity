BootStrap:docker
From:ubuntu:18.04

%labels
AUTHOR Zhiqi
BASED_ON https://github.com/rianders/docker-openpose/blob/master/Dockerfile

%environment
        export LANGUAGE=en_US.UTF-8
        export LANG=en_US.UTF-8
        export LC_ALL=en_US.UTF-8

%post
apt-get update && apt-get install -y --no-install-recommends software-properties-common wget
add-apt-repository universe
apt-get update && apt-get install -y --no-install-recommends \
  ca-certificates curl git nano less \
  build-essential cmake pkg-config libopencv-dev caffe-cpu libgoogle-glog-dev libcaffe-cpu-dev \
  libboost-dev libprotobuf-dev gpg-agent locales language-pack-en
locale-gen en_US.UTF-8 && dpkg-reconfigure locales
wget https://apt.repos.intel.com/intel-gpg-keys/GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
apt-key add GPG-PUB-KEY-INTEL-SW-PRODUCTS-2019.PUB
wget https://apt.repos.intel.com/setup/intelproducts.list -O /etc/apt/sources.list.d/intelproducts.list
apt-get update && apt-get install -y --no-install-recommends intel-mkl-64bit-2018.2

# option caffe-cuda
# http://caffe.berkeleyvision.org/install_apt.html
# In case we need to turn off ssl verify
# RUN  git config --global http.sslVerify false

#Default mount point used in Shef Uni's ShARC cluster
mkdir /scratch /data /shared /fastdata

#Nvidia driver file mount paths
mkdir /nvlib /nvbin

#Add nvidia driver paths to the environment variables
echo "\n #Nvidia driver paths \n" >> /environment
echo 'export PATH="/nvbin:$PATH"' >> /environment
echo 'export LD_LIBRARY_PATH="/nvlib:$LD_LIBRARY_PATH"' >> /environment

#Add CUDA paths
echo "\n #Cuda paths \n" >> /environment
echo 'export CPATH="/usr/local/cuda/include:$CPATH"' >> /environment
echo 'export PATH="/usr/local/cuda/bin:$PATH"' >> /environment
echo 'export LD_LIBRARY_PATH="/usr/local/cuda/lib64:$LD_LIBRARY_PATH"' >> /environment
echo 'export CUDA_HOME="/usr/local/cuda"' >> /environment

mkdir /localdata
cd /localdata
mkdir src
cd src
git clone https://github.com/CMU-Perceptual-Computing-Lab/openpose.git
cd openpose
mkdir build
cd build
export MKLVARS_ARCHITECTURE=intel64
. /opt/intel/mkl/bin/mklvars.sh
# Apparently not all shells allow parameters with source.
#. /opt/intel/mkl/bin/mklvars.sh intel64

cmake -DGPU_MODE=CPU_ONLY -DBUILD_CAFFE=OFF -DCaffe_INCLUDE_DIRS=/usr/include/caffe/ -DCaffe_LIBS=/usr/lib/x86_64-linux-gnu/libcaffe.so ..
make
make install

