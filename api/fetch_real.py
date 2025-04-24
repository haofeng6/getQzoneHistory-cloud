from flask import Blueprint, request, jsonify
import requests

fetch_real_bp = Blueprint('fetch_real', __name__)

@fetch_real_bp.route('/api/fetch_real', methods=['POST'])
def fetch_real_data():
    cookie = request.json.get('cookie')
    if not cookie:
        return jsonify({"error": "请提供有效的 Cookie 参数"}), 400

    # 使用 QQ 空间 JSONP 接口，模拟请求获取说说列表
    headers = {
        "Cookie": cookie,
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(
            "https://h5.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?uin=YOUR_UIN&format=json&num=10",
            headers=headers
        )
        return jsonify({
            "message": "抓取成功（示例）",
            "raw_response": response.text
        })
    except Exception as e:
        return jsonify({"error": f"请求出错: {str(e)}"})
