FROM python:3.7

COPY requirements.txt /tmp/requirements.txt
RUN pip3 install --upgrade pip setuptools -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip3 install -r /tmp/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

WORKDIR /home/app

EXPOSE 3000