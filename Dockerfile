FROM centos:7

# install r
RUN yum install epel-release -y
RUN yum install R readline-devel python python-devel python-pip -y

# install app
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r /app/requirements.txt

# install r packages
RUN -p mkdir /r/repo
ADD ./r-repo /r/repo
RUN -p mkdir /r/lib
RUN R_LIBS=/r/lib R -e "install.packages('AnomalyDetection', depencencies=TRUE, repos='file://app/r/repo')"


