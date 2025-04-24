from flask import Blueprint, jsonify

fetch_bp = Blueprint('fetch', __name__)

@fetch_bp.route('/api/fetch', methods=['GET'])
def fetch():
    return jsonify({"message": "接口已启动，准备接入 QQ空间数据..."})
