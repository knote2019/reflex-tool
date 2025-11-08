# NGINX 配置说明

## 配置概述

已配置 NGINX 作为反向代理：
- **NGINX 监听端口**: 3000
- **Reflex Frontend**: 5000
- **Reflex Backend**: 8000

## 架构

```
用户浏览器 (访问 :3000)
    ↓
NGINX (:3000)
    ↓
    ├── Frontend 请求 → Reflex Frontend (:5000)
    ├── WebSocket (_event) → Reflex Backend (:8000)
    └── API 请求 → Reflex Backend (:8000)
```

## 安装和启动

### 方法 1: 使用自动脚本（推荐）

```bash
sudo /root/reflex_tool/setup_nginx.sh
```

### 方法 2: 手动配置

```bash
# 安装 NGINX
sudo apt-get update
sudo apt-get install -y nginx

# 复制配置文件
sudo cp /root/reflex_tool/nginx.conf /etc/nginx/sites-available/reflex_tool

# 启用站点
sudo ln -sf /etc/nginx/sites-available/reflex_tool /etc/nginx/sites-enabled/reflex_tool

# 删除默认配置（可选）
sudo rm /etc/nginx/sites-enabled/default

# 测试配置
sudo nginx -t

# 重启 NGINX
sudo systemctl restart nginx
```

## 启动 Reflex 应用

在配置好 NGINX 后，启动 Reflex 应用：

```bash
cd /root/reflex_tool
reflex run --loglevel info
```

应用将在以下端口运行：
- Frontend: http://0.0.0.0:5000
- Backend: http://0.0.0.0:8000

通过 NGINX 访问：
- **http://localhost:3000** (或者 http://<你的IP>:3000)

## NGINX 配置文件说明

配置文件位置: `/root/reflex_tool/nginx.conf`

### 主要配置：

1. **WebSocket 支持** (`/_event`)
   - 长连接超时: 24小时
   - 支持 Reflex 实时更新

2. **后端 API 代理**
   - `/ping`, `/_upload`, `/_health` 等路由
   - 转发到 Backend (8000)

3. **前端代理**
   - 所有其他请求转发到 Frontend (5000)
   - 支持热重载

4. **静态资源缓存**
   - JS/CSS/图片等静态资源缓存 30 天

## 常用命令

```bash
# 检查 NGINX 状态
sudo systemctl status nginx

# 重启 NGINX
sudo systemctl restart nginx

# 重新加载配置（无需停机）
sudo systemctl reload nginx

# 停止 NGINX
sudo systemctl stop nginx

# 查看 NGINX 日志
sudo tail -f /var/log/nginx/access.log
sudo tail -f /var/log/nginx/error.log

# 测试配置文件语法
sudo nginx -t
```

## 故障排除

### 端口冲突

如果端口 3000 已被占用：

```bash
# 查看端口占用
sudo lsof -i :3000

# 或者
sudo netstat -tlnp | grep :3000
```

### NGINX 无法启动

```bash
# 查看错误日志
sudo journalctl -u nginx -n 50

# 或者
sudo tail -n 50 /var/log/nginx/error.log
```

### 修改配置后

每次修改 `/root/reflex_tool/nginx.conf` 后：

```bash
# 1. 更新到 NGINX 配置目录
sudo cp /root/reflex_tool/nginx.conf /etc/nginx/sites-available/reflex_tool

# 2. 测试配置
sudo nginx -t

# 3. 重新加载
sudo systemctl reload nginx
```

## 安全建议

对于生产环境，建议：

1. 启用 HTTPS
2. 添加速率限制
3. 配置防火墙规则
4. 使用域名而非 IP
5. 添加访问日志和监控

## 性能优化

配置文件已包含：
- 静态资源缓存
- 长连接支持
- 适当的超时设置

根据需要可以进一步调整这些参数。

