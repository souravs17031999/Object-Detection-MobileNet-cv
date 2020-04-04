from flask import Flask, render_template, request
from inference import MobileNetSSD
from PIL import Image
import io
import numpy as np
import os

app = Flask(__name__, static_folder="images")

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
target = os.path.join(APP_ROOT, 'images/')
full_path = target + 'result.png'

@app.route('/',methods = ['GET','POST'])
def hello_world():
	if request.method == 'GET':
		return render_template('index.html',name = "sourav")
	if request.method == 'POST':
		print(request.files)
		if 'file' not in request.files:
			return render_template('error.html', message='FILE_LOAD_ERROR : File not loaded properly, please try again !')
		file = request.files['file']
		if file.filename == '':
		    return render_template('error.html', message='FILE_LOAD_ERROR : File not loaded properly, please try again !')
		image = file.read()
		npimg = np.fromstring(image, np.uint8)
		query = request.form['text'].lower()
		if not query:
			return render_template('error.html', message='EMPTY_STRING_ERROR : Query string is empty, please enter something !')
		print(file)
		for file in os.listdir(target):
			os.remove(target + file)

		prototxt = APP_ROOT + '/info.txt'
		model = APP_ROOT + '/model.caffemodel'
		m = MobileNetSSD(npimg, prototxt, model, 0.5, query, True)
		result_flag = m.main()
		if result_flag[0]:
			return render_template('result.html', image_name=result_flag[1])
		else:
			return render_template('error.html', message='NOT_FOUND_ERROR : Given Object not found in the Provided Image')

		
