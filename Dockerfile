FROM python:3.10

# 复制项目代码
WORKDIR /app
COPY . /app

# 安装依赖
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -U streamlit

# 启动服务
CMD ["streamlit", "run","demo.py"]