FROM vertisfinance/base

MAINTAINER Richard Bann richard.bann@vertis.com

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python-pip
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs

RUN pip install pygments==2.1
RUN pip install pytest pytest-cov
