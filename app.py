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


@app.route('/uploaded', methods = ['GET', 'POST'])
def upload_file():
	if request.method=='POST':
		f = request.files['fileToUpload']
		imgname=f.filename
		f.save(imgname)
		imgtotxt.imgtotxt(imgname)
		return render_template('home.html',u="Image Uploaded!",l="Upload Text")

@app.route('/compressed',methods=['GET','POST'])
def compress():
	
	if request.method=='POST':
		os.system('gcc huffman.c')
		v=os.popen('./a.out')
		v=v.read().split('\n')
		v=v[:len(v)-1]
		keys,data=[int(i.split(': ')[0]) for i in v],[i.split(': ')[1] for i in v]
		global s
		s=dict(zip(keys,data))
		dtbw=[]
		with open('test1.txt') as f:
			for i in f:
				try:
					dtbw.append(s[int(i)])
				except:
					dtbw.append(i)
		dtbw=[str(i)+'\n' for i in dtbw]
		open('compressed.txt','w').writelines(dtbw)
		return decompress()

@app.route('/about',methods=['GET','POST'])
def about():
	return render_template('about.html')

