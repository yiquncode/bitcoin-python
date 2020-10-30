FROM centos:8
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
RUN yum install -y python3 python3-devel net-tools wget cronie vim gcc gcc-c++ autoconf

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --upgrade pip setuptools -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install -r /tmp/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

WORKDIR /home/app

EXPOSE 3000