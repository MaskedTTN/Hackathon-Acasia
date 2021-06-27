from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    with open("data/testdata.json", "r")as data:
        datastore = json.load(data)
        Fmeetingname = datastore["accounts"][0]["meetings"]["Name"]
        Fmeetingstart = datastore["accounts"][0]["meetings"]["start"]
        Fmeetingend = datastore["accounts"][0]["meetings"]["end"]
        print(Fmeetingname)
        print(Fmeetingstart)
        print(Fmeetingend)
        data.close()
    return render_template("main.html", name=Fmeetingname, start=Fmeetingstart, end=Fmeetingend)

@app.route('/performance', methods=["GET", "POST"])
def performance():
    with open("data/testdata.json", "r")as data:
        datastore = json.load(data)
        Pattendance = datastore["accounts"][0]["performance"]["attendance"]
        Ppunctuality = datastore["accounts"][0]["performance"]["punctuality"]
        Poverall = datastore["accounts"][0]["performance"]["overall"]
        print(Pattendance)
        print(Ppunctuality)
        print(Poverall)
        data.close()
    return render_template("performance.html", attendance=Pattendance, punctuality=Ppunctuality, overall=Poverall)

@app.route('/shifts', methods=["GET", "POST"])
def shifts():
    with open("data/testdata.json", "r")as data:
        datastore = json.load(data)
        #put location changing
        Sstarting = datastore["accounts"][0]["shifts"]["location"]
        Sending = datastore["accounts"][0]["shifts"]["start"]
        Slocation = datastore["accounts"][0]["shifts"]["end"]
        print(Sstarting)
        print(Sending)
        print(Slocation)
        data.close()
    return render_template("shifts.html", starting=Sstarting, ending=Sending, location=Slocation)

@app.route('/status', methods=["GET", "POST"])
def status():
    with open("data/testdata.json", "r")as data:
        datastore = json.load(data)
        Sstatus = datastore["accounts"][0]["status"]
        print(Sstatus)
        data.close()
    return render_template('status.html', status=Sstatus)

@app.route('/changeDND', methods=["GET", "POST"])
def changeDND():
    with open("data/testdata.json", "r")as fp:
        tmpdata = json.load(fp)
        fp.close()
    tmpdata["accounts"][0]["status"] = "DND"
    with open("data/testdata.json", "w")as fp:
        fp.write(json.dumps(tmpdata))
    return redirect("/status")

@app.route('/changeOnline', methods=["GET", "POST"])
def changeOnline():
    with open("data/testdata.json", "r")as fp:
        tmpdata = json.load(fp)
        fp.close()
    tmpdata["accounts"][0]["status"] = "Online"
    with open("data/testdata.json", "w")as fp:
        fp.write(json.dumps(tmpdata))
    return redirect("/status")

@app.route('/changeBusy', methods=["GET", "POST"])
def changeBusy():
    with open("data/testdata.json", "r")as fp:
        tmpdata = json.load(fp)
        fp.close()
    tmpdata["accounts"][0]["status"] = "Busy"
    with open("data/testdata.json", "w")as fp:
        fp.write(json.dumps(tmpdata))
        fp.close()
    return redirect("/status")

@app.route('/passwords', methods=["GET", "POST"])
def passwords():
    with open("data/testdata.json") as fp:
        data = json.load(fp)
        Pusername = data["accounts"][0]["passwords"][0]["Username"]
        Ppassword = data["accounts"][0]["passwords"][0]["Password"]
        fp.close()
    print(Pusername)
    print(Ppassword)
    return render_template("passwords.html", username=Pusername, password=Ppassword)

if __name__ == "__main__":
    app.run(debug=True)
