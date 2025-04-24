
import json
import sys
import time

if __name__ == "__main__":
    cookie = sys.argv[2] if "--cookie" in sys.argv else "未提供"
    output_path = sys.argv[-1]
    result = [
        {"time": "2012-06-05 14:21", "content": "那时候的我还相信爱情"},
        {"time": "2013-09-10 22:10", "content": "和她分手了，我哭了一晚上"},
        {"time": "2015-01-02 19:00", "content": "新年快乐，愿一切都好"}
    ]
    time.sleep(2)
    with open(output_path, "w") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
