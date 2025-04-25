import requests
import re
import time
import json

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

    headers = {
        "cookie": cookie,
        "user-agent": "Mozilla/5.0"
    }

    result = []
    pos = 0
    while True:
        url = f"https://h5.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?uin={uin}&inCharset=utf-8&outCharset=utf-8&hostUin={uin}&notice=0&sort=0&pos={pos}&num=20&format=jsonp&g_tk={g_tk}"
        res = requests.get(url, headers=headers)

        if res.status_code != 200:
            break

        try:
            json_text = re.search(r"_Callback\\((.*)\\);", res.text).group(1)
            data = json.loads(json_text)
        except Exception:
            break

        items = data.get("msglist")
        if not items:
            break

        for item in items:
            content = item.get("content", "")
            time_raw = item.get("created_time", "")
            time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time_raw))
            result.append({
                "time": time_str,
                "content": content
            })

        pos += 20
        if pos > 100:
            break

    return result if result else [{"notice": "未抓取到说说，可能 Cookie 失效"}]
