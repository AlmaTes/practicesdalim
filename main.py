from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("neco napisu")
    return "<p>Hello, World!</p>"

@app.route("/randomendpoint")
def sadfasdfsaparek():
    return str(8*4*1000)

@app.route("/klacek/<karek>")
def parek(karek):
    return karek

@app.route("/polican",methods=["GET","POST"])
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