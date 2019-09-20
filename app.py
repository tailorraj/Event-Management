from flask import Flask, flash, redirect, render_template,request, url_for, session,jsonify
import Dbfun
import os
import datetime
import email_attach
import qr_code

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/admin')
def admin_template():
    return render_template('admin.html')

@app.route('/publish-event',methods=['POST'])
def register_event():
    title=request.form['title']
    description=request.form['description']
    catagory=request.form['category']
    tags=request.form['tags']
    result = Dbfun.register_event(title,description,catagory,tags)
    print(result)
    if result =="done":
        return render_template('admin.html',msg2="*Event Registered")
    else:
        return render_template('admin.html',msg1="*Event not Registered")

@app.route('/event-list')
def get_event():
    return render_template('event_list.html',data = Dbfun.get_event())


@app.route('/signup')
def signup():
    return render_template('signup.html')



@app.route('/process',methods=['POST'])
def get_d():
    mail=request.form['email']
    fname=request.form['fname']
    lname=request.form['lname']
    city=request.form['city']
    num=request.form['num']
    image=request.form['pic']
    if(Dbfun.check_exist(mail)):
        return render_template('signup.html',msg1="*Email You Entered is already Registered")
    else:
        Dbfun.register(fname,lname,city,num,image,mail)
        Dbfun.generate_qr(fname+"&"+num)
        email_attach.send_mail(mail)
        
        return render_template('home.html',msg2="You are successfully Registered")  


@app.route('/check_entry')
def get_existing_data():
    check_entry=qr_code.qr_code_reader()
    if check_entry:
        return render_template('home.html',msg2="Entry Exist") 
    else:
        return render_template('home.html',msg2="No entry") 


if __name__=='__main__':
    app.run(debug=True)