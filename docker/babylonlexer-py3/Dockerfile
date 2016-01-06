FROM vertisfinance/base

MAINTAINER Richard Bann richard.bann@vertis.com

RUN apt-get update
# RUN DEBIAN_FRONTEND=noninteractive apt-get install -y make
# RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3-pip
# RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3-dev
#
# RUN pip3 install six==1.8.0
# RUN pip3 install Pygments==2.0.2
# RUN pip3 install Markdown==2.6.5
# RUN pip3 install pelican==3.6.3
# RUN pip3 install ghp-import==0.4.1
#
# RUN DEBIAN_FRONTEND=noninteractive apt-get install -y git
#
# RUN DEBIAN_FRONTEND=noninteractive apt-get install -y curl
# RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -
# RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs
# RUN npm install -g npm@latest

# RUN pip3 install git+https://github.com/rbann/pygments-lexer-babylon.git


FROM vertisfinance/base

MAINTAINER Richard Bann richard.bann@vertis.com

RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python3-pip

RUN pip3 install six==1.8.0
RUN pip3 install Pygments==2.0.2

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y nodejs
