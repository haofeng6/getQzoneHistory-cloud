from flask import Blueprint, request, jsonify

fetch_real_bp = Blueprint('fetch_real', __name__)

@fetch_real_bp.route('/api/fetch_real', methods=['POST'])
def fetch_real_data():
    data = request.get_json()
    cookie = data.get('cookie')

    if not cookie:
        return jsonify({"error": "未提供 cookie"}), 400

    # ✅ 模拟返回结构（下一步我们将替换为真实请求）
    fake_data = {
        "message": "成功接收到 Cookie",
        "cookie": cookie[:30] + "...",
        "posts": [
            {"time": "2020-01-01", "content": "这是你的一条说说"},
            {"time": "2020-02-02", "content": "又一条说说的内容"},
        ]
    }

    return jsonify(fake_data)
