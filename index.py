from flask import Flask, render_template,request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    x ="資管二A 411146651 林映均的求職相關資訊<br>"
    x +="<a href=/about>個人簡介</a><br>"
    x +="<a href=/company>MIS相關工作介紹</a><br>"
    x +="<a href=/welcome>興趣何倫碼測驗結果</a><br>"
    x +="<a href=/job>求職自傳</a><br>"
    x +="<a href=/julia>求職履歷</a><br>"
    return x

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/company")
def company():
    return render_template("company.html")

@app.route("/welcome", methods=["GET", "POST"])
def welcome():
     user = request.values.get("nick")
     return render_template("welcome.html", name=user)

@app.route("/job")
def job():
    return render_template("job.html")

@app.route("/julia")
def julia():
    return render_template("julia.html")


# if __name__ == "__main__":
#     app.run()

