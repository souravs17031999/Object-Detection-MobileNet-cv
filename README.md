# Object-Detection-MobileNet-cv
This repo contains script for detecting multiple objects in the given image and return bounding boxes for a given query string.

# Project Objective: 
Using a machine learning toolkit of your choice, create a tool which identifies objects in the image, then returns positions in pixels corresponding to bounding boxes of a user-selected class of object in the image.    

# Approach :   
The following Python script uses MobileNet + SSD for object detection in a given image as it is one of the light weight balanced models with optimum accuracy.   
* More approach[TODO!]

# Getting started :
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

# Front-end and Web server
* The pages ```index.html``` and ```result.html``` is just skeleton form of the actual page , just for showcasing the look.    
It is in active developement and a web server based on Flask will be added soon[TODO!]
