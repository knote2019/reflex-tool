#!/bin/bash
# Linux/Mac 一键部署脚本
# Reflex Docker 部署

set -e

echo "开始构建 Reflex Docker 镜像..."

# 1. 构建镜像
docker build -t reflex-tool:latest .

echo "✅ 镜像构建成功！"

# 2. 停止并删除旧容器（如果存在）
echo "检查并清理旧容器..."
docker rm -f reflex-tool 2>/dev/null || true

# 3. 运行新容器
echo "启动容器..."
docker run -d \
  --name reflex-tool \
  -p 3000:3000 \
  -p 8000:8000 \
  -v "$(pwd)/data:/app/data" \
  -v "$(pwd)/config:/app/config" \
  --restart unless-stopped \
  reflex-tool:latest

echo ""
echo "✅ 部署成功！"
echo "应用正在运行，访问地址：http://localhost:6000"
echo ""
echo "查看日志：docker logs -f reflex-tool"
echo "停止容器：docker stop reflex-tool"

