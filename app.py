from flask import Flask,render_template,redirect,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///mydet.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

dbn = SQLAlchemy(app)

class Mydet(dbn.Model):
    emid = dbn.Column(dbn.String(100),primary_key=True)
    pasw = dbn.Column(dbn.String(100),nullable=False)
    log_time = dbn.Column(dbn.DateTime, default=datetime.utcnow)
    def __repr__(self) -> str:
        return f"{self.pasw}, {self.emid}"

@app.route("/mypage")
def my_page():
    #alldet = Mydet.query.filterby(emid=emid).first()
    return render_template("mypage.html",alldet=alldet)

@app.route("/",methods=["GET","POST"])
def home_page():
    if request.method=="POST":
        global emids
        emids=request.form["emid"]
        pasw=request.form["pasw"]
        det = Mydet(emid=emids,pasw=pasw)
        dbn.session.add(det)
        dbn.session.commit()
        #alldet = Mydet.query.filter_by(emid=emids).first()
        return render_template("mypage.html")
    return render_template("home.html")

@app.route("/mypag")
def my_pag():
    return render_template("mypage.html")

@app.route("/profile")
def my_prof():
    alldet = Mydet.query.filter_by(emid=emids).first()
    #print(alldet.emid)
    return render_template("mydet.html",alldet=alldet)

@app.route("/del")
def del_prof():
    print(emids)
    det = Mydet.query.filter_by(emid=emids).first()
    dbn.session.delete(det)
    dbn.session.commit()
    return render_template("logoff.html")
'''
if __name__ == "__main__":
    app.run(debug=True,port=9000)
'''