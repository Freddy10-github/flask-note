---
tags: Flask
---
從 Hello World 開始學習 Flak
===
## 安裝 Flask
`pip install Flask`
## 建立程式碼
新增檔案 `main.py`，且貼上下面程式：

```python=
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello,World!'
```

`app = Flask(__name__)`
__name__ 這邊是用來定位目前載入資料夾的位置，用來判別 template__folder 或 static_folder 資料夾位置。

`@app.route('/')`
讓 Flask 監聽此 URL，並 return 返回結果。

## 運行 Flask 的方式
在 command line 輸入 Flask 的內建指令
```
export FLASK_APP=main.py
export FLASK_ENV=development
flask run
```
flask 也可以增加設定
```
flask run --reload --debugger --host 0.0.0.0 --port 80
```
* reload：修改 py 檔後，Flask server 會自動 reload。
* debugger：如果有錯誤，會在頁面上顯示是哪一行錯誤。
* host：可以指定允許訪問的主機IP，0.0.0.0 為所有主機的意思。
* port：自訂網路埠號的參數。

如果像我一樣是在 Windows 上使用 VScode 的話，建議把預設 Terminal 改成 Git bash 。

成功之後打開 http://127.0.0.1:5000/ 即可看到結果。

## Reference
[【Hello word】實作一個簡單的 Flask 入門](https://www.maxlist.xyz/2020/04/30/flask-helloworld/)
[[VSCode] 將Visual Studio Code的終端機改為bash](https://dotblogs.com.tw/tom5707/2017/03/02/165726)

https://hackmd.io/@shaoeChen/HJkOuSagf?type=view
Jinja template