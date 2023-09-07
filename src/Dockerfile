# 设置基础镜像
FROM python:3.8

# 设置工作目录
WORKDIR /app

# 将当前目录下的文件复制到容器的工作目录中
COPY . .

# 安装依赖
RUN pip install -r requirements.txt

# 运行 cliff.py
CMD python cliffscan.py
