# WEB - Yet Another Login Page
## 原始碼

```
from flask import Flask, request, make_response, redirect, session, render_template, send_file
import os
import json

app = Flask(__name__)
app.secret_key = os.urandom(32)

FLAG = os.environ.get('FLAG', 'AIS3{TEST_FLAG}')
users_db = {
    'guest': 'guest',
    'admin': os.environ.get('PASSWORD', 'S3CR3T_P455W0RD')
}


@app.route("/")
def index():
    def valid_user(user):
        print(user)
        return users_db.get(user['username']) == user['password']

    if 'user_data' not in session:
        return render_template("login.html", message="Login Please :D")

    user = json.loads(session['user_data'])
    if valid_user(user):
        if user['showflag'] == True and user['username'] != 'guest':
            return FLAG
        else:
            return render_template("welcome.html", username=user['username'])

    return render_template("login.html", message="Verify Failed :(")


@app.route("/login", methods=['POST'])
def login():
    data = '{"showflag": false, "username": "%s", "password": "%s"}' % (
        request.form["username"], request.form['password']
    )
    session['user_data'] = data
    return redirect("/")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/sauce")
def sauce():
    return send_file(__file__, mimetype="text/plain")


if __name__ == '__main__':
    app.run(threaded=True, debug=True)
```

## 題目解析
可以知道這題的運作機制就是把輸入的 username 和 password 用 format string 填成 json 格式，之後判斷 users_db.get(user['username']) == user['password'] 和 user['showflag'] == true 是否成立

## 漏洞
由於是用 format string 變成 json 字串存進 session，之後才用 json.loads 轉回來，所以只要輸入的 username 或 password 符合 json 格式就好。

如果 username 填入 `", "showflag": true`，整個 json 就變成 `'{"showflag": false, "username": "", "showflag": true, "password": ""}'`，這樣就成功繞過 showflag 要是 true 的驗證

再來要讓 users_db.get(user['username']) == user['password']。
首先可以試出來 python 的 dict 的 get()，如果 key 是不存在，就會回傳 None，也就是 users_db.get(\<not exist\>) == None。
然後 user['password'] 要是 None 很簡單，就把 json 的字串那邊 password 欄位填入 none 就好

## exploit
* username: `haha`
* password: `", "password": null, "showflag": true, "username": "haha`

* flag: `AIS3{/r/badUIbattles?!?!}`
