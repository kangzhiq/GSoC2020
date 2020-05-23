Bootstrap:docker  
From:ubuntu:latest  

%labels
MAINTAINER Zhiqi


%environment
RAWR_BASE=/code
export RAWR_BASE

%runscript
echo "This is the latest Singularity"
exec /bin/bash /code/rawr.sh "$@"  

%post  
echo "This section happens once after bootstrap to build the image."  
mkdir -p /code  
echo "RoooAAAAR" >> /code/rawr.sh
chmod u+x /code/rawr.sh 

apt-get update
apt-get install -y cmake \
				locales \
				language-pack-en \
				git \
				python3.6 \
				pkg-config 