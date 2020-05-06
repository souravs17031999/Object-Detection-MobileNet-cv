from flask import Flask, render_template, request, jsonify
from werkzeug import secure_filename
from inference_object import MobileNetSSD
from PIL import Image
import io
import numpy as np
import os
import datetime
import boto3
import cv2
import uuid

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# modify the following part according to your configurations : ------------
client = boto3.client('s3', aws_access_key_id='############', aws_secret_access_key='############')
bucket_name = '###########'
# --------------------------------------------------------------------

# defining default route
@app.route('/',methods = ['GET'])
def hello_world():
	return render_template('index.html')

@app.route('/object',methods = ['GET','POST'])
def object_detection():
	'''
	methods :
		GET : is used to request data from a specified resource.
		POST : is used to send data to a server to create/update a resource.
	'''
	# if we are just opening the webpage
	if request.method == 'GET':
		return render_template('index_object.html')
	# if we are creating POST requests when filling the form for uploading the image
	if request.method == 'POST':
		# checking for file upload errors
		if 'file' not in request.files:
			return render_template('error_object.html', message='FILE_LOAD_ERROR : File not loaded properly, please try again !')
		content_type = request.mimetype
		file = request.files['file']
		filename = secure_filename(file.filename)
		# checking for file upload errors  , if empty means nothing selected
		if file.filename == '':
		    return render_template('error_object.html', message='FILE_LOAD_ERROR : File not loaded properly, please try again !')
		image = file.read()
		npimg = np.fromstring(image, np.uint8)
		# converting all queries from text box to lower case as we have defined all classes to be in lower case
		query = request.form['object'].lower()
		# check if nothing is provided in text box
		if not query:
			return render_template('error_object.html', message='EMPTY_STRING_ERROR : Query string is empty, please enter something !')
		# # deleting older images to save space
		# for file in os.listdir(target):
		# 	os.remove(target + file)

		# this is the file path of info about model file for caffe
		prototxt = APP_ROOT + '/info.txt'
		# this is the caffemodel containing weights of the pre trained model
		model = APP_ROOT + '/model.caffemodel'
		m = MobileNetSSD(npimg, prototxt, model, 0.5, query, True)
		result_flag = m.main()  # this flag tells whether we detected given object in the image or not

		random_generate = str(uuid.uuid4())
		full_path = random_generate + '.png'

		data_serial = cv2.imencode('.png', result_flag[1])[1].tostring()
		client.put_object(Body=data_serial,
                      Bucket=bucket_name,
                      Key=full_path,
                      ContentType=content_type)



		if result_flag[0]:
			target_url = full_path
			return render_template('result_object.html', bucket_name=bucket_name, image_name=target_url, detected_items=result_flag[2], len = len(result_flag[2]))
		else:
			return render_template('error_object.html', message='NOT_FOUND_ERROR : Given Object not found in the Provided Image')
