
const { exec } = require("child_process");
const fs = require("fs");

module.exports = async (req, res) => {
  if (req.method !== "POST") {
    return res.status(405).json({ status: "error", message: "仅支持 POST 请求" });
  }

  const { cookie } = req.body;
  if (!cookie || !cookie.includes("p_skey") || !cookie.includes("uin")) {
    return res.status(400).json({ status: "error", message: "无效的 Cookie" });
  }

  const cookieFile = "/tmp/user_cookie.txt";
  const outputFile = "/tmp/result.json";

  fs.writeFileSync(cookieFile, cookie);

  exec(`python3 getQzoneHistory.py --cookie "${cookie}" --output ${outputFile}`, (err, stdout, stderr) => {
    if (err) {
      return res.status(500).json({ status: "error", message: "抓取失败", error: stderr });
    }

    try {
      const data = JSON.parse(fs.readFileSync(outputFile, "utf8"));
      res.status(200).json({ status: "ok", data });
    } catch (e) {
      res.status(500).json({ status: "error", message: "结果解析失败" });
    }
  });
};
