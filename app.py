from flask import Flask, render_template, request ,session,redirect
from pymongo import MongoClient
from datetime import datetime

usr_name = "Sourya"
usr_password = "Sourya.123"

client = MongoClient('mongodb+srv://SouryaPoudel:Sourya.123@ankuramrobotbackend.jydvwk1.mongodb.net/')

app = Flask(__name__)
app.secret_key='sourya123'

@app.route("/",methods=['GET','POST'])
def dashboard():
    if ('user' in session and session['user']== usr_name):
        return render_template('dashboard.html')
    if request.method=="POST":
        username = request.form.get("uname")
        password = request.form.get("password")
        if(username==usr_name and password==usr_password):
            session['user']=username
            return render_template('dashboard.html')
        else:
            return render_template('login.html', error="Invalid username or password")
    return render_template('login.html')

@app.route("/notice",methods=['GET','POST'])
def notice():
    if('user'in session and session['user']==usr_name):
        return render_template('notice.html')
    else:
        return redirect("/")
    return redirect('/')

@app.route("/noticesuccess",methods=['GET','POST'])
def noticesuccess():
    if('user'in session and session['user']==usr_name):
        db = client["notice"]
        collection = db["notice"]
    notice_url = request.form.get("notice_url")
    user_data = {
        "notice_url": notice_url,
        "date": datetime.now(),
        "user": "root"  # <-- Add this field explicitly here
    }
    result = collection.update_one(
        {"user": "root"},        # match document for user 'root'
        {"$set": user_data},     
        upsert=True
    )

    return redirect('/success')

@app.route("/slide",methods=['GET','POST'])
def slide():
    if('user'in session and session['user']==usr_name):
        return render_template('slide.html')
    else:
        return redirect("/")
    return redirect('/')

@app.route("/slidesuccess",methods=['GET','POST'])
def slidesuccess():
    if('user'in session and session['user']==usr_name):
        db = client["slide"]
        collection = db["slide"]
        slide_url = request.form.get("slide_url")
        user_data = {
    "slide_url": slide_url,
    "date": datetime.now(),
    "user": "root"
}
        result = collection.update_one(
        {"user": "root"},   # Query to find the document
        {"$set": user_data},         # Update the document with new data
        upsert=True                  # Insert if it doesn't exist
    )
        return redirect('/success')

@app.route("/foodmenu",methods=['GET','POST'])
def foodmenu():
    if('user'in session and session['user']==usr_name):
        return render_template('foodmenu.html')
    else:
        return redirect("/")
    return redirect('/')

@app.route("/foodmenusuccess",methods=['GET','POST'])
def foodmenusuccess():
    if('user'in session and session['user']==usr_name):
        db = client["foodmenu"]
        collection = db["foodmenu"]
        slide_url = request.form.get("foodmenu_url")
        user_data = {
    "foodmenu_url": slide_url,
    "date": datetime.now(),
    "user": "root"
}
        result = collection.update_one(
        {"user": "root"},   # Query to find the document
        {"$set": user_data},         # Update the document with new data
        upsert=True                  # Insert if it doesn't exist
    )
        return redirect('/success')
    
@app.route("/success",methods=['GET','POST'])
def success():
    if('user'in session and session['user']==usr_name):
        return render_template('success.html')
    return redirect('/')


import threading
import time
import webbrowser

def open_browser():
    time.sleep(1)  # Wait a moment for the server to start
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Thread(target=open_browser).start()
    app.run()
