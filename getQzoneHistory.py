from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "后端服务正常运行 ✅"

@app.route("/api/fetch", methods=["POST"])
def fetch_qzone():
    cookie = request.json.get("cookie")
    if not cookie:
        return jsonify({"error": "请提供 Cookie"}), 400

    # 这里模拟返回说说数据，真实版本请对接 g_tk 和请求接口
    return jsonify({
        "status": "success",
        "data": [
            "2010年6月：‘今天被某人虐待，心情特别复杂...’",
            "2011年12月：‘看到某人和他走得那么近，心里真不是滋味...’",
            "2012年3月：‘想她了...感觉回不去的过去。’"
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
