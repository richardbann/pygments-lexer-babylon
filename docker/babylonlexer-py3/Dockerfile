FROM vertisfinance/base

MAINTAINER Richard Bann richard.bann@vertis.com

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3-pip

# RUN pip3 install six==1.8.0
# RUN pip3 install Pygments==2.0.2

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs
