from app import app
from flask import render_template, request, redirect, flash
from flask_basicauth import BasicAuth
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import pandas as pd

gauth = GoogleAuth()
gauth.LoadCredentialsFile("mycreds.txt")
gauth.LocalWebserverAuth()
# gauth.SaveCredentialsFile("mycreds.txt")
drive = GoogleDrive(gauth)



#authentication
basic_auth = BasicAuth(app)


#routes
@app.route("/csv-template")
def csv_template():
    return render_template("admin/csv_template.html")

@app.route("/admin/dashboard")
@basic_auth.required
def dashboard():
    return render_template("admin/dashboard.html")

@app.route("/admin/request-report", methods = ["GET", "POST"])
@basic_auth.required
def request_report():

    if request.method== "POST":
        
        if request.files:

            file = request.files["csv"]
            client_csv = pd.read_csv(file)

            #save file to drive            
            client_csv.to_csv("hb.csv")
            uploaded = drive.CreateFile({'title': 'hb.csv'})
            uploaded.SetContentFile("hb.csv")
            uploaded.Upload()

            # flash("File Uploaded to Drive.")


            return redirect(request.url)

    return render_template("admin/request_report.html")

