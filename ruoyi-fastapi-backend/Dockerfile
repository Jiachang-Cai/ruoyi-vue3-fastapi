# 使用官方 Python 镜像作为基础镜像
FROM python:3.13-slim

# 安装构建依赖和运行依赖
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    zlib1g-dev \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# 安装uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
# 拷贝应用代码
WORKDIR /app
COPY . .
# 安装依赖
RUN uv sync --frozen --no-cache
# 端口
EXPOSE 9099
# 启动应用
CMD [".venv/bin/python", "app.py"]

