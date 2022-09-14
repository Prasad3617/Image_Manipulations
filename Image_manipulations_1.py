#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np


# In[2]:


def read_image(image_path):
    image = cv2.imread(image_path)
    return image    


# In[3]:


def display_image(window_name,read_image):
    image = cv2.imshow(window_name,read_image) # "cv2" Reads images in 'BGR Format' # "cv2" does the flipping part of flipping BGR to RGB in the format which we are able to see.
    cv2.waitKey(0)


# In[4]:


def save_image(image_name,image):
    cv2.imwrite(image_name,image) #for ex: "save_image.jpg"


# In[5]:


def resize_image(image,dimensions,method_number):
    method = [cv2.INTER_AREA,cv2.INTER_LINEAR,cv2.INTER_NEAREST,cv2.INTER_CUBIC,cv2.INTER_LANCZOS4] #different methods available in CV2
    resize_method = method[method_number]
    resized_image = cv2.resize(image,dimensions,interpolation=resize_method) #3 parameters to be passed in image resizing operations 
    return resized_image


# In[6]:


def crop_image(image,dimensions):
    image_dims = image.shape
    h_s,h_e,w_s,w_e = dimensions
    width_dims = [w_s,w_e]
    height_dims = [h_s,h_e]
    np.clip(height_dims,a_min=0,a_max=image_dims[0])
    np.clip(width_dims,a_min=0,a_max=image_dims[1])
    crop_image = image[height_dims[0]:height_dims[1],width_dims[0]:width_dims[1]
    return crop_image


# Below is the implementaion of the above written code

# In[ ]:


image = read_image('car.jpg')
#display_image('Displayed_image',image)
#save_image('untitled_folder//saved_image.jpg',image)
print(image.shape)
dimensions = (160,160)
method = 1      #In python indexing begins from '0', '1' stands for eement at '2nd' position
resized_image = resize_image(image,dimensions,method)
display_image('resized_image',resized_image)
crop_dimensions = [0,150,0,150]
cropped_image = crop_image(image,crop_dimensions)
display_image('cropped_image',cropped_image)


# In[ ]:




