# -*- coding: utf-8 -*-
"""Image classification Project.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19S4TP9ihqlBeoxBq5ekqhhGEwGqJ_M6N
"""

!pip install -q kaggle

from google.colab import files
# Upload the Kaggle API credentials JSON file
files.upload()

#do not run twice!!
!mkdir -p ~/.kaggle
!mv kaggle.json ~/.kaggle/
!chmod 600 ~/.kaggle/kaggle.json

!kaggle datasets download -d darren2020/ct-to-mri-cgan

! unzip ct-to-mri-cgan.zip -d ct-to-mri-cgan

import pandas as pd
import numpy as np
import cv2
import os
#define the cat and dog folder
CT_folder='/content/ct-to-mri-cgan/Dataset/images/testA'
MRI_folder='/content/ct-to-mri-cgan/Dataset/images/testB'
#initialize lists to store images and labels
images=[]
labels=[]
#load and preprocess cat images
for filename in os.listdir(CT_folder):
  if filename.endswith('.jpg'):
    img=cv2.imread(os.path.join(CT_folder,filename))
    img=cv2.resize(img,(128,128)) #resize the images
    images.append(img)
    labels.append(0) # 0 represents cats!
#load and preprocess dog images
for filename in os.listdir(MRI_folder):
  if filename.endswith('.jpg'):
    img=cv2.imread(os.path.join(MRI_folder,filename))
    img=cv2.resize(img,(128,128))
    images.append(img)
    labels.append(1) # 1 represents dogs!
#conver lists to Numpy arrays!
images=np.array(images)
labels=np.array(labels)

from sklearn.model_selection import train_test_split
#split the data into training and testing sets
x_train,x_test,y_train,y_test=train_test_split(images,labels,test_size=0.2,random_state=42)

#KERAS MODEL
from operator import mod
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
model=keras.Sequential([
    layers.Conv2D(32,(3,3),activation='relu',input_shape=(128,128,3)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64,(3,3), activation='relu'),
    layers.MaxPool2D((2,2)),
    layers.Flatten(),
    layers.Dense(64,activation='relu'),
    layers.Dense(2,activation='softmax')])
#compile the model
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

#train the model
history = model.fit(x_train , y_train , epochs=10 , batch_size=32 , validation_split=0.2)

#evaluating the model
test_loss,test_acc=model.evaluate(x_test,y_test,verbose=2)
print(f'Test accuracy= {test_acc}')

model.summary()

#Example: predicting on a single image
sample_image=x_test[6] #replace with your image data!
predictions=model.predict(np.expand_dims(sample_image,axis=0))
predicted_lable=np.argmax(predictions)

#you can interpret the lable with yousing your dataset's class lables (0 for cats ,1 for dogs)
class_lables=['CT','MRI']
predicted_class=class_lables[predicted_lable]
print(f'predicted_class: {predicted_class}')

import matplotlib.pyplot as plt
#Display the sample image
plt.imshow(sample_image)
plt.axis('off')
plt.show()

#test from out of our dataset
uploaded=files.upload()

img_bgr = cv2.imread('/content/pexels-mart-production-7089020.jpg', cv2.IMREAD_COLOR)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)

plt.imshow(img_rgb.astype(float))
plt.axis('off')
plt.show()

uploaded_image=cv2.resize(img_bgr,(128,128))
#uploaded_image=cv2.cvtColor(uploaded_image,cv2.COLOR_BGR2RGB)
plt.imshow(uploaded_image)
plt.axis('off')
plt.show()

#comparing both libraries
img_mpl = plt.imread(trainA_files[20])
img_cv2 = cv2.imread(trainA_files[20])
img_mpl.shape, img_cv2.shape

uploaded_image=uploaded_image.astype('float32') / 255.0
uploaded_image=np.expand_dims(uploaded_image,axis=0)
predictions=model.predict(uploaded_image)
predicted_lable=np.argmax(predictions)

class_lables=['CT','MRI']
predicted_class=class_lables[predicted_lable]
print(f'predicted_class: {predicted_class}')

#PYTORCH

img_mpl

img_mpl.max()

fig,ax = plt.subplots(figsize = (10,10))
ax.imshow(img_mpl)
ax.axis('off')
plt.show()

