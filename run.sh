#!/bin/bash

container_name="streamlit_demo"

image_name="streamlit/streamlit_demo"

# 获取容器ID
container_id=$(docker ps -a | grep $container_name | awk '{print $1}')

# 如果容器存在，删除容器
if [ ! -z "$container_id" ]; then
    docker rm -f "$container_id"
fi

# 获取镜像ID
image_id=$(docker images | grep $image_name | awk '{print $3}')

# 如果镜像存在，删除镜像
if [ ! -z "$image_id" ]; then
    docker rmi "$image_id"
fi

# 构建新的Docker镜像
docker build -t $image_name .

# 运行新的Docker容器
docker run -d -p 10411:8501 -v .:/app --name $container_name $image_name