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

# defining default route
@app.route('/',methods = ['GET','POST'])
def hello_world():
	'''
	methods :
		GET : is used to request data from a specified resource.
		POST : is used to send data to a server to create/update a resource.
	'''
	# if we are just opening the webpage
	if request.method == 'GET':
		return render_template('index.html',name = "sourav")
	# if we are creating POST requests when filling the form for uploading the image
	if request.method == 'POST':
		# checking for file upload errors
		if 'file' not in request.files:
			return render_template('error.html', message='FILE_LOAD_ERROR : File not loaded properly, please try again !')
		file = request.files['file']
		# checking for file upload errors  , if empty means nothing selected
		if file.filename == '':
		    return render_template('error.html', message='FILE_LOAD_ERROR : File not loaded properly, please try again !')
		image = file.read()
		npimg = np.fromstring(image, np.uint8)
		# converting all queries from text box to lower case as we have defined all classes to be in lower case
		query = request.form['object'].lower()
		# check if nothing is provided in text box
		if not query:
			return render_template('error.html', message='EMPTY_STRING_ERROR : Query string is empty, please enter something !')
		# deleting older images to save space
		for file in os.listdir(target):
			os.remove(target + file)

		# this is the file path of info about model file for caffe
		prototxt = APP_ROOT + '/info.txt'
		# this is the caffemodel containing weights of the pre trained model
		model = APP_ROOT + '/model.caffemodel'
		m = MobileNetSSD(npimg, prototxt, model, 0.5, query, True)
		result_flag = m.main()  # this flag tells whether we detected given object in the image or not
		if result_flag[0]:
			return render_template('result.html', image_name=result_flag[1], detected_items=result_flag[2], len = len(result_flag[2]))
		else:
			return render_template('error.html', message='NOT_FOUND_ERROR : Given Object not found in the Provided Image')
