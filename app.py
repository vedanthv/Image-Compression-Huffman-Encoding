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

def decompress():
	start=timer()
	if request.method=='POST':
		global s
		d=[]
		with open('compressed.txt','r') as f:
			l=[]
			f=f.read().split('\n')
			f=f[:len(f)-1]
			l,size=[i for i in f[:len(f)-1]],f[-1:][0]
			for i in l:
				for key,value in s.items():
					if value==i:
						d.append(key)
			d=[str(i)+'\n' for i in d]
			d.append(str(size))
			open('decompressed.txt','w').writelines(d)
		with open('decompressed.txt','r') as f:
			l=list(f.read().split())
			l1=[]
			l2=[]
			l3=[]
			l1=[int(l[i]) for i in range(0,len(l)-2,3)]
			l2=[int(l[i]) for i in range(1,len(l)-2,3)]
			l3=[int(l[i]) for i in range(2,len(l)-2,3)]
			res=list(zip(l1,l2,l3))
			with open('final.txt','w') as file:
				for i in res:
					file.write(str(i)+'\n')
				file.write(l[len(l)-2])
				file.write(l[len(l)-1])
    
		txttoimg.txttoimg('final.txt')
		response=make_response(send_from_directory('/D:/University/Image-Compression-Huffman Encoding','pic.jpeg'))
		response.headers["Content-Disposition"]="attachment; filename=compressed_image.jpg"
		end=timer()
		duration=end-start
		print("Duration in seconds:",duration)
		return response



@app.route('/about',methods=['GET','POST'])
def about():
	return render_template('about.html')

