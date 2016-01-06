FROM vertisfinance/base

MAINTAINER Richard Bann richard.bann@vertis.com

RUN apt-get update
# RUN DEBIAN_FRONTEND=noninteractive apt-get install -y make
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python-pip
# RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python-dev

RUN pip install six==1.8.0
RUN pip install Pygments==2.0.2

# RUN DEBIAN_FRONTEND=noninteractive apt-get install -y git

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs
# RUN npm install -g npm@latest

# RUN pip3 install git+https://github.com/rbann/pygments-lexer-babylon.git
