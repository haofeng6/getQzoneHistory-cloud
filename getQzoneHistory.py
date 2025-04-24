from flask import Flask
from api.fetch import fetch_bp  # 引入刚才创建的接口模块

app = Flask(__name__)
app.register_blueprint(fetch_bp)  # 注册接口

@app.route('/')
def index():
    return '服务已启动，准备接入QQ空间数据接口...'

import os  # 👈 新增这行

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # 👈 读取 PORT 变量
    app.run(host='0.0.0.0', port=port)        # 👈 启动时绑定 0.0.0.0 和端口
