# Object-Detection-MobileNet-cv

# Project Objective: 
Using a machine learning toolkit of your choice, create a tool which identifies objects in the image, then returns positions in pixels corresponding to bounding boxes of a user-selected class of object in the image.    

# Approach :   
* Pre-trained ```MobileNet + SSD``` run from command line (terminal).
* Pre-trained ```MobileNet + SSD``` with ```Flask``` server.   
> Brief introduction       
![conv1](/img/conv1.PNG)      
* MobileNet uses Depthwise Separable Convolution which consists of two steps - Depthwise convolution and then Pointwise convolution.   
* Depthwise convolution channel wise spatial convolution.   
* Pointwise convolution uses Network-In-Network architechture (NiN) which is bsically doing 1 x 1 convolutions along with other conv layers. This helps in reducing parameters to a large extent.     

* [Pre-trained ```Resnet-152``` with ```GUI Tkinter```](https://github.com/souravs17031999/Retinal_blindness_detection_Pytorch).
* Object detection in the browser using ```tensorflow.js```


# Getting started :     

### CMD (terminal) solution :    
* We need to install latest version of Opencv.     
[Download here](https://pypi.org/project/opencv-python/)   
* Run the cmd (terminal).    

* Download the project files using following command in the directory from where you need to run the script :   
```
git clone https://github.com/souravs17031999/Object-Detection-MobileNet-cv   
```   
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
![output1](/img/output/output1.JPG)
![output2](/img/output/output2.JPG)
![output3](/img/output/output3.JPG)

### Flask server :     
