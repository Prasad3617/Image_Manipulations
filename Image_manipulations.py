#!/usr/bin/env python
# coding: utf-8

# In[13]:


import cv2
import numpy as np


# In[14]:


def read_image(image_path):
    image = cv2.imread(image_path)
    return image    


# In[15]:


def display_image(window_name,read_image):
    image = cv2.imshow(window_name,read_image) # "cv2" Reads images in 'BGR Format' # "cv2" does the flipping part of flipping BGR to RGB in the format which we are able to see.
    cv2.waitKey(0)


# In[16]:


def save_image(image_name,image):
    cv2.imwrite(image_name,image) #for ex: "save_image.jpg"


# In[17]:


def resize_image(image,dimensions,method_number):
    method = [cv2.INTER_AREA,cv2.INTER_LINEAR,cv2.INTER_NEAREST,cv2.INTER_CUBIC,cv2.INTER_LANCZOS4] #different methods available in CV2
    resize_method = method[method_number]
    resized_image = cv2.resize(image,dimensions,interpolation=resize_method) #3 parameters to be passed in image resizing operations 
    return resized_image


# Below is an implementaion of the above written code

# In[ ]:


image = read_image('car.jpg')
#display_image('Displayed_image',image)
#save_image('untitled_folder//saved_image.jpg',image)
print(image.shape)
dimensions = (160,160)
method = 1      #In python indexing begins from '0', '1' stands for eement at '2nd' position
resized_image = resize_image(image,dimensions,method)
display_image('resized_image',resized_image)


# In[ ]:




