from flask import Flask
from flask_cors import CORS  # ✅ 跨域支持
from api.fetch_real import fetch_real_bp
from api.fetch import fetch_bp

app = Flask(__name__)
CORS(app)  # ✅ 启用跨域支持

# 注册路由蓝图
app.register_blueprint(fetch_bp)
app.register_blueprint(fetch_real_bp)

@app.route('/')
def index():
    return '服务已启动，准备接入QQ空间数据接口...'

import os
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

# ✅ 模拟真实抓取的函数（后期可替换为正式请求逻辑）
def get_qzone_history_by_cookie(cookie: str) -> list:
    """
    模拟从 QQ 空间抓取历史说说数据
    实际抓取逻辑后面可以替换，这里是返回演示数据结构
    """
    return [
        {"time": "2020-01-01", "content": "这是你真实的说说"},
        {"time": "2020-02-02", "content": "这是另一条历史动态"}
    ]
