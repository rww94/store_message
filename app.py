from flask import Flask
from flask import render_template
from flask import request
import os
import tkinter.messagebox
from tkinter import *
app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html',MARKER_DISPLACEMENT_num=2,MARKER_PRESSURE_num=1)

@app.route('/subfrom',methods=['POST'])
def subfrom():
	MARKER_DISPLACEMENT_num = int(request.form.get("MARKER_DISPLACEMENT_num"))
	MARKER_PRESSURE_num = int(request.form.get("MARKER_PRESSURE_num"))
	return render_template('index.html',MARKER_DISPLACEMENT_num=MARKER_DISPLACEMENT_num,MARKER_PRESSURE_num=MARKER_PRESSURE_num)

@app.route('/store',methods=['POST'])
def store():
	res = {}
	name = ['MODULE_CONTAINER','MODULE','METHOD','POSTPROCESSOR','SOLVER_TYPE','MATERIAL_TYPE','MAT_PARA','ELEMENT_TYPE','MESH_FILENAME',
	'MARKER_DISPLACEMENT','MARKER_PRESSURE','OUTPUT_FILENAME']
	for t in name:
		if t =='MAT_PARA' or  t =='MARKER_DISPLACEMENT' or t == 'MARKER_PRESSURE':
			res[t] = request.form.getlist(t)
		else:
			res[t] = request.form.get(t)
	outfile = res['OUTPUT_FILENAME']
	out_dir = os.path.dirname(outfile)
	if not os.path.exists(out_dir):
		os.makedirs(out_dir)
	f = open(outfile,'w')
	for k,v in res.items():
		if k == 'MAT_PARA' or k == 'MARKER_DISPLACEMENT' or k == 'MARKER_PRESSURE':
			f.write(k+" = (")
			for i in range(len(v)):
				if i!= len(v)-1:
					f.write(str(v[i])+",")
				else:
					f.write(str(v[i]))
			f.write(")\n")
		else:
			f.write(k+" = "+v+"\n")
	f.close()
	return render_template("info.html",res = res)


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=88)