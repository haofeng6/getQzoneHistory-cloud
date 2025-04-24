from flask import Flask
from api.fetch import fetch_bp  # 引入刚才创建的接口模块

app = Flask(__name__)
app.register_blueprint(fetch_bp)  # 注册接口

@app.route('/')
def index():
    return '服务已启动，准备接入QQ空间数据接口...'

if __name__ == '__main__':
    app.run()
