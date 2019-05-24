from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/store',methods=['POST'])
def store():
	res = {}
	name = ['MODULE_CONTAINER','MODULE','METHOD','POSTPROCESSOR','SOLVER_TYPE','MATERIAL_TYPE','ELEMENT_TYPE','MESH_FILENAME','OUTPUT_FILENAME']
	for t in name:
		res[t] = request.form.get(t)
	outfile = res['OUTPUT_FILENAME']
	f = open(outfile,'w')
	for k,v in res.items():
		f.write(k+" = "+v+"\n")
	f.close()
	return render_template("info.html",res = res)


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=88)