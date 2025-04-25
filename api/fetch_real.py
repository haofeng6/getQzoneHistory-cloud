from flask import Blueprint, request, jsonify
from utils.qzone import get_qzone_history_by_cookie  # ✅ 从正确的模块引入

fetch_real_bp = Blueprint('fetch_real', __name__)

@fetch_real_bp.route('/api/fetch_real', methods=['POST'])
def fetch_real_data():
    data = request.get_json()
    cookie = data.get('cookie')

    if not cookie:
        return jsonify({"error": "未提供 cookie"}), 400

    try:
        posts = get_qzone_history_by_cookie(cookie)
        return jsonify({
            "message": "抓取成功",
            "cookie": cookie[:30] + "...",
            "posts": posts
        })
    except Exception as e:
        return jsonify({
            "error": "抓取失败",
            "detail": str(e)
        }), 500
