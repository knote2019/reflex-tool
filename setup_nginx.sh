#!/bin/bash

# NGINX 配置脚本 for Reflex Tool

echo "Setting up NGINX for Reflex Tool..."

# 检查 NGINX 是否已安装
if ! command -v nginx &> /dev/null; then
    echo "NGINX not found. Installing..."
    apt-get update
    apt-get install -y nginx
fi

# 备份默认配置（如果存在）
if [ -f /etc/nginx/sites-enabled/default ]; then
    echo "Backing up default NGINX config..."
    mv /etc/nginx/sites-enabled/default /etc/nginx/sites-enabled/default.bak 2>/dev/null || true
fi

# 复制配置文件
echo "Copying NGINX configuration..."
cp /root/reflex_tool/nginx.conf /etc/nginx/sites-available/reflex_tool

# 创建符号链接
echo "Enabling site..."
ln -sf /etc/nginx/sites-available/reflex_tool /etc/nginx/sites-enabled/reflex_tool

# 测试配置
echo "Testing NGINX configuration..."
nginx -t

if [ $? -eq 0 ]; then
    echo "✓ NGINX configuration is valid"
    
    # 停止可能运行的 NGINX 进程
    echo "Stopping existing NGINX processes..."
    pkill nginx 2>/dev/null || true
    sleep 1
    
    # 启动 NGINX
    echo "Starting NGINX..."
    nginx
    
    if [ $? -eq 0 ]; then
        echo "✓ NGINX started successfully"
        echo ""
        echo "Configuration complete!"
        echo "NGINX is now listening on port 3000"
        echo "Proxying to Reflex frontend on port 5000"
        echo "Proxying backend API on port 8000"
        echo ""
        echo "Access your application at: http://localhost:3000"
        echo ""
        echo "To check NGINX status: ps aux | grep nginx"
        echo "To reload NGINX: nginx -s reload"
        echo "To stop NGINX: nginx -s stop"
    else
        echo "✗ Failed to start NGINX"
        exit 1
    fi
else
    echo "✗ NGINX configuration test failed"
    exit 1
fi

