# Object-Detection-MobileNet-cv

# Project Objective: 
Using a machine learning toolkit of your choice, create a tool which identifies objects in the image, then returns positions in pixels corresponding to bounding boxes of a user-selected class of object in the image.    

# Approach :   
* Pre-trained ```MobileNet + SSD``` run from command line (terminal).
* Pre-trained ```MobileNet + SSD``` with ```Flask``` server.     

> Brief introduction       
![conv1](/img/conv1.png)      
* MobileNet uses Depthwise Separable Convolution which consists of two steps - Depthwise convolution and then Pointwise convolution.   
* Depthwise convolution channel wise spatial convolution.   
* Pointwise convolution uses Network-In-Network architechture (NiN) which is bsically doing 1 x 1 convolutions along with other conv layers. This helps in reducing parameters to a large extent.     

* [Pre-trained ```Resnet-152``` with ```GUI Tkinter```](https://github.com/souravs17031999/Retinal_blindness_detection_Pytorch).     

> Brief introduction            
![conv1](/img/conv2.gif)         
* Resnet-152 uses residual connections, The core idea exploited in these models, residual connections, is found to greatly improve gradient flow, thus allowing training of much deeper models with tens or even hundreds of layers.       

* Object detection in the browser using ```tensorflow.js``` [TODO - Currently in progress]  


### Real time Flask server hosted :      
* Log on to following URL hosted on pythonanywhere.com using flask server :    

### [LIVE WEBSITE](https://souravsdlboy.pythonanywhere.com/object)    

# Getting started :     
### FLASK solution : 
* Run the cmd (terminal). 
* Move to the project main directory where the project is downloaded.
* Move to directory ```object_detect_flask```.  
* Now run following :     
(for windows)     
> set FLASK_APP=object.py    
> python -m flask run       

(for other termials)          

> $ export FLASK_APP=object.py      
> $ flask run       

[Other troubleshooting issues related to flask server](https://flask.palletsprojects.com/en/1.1.x/quickstart/#what-to-do-if-the-server-does-not-start)    

* Now the local server should start, log on to : [local url port] shown on terminal.     
(Most probably it will be http://127.0.0.1:5000/ , or maybe any other port)   

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
![flask1](/img/flask1.JPG)   
![flask3](/img/flask3.JPG)    
![output1](/img/output/output1.JPG)    
![output2](/img/output/output2.JPG)   
![output3](/img/output/output3.JPG)   
![output4](/img/output_animate.gif)      
      
     
> Note : All images and videos are from Google images and Youtube and copyrights are reserved with their respective owners.
