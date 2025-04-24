from flask import Flask
from flask_cors import CORS  # ✅ 新增
from api.fetch_real import fetch_real_bp
from api.fetch import fetch_bp

app = Flask(__name__)
CORS(app)  # ✅ 启用全局跨域支持

app.register_blueprint(fetch_bp)
app.register_blueprint(fetch_real_bp)

@app.route('/')
def index():
    return '服务已启动，准备接入QQ空间数据接口...'

import os
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
