from flask import Flask
from flask_cors import CORS
from api.fetch_real import fetch_real_bp  # ✅ 只保留这一行

app = Flask(__name__)
CORS(app)

# ✅ 只注册 fetch_real 接口
app.register_blueprint(fetch_real_bp)

@app.route('/')
def index():
    return '服务已启动，准备接入QQ空间数据接口...'

# ✅ 以下是你真实抓取QQ说说的代码（不改）
import requests, re, time, json

def get_g_tk(skey):
    hash_value = 5381
    for c in skey:
        hash_value += (hash_value << 5) + ord(c)
    return hash_value & 0x7fffffff

def get_qzone_history_by_cookie(cookie: str) -> list:
    skey_match = re.search(r'skey=([^;]+)', cookie)
    uin_match = re.search(r'uin=o?(\d+)', cookie)
    if not skey_match or not uin_match:
        return [{"error": "cookie 中缺少 skey 或 uin"}]

    skey = skey_match.group(1)
    uin = uin_match.group(1)
    g_tk = get_g_tk(skey)
    headers = {"cookie": cookie, "user-agent": "Mozilla/5.0"}

    result = []
    pos = 0
    while True:
        url = f"https://h5.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?uin={uin}&inCharset=utf-8&outCharset=utf-8&hostUin={uin}&notice=0&sort=0&pos={pos}&num=20&format=jsonp&g_tk={g_tk}"
        res = requests.get(url, headers=headers)
        if res.status_code != 200: break

        try:
            json_text = re.search(r"_Callback\((.*)\);", res.text).group(1)
            data = json.loads(json_text)
        except Exception: break

        items = data.get("msglist")
        if not items: break

        for item in items:
            result.append({
                "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item.get("created_time", 0))),
                "content": item.get("content", "")
            })

        pos += 20
        if pos > 100: break

    return result if result else [{"notice": "未抓取到说说，可能 Cookie 失效"}]

# ✅ 一定要放在最底下！Render 云才能识别端口
import os
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)


