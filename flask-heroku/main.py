from flask import Flask
app = Flask(__name__) # __name__ 代表目前執行的模組

@app.route("/") #涵式的裝飾(Decorator) 以涵式為基礎 提供附加的功能
def home():
    return "Hello Flask   Go Go PowerRanger"

@app.route("/test") #代表要處理的網路路徑 /後面為路徑
def test():
    return "Let,s go"

if __name__ == "__main__": #如果以主程式執行
    app.run() #立刻啟動伺服器