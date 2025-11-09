# Reflex Docker 部署配置
# 使用 Python 3.11 作为基础镜像
FROM python:3.11-slim

# 设置工作目录
WORKDIR /app

# 安装系统依赖
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# 安装 Node.js (Reflex 需要 Node.js 来构建前端)
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# 复制依赖文件
COPY requirements.txt .

# 安装 Python 依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制项目文件
COPY . .

# 暴露端口 (前端和后端)
EXPOSE 6000 7000

# 初始化 Reflex 应用（安装前端依赖）
RUN reflex init

# 启动命令 - 生产模式
CMD ["reflex", "run", "--env", "prod"]

