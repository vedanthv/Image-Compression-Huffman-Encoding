import os
import sys
import imgtotxt
import txttoimg
from timeit import default_timer as timer 
from flask import Flask,render_template,request,redirect,send_from_directory,make_response
app=Flask(__name__)
s=dict()

@app.route('/',methods=['GET','POST'])
def home():
	return render_template('home.html',u="Upload Image",c="COMPRESS!",ul='/compressed')


