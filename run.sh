#!/bin/bash
echo "============================================"
echo "  Local AI Toolbox - 一键启动"
echo "============================================"
echo ""

echo "[1/2] 检查并安装依赖（首次运行需要几分钟）..."
pip3 install -r requirements.txt

echo ""
echo "[2/2] 启动工具箱..."
echo "启动后浏览器会自动打开 http://127.0.0.1:7860"
echo "按 Ctrl+C 停止服务。"
echo ""
python3 app.py
