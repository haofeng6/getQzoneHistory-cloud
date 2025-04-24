from flask import Flask
from api.fetch import fetch_bp  # 原本就有的
from api.fetch_real import fetch_real_bp  # 👈 新加的

app = Flask(__name__)
app.register_blueprint(fetch_bp)
app.register_blueprint(fetch_real_bp)     # 👈 新加的

@app.route('/')
def index():
    return '服务已启动，准备接入QQ空间数据接口...'

import os
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
