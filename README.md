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

* Object detection in the browser using ```tensorflow.js```


# Getting started :     
### Real time Flask server hosted :      
* Log on to following URL hosted on pythonanywhere.com using flask server :    
#### [LIVE WEBSITE](https://souravsdlboy.pythonanywhere.com/)    
### CMD (terminal) solution :    
* We need to install latest version of Opencv.     
[Download here](https://pypi.org/project/opencv-python/)   
* Run the cmd (terminal).    

* Download the project files using following command in the directory from where you need to run the script :   
```
git clone https://github.com/souravs17031999/Edge-detection-Challenge 
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
