# Object-Detection-MobileNet-cv

# Project Objective: 
Using a machine learning toolkit of your choice, create a tool which identifies objects in the image, then returns positions in pixels corresponding to bounding boxes of a user-selected class of object in the image.    
So, we are going to draw the bounding boxes of the defined labels with detected objects and also return their coordinates.    
This type of system can be very useful in such possible scenarios and can be integrated into the current tech stack :    

* Intrusion detection / Anti-theft surveillance systems   
* Maintaining safe distance between people during the pandemic times (COVID-19)
* Detecting face masks on people     
* Assiting traffic management tasks etc..    


# Approach :   
* Pre-trained ```MobileNet + SSD``` run from command line (terminal).
* Pre-trained ```MobileNet + SSD``` with ```Flask``` server.     

> Brief introduction       
![conv1](/img/conv1.png)      
* MobileNet uses Depthwise Separable Convolution which consists of two steps - Depthwise convolution and then Pointwise convolution.   
* Depthwise convolution channel wise spatial convolution.   
* Pointwise convolution uses Network-In-Network architechture (NiN) which is bsically doing 1 x 1 convolutions along with other conv layers. This helps in reducing parameters to a large extent.     
   

>Final architechture 
![final1](/img/overview.JPG)
![final2](/img/final2.JPG)


* Object detection in the browser using ```tensorflow.js``` [TODO - Currently in progress]  


### Real time Flask server hosted :      
* Log on to following URL hosted on pythonanywhere.com using flask server :    

### [LIVE WEBSITE](https://souravsdlboy.pythonanywhere.com/object)    

# Getting started :     
### FLASK solution : 
* Run the cmd (terminal).     
* Download the project files using following command in the directory from where you need to run the script :       
```  
git clone https://github.com/souravs17031999/Object-Detection-MobileNet-cv    
```      
* Move to the project main directory where the project is downloaded.
* Move to directory ```object_detect_flask```.  
* Now run following :     
(for windows)     
> set FLASK_APP=object.py      
> set FLASK_ENV=development (useful for debugging while developement)     
> python -m flask run          

(for other termials)          

> $ export FLASK_APP=object.py   
> $ FLASK_ENV=development (useful for debugging while developement)     
> $ flask run       

[Other troubleshooting issues related to flask server](https://flask.palletsprojects.com/en/1.1.x/quickstart/#what-to-do-if-the-server-does-not-start)    

* Now the local server should start, log on to : [local url port] shown on terminal.     
(Most probably it will be http://127.0.0.1:5000/ , or maybe any other default port)   

### USING AMAZON WEB SERVICES S3 :      
* This solution is for scenario if you are considering to Scale the Webapp in terms of storage capacity as PythonAnywhere.com doesn't have scalability anywhere near as we have on AWS S3 but there is a workaround which can be helpful (similar to script automation trying to remove the files on the disk and saving space on a daily basis, weekly basis based on the traffic on your website).       

* Now, If you want to configure AWS S3 for your Use , [check this repo](https://github.com/souravs17031999/aws-s3-python) by me which gives detailed explanation for the same.    
* After getting credentials, put your credentials in the script named ```flask_app.py``` in the dir named ```object_detect_s3```.   
* The only change is to be made on the two lines 18 and 19:      

> client = boto3.client('s3', aws_access_key_id='############', aws_secret_access_key='############')     
> bucket_name = '###########'       

* Let's now run the project locally on your system :        
* Run the cmd (terminal).     
* Download the project files using following command in the directory from where you need to run the script :       
```  
git clone https://github.com/souravs17031999/Object-Detection-MobileNet-cv    
```      
* Move to the project main directory where the project is downloaded.   
* Move to directory ```object_detect_s3```.    
* Now run following :     
(for windows)     
> set FLASK_APP=flask_app.py  
> set FLASK_ENV=development (useful for debugging while developement)       
> python -m flask run       

(for other termials)          

> $ export FLASK_APP=object.py  
> $ FLASK_ENV=development (useful for debugging while developement)     
> $ flask run       

[Other troubleshooting issues related to flask server](https://flask.palletsprojects.com/en/1.1.x/quickstart/#what-to-do-if-the-server-does-not-start)        

* Now the local server should start, log on to : [local url port] shown on terminal.      
(Most probably it will be http://127.0.0.1:5000/ , or maybe any other default port)    



### CMD (terminal) solution :    
* We need to install latest version of Opencv.     
[Download here](https://pypi.org/project/opencv-python/)   
* Run the cmd (terminal).    

* Download the project files using following command in the directory from where you need to run the script :   
```
git clone https://github.com/souravs17031999/Object-Detection-MobileNet-cv
```     
* Change directory to ```object_detect_cmd```.    
* Run the command using the following parameters as shown : 
```
python object_detection.py <image> <prototxt> <model> <confidence> <query>
``` 
 
positional arguments:   
| arguments  | details |
| ------------- | ------------- |
| image | Image path |  
| prototxt | info file path about model |
| model | model file of caffemodel type path |
| confidence | threshold confidence % (0.2, 0.3, ...)  |
| query | Query string to search for |     

optional arguments:         
  -v  :  debug output to print all items detected    
  
# Sample runs with outputs
![flask1](/img/output/output_final.JPG)   
![flask3](/img/flask3.JPG)    
![output1](/img/output/output1.JPG)    
![output2](/img/output/output2.JPG)   
![output3](/img/output/output3.JPG)   
![output4](/img/output_animate.gif)      
      
     
> Note : All images and videos are from Google images and Youtube and copyrights are reserved with their respective owners.

## Future Scope :     
* Add a URL input box : Currently, we only have choose photo option which pops up dialog box and then you can select photo from your local device but is it really necessary ? No why you should download the photo if you just share the public URL , then we can do it for you.     
* As of now, i have only described and made use of AWS S3 for storage but i will be deploying complete WebAPP on AWS using Elastic Beanstalk using EC2 instances.      
Maybe you can help me out !      

⭐️ this Project if you liked it !

