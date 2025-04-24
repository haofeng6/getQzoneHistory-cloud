from flask import Blueprint, jsonify

fetch_real_bp = Blueprint('fetch_real', __name__)

@fetch_real_bp.route('/api/fetch_real', methods=['GET'])
def fetch_real_data():
    return jsonify({"message": "真实抓取接口已准备，后续将返回QQ空间数据..."})
