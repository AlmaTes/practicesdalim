from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def vysocina():
    if request.method=="POST":
        for i in ["username","username1","username2","username3"]:
            with open('uzeniny.txt', 'a') as f:
                f.write(str(request.form[i])+"\n")
                f.close()

    else:
        return render_template("test.html")


if __name__ == '__main__':
    app.run()