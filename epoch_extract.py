# -*- coding: utf-8 -*-
"""epoch_extract

Automatically generated by Colaboratory.


"""

#This is just a simple extractor for epochs

import pyedflib
from keras.utils import to_categorical
from sklearn import preprocessing
from pyedflib import highlevel
import numpy as np

class epoch_extract(): 
  def __init___(self): 
    self.sample_rate=0
    self.final_labels
    self.epoch={} 
    self.test
  def read(self,datafile): 
    self.signals, self.signal_headers, self.header = highlevel.read_edf(datafile)
    self.sample_rate= self.signal_headers[0]['sample_rate']
    print(f'Data Imported, sample rate: ' , self.sample_rate)
  
  def process(self): 
    events=self.header['annotations'][0:len(self.header['annotations'])]
    events=np.array(events) 
    labels=events[:,2] #gather labels 
    time_stamps=events[:,0] #gather time stamps.
    le = preprocessing.LabelEncoder()
    le.fit(labels)
    classes=le.classes_
    self.classes=classes
    self.final_labels=le.transform(labels) #converts all the classes in to values this will be outputted. 
    print ('extracted labels')
    time_stamps_fl=[]
    for i in range(len(time_stamps)):
      time_stamps_fl.append(float(time_stamps[i]))
    time_stamps_fl=np.array(time_stamps_fl)
    time_stamps_fl=np.round(time_stamps_fl *self.sample_rate)
    self.test=time_stamps_fl    

    
    epoch ={}
    start=0
    ctr=0
    for i in range(1,len(time_stamps_fl)):  
      end=int(time_stamps_fl[i]) 
      print (end)
      for channels in range(len(self.signals)):    
        epoch.update({str(i-1)+ 'c' + str(channels): self.signals[channels,start:end]})
      ctr+=1
      start=end

    print(f'extracted ', ctr, ' epochs')

    self.epoch=epoch
  
    #this will turn each epoch into channel:time epoch, but will clip at the smallest time. 
  def make2D (self,width): 
    #find channels.
    epoch=self.epoch
    total_epochs=int(len(self.final_labels))
    channels = len(self.signals)
    output = np.zeros((total_epochs,channels,width))

    for (keys,values) in epoch.items(): 
      temp=keys
      c=temp.find('c')
      epoch_ = int(temp[0:c])
      channel = int(temp[c+1:])

      output[epoch_,channel-1]=epoch[keys][0:int(width)]
    return output


  def output(self):
    return [self.epoch,self.final_labels,self.classes]
