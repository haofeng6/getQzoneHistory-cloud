from flask import Blueprint, jsonify

fetch_bp = Blueprint('fetch', __name__)

@fetch_bp.route('/api/fetch', methods=['GET'])
def fetch_data():
    return jsonify({
        "status": "success",
        "message": "这是 /api/fetch 接口返回的数据"
    })
