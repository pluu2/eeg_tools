#Let's  start with building the general structure of EEG graph data  

#Actual data is applied here. 

#We will need the connectivity, but not the features. This is important because the nodes
#Will still feed into the the networks found within the edges, but the features still feed into the edge networks.
#Also need to figure out how to do use tf to compare loss functions. 

#This needs to be put into a data loader
#the output will most likely be a dict of a dict.
#eeg data will be put into [sample,channel,datapoints] 
#this function will split by channel and datapoints. 
#the layout of the connections will be hard coded right now. 
#remember the layout of the graph will be 

#Defined Connectivity: 
#All connections are one way unless specified. At one point the connections will be doubled. 
#Numbers represent channels
#Channel 0 (Fp1) : 32,36,2,1 
#Channel 1(AF7): 0,2,5,6
#Channel 2(AF3) : 0,1,5,4,3,36,32
#Channel 3(F1): 37,46,10,9,4,2,36
#Channel 4(F3): 3,10,9,8,5,2
#CHannel 5(F5): 4,9,8,7,6,1,2
#Channel 6(F7): 5,8,7,1
#Channel 7 (FT7): 6,8,13,14
#Channel 8 (FC5): 9,12,13,14,7,6,5
#Channel 9(FC3) : 10,,11,12,13,8,5,4,3
#Channel 10(FC1): 46,47,11,12,9,4,3,37
#Channel 11(C1): 47,31,18,17,12,9,10,46,
#Channel 12(C3): 11,18,17,16,13,8,9,10
#Channel 13(C5): 9,12,17,16,15,14,7,8.
#Channel 14(T7): 13,16,15,7 8
#Channel 15(TP7): 14,13,16,21,22,23
#Channel 16(CP5): 12,17,20,21,22,15,14,13
#Channel 17(CP3): 11,18,19,20,21,16,13,12
#Channel 18 (CP1): 31,30,19,20,17,12,11,47
#Channel 19(P1): 31,30,29,25,20,17,18
#Channel 20(P3): 18,19,25,24,21,16,17
#Channel 21(P5): 17,20,25,24,22,15,16
#Channel 22(P7): 21,24,23,15,16.
#Channel 23(P9): 22,24,15
#Channel 24(PO7): 25,26,22,21,
#Channel 25(PO3): 29,28,26,24,21,20,19,30
#Channel 26(O1): 25,29,28,27,24
#Channel 27(IZ): 63,28,26
#channel 28(OZ): 62,63,27,26,25,29,
#Channel 29(POZ): 56,62,63,28,26,25,19,30
#channel 30(PZ): 56,29,19,18,31,55
#channel 31(CPZ): 48,55,56,30,19,18,11,47
#Channel 32(FpZ): 33,36,0
#Channel 33(Fp2): 34,35,32
#Channel 34(AF8): 41,40,35,33
#Channel 35(AF4): 34,40,39,38,33
#Channel 36(AFZ): 33,35,32,38,37,3,2,0)(??)
#Channel 37(Fz): 36,38,45,46,10,3
#Channel 38(F2): 35,39,44,45,46,37
#Channel 39(F4): 40,43,44,45,38,35,34
#Channel 40(F6): 41,43,44,39,35,34
#Channel 41(F8): 42,43,40,34
#Channel 42(FT8): 51,50,43,40,41
#Channel 43(FC6): 42,51,50,49,44,39,40,41
#Channel 44(FC4): 43,50,49,48,45,38,39,40,
#Channel 45(FC2): 44,49,48,47,46,37,38,39,
#Channel 46(FCZ): 45,48,47,11,10,3,37,38
#Channel 47(Cz): 45,48,55,31,18,11,10,46
#Channel 48(C2): 45,44,49,54,55,31,47,46,
#Channel 49(C4): 43,50,53,54,55,48,45,44.
#Channel 50(C6): 51,52,53,54,49,44,43,42
#Channel 51(T8): 52,53,50,43,42
#Channel 52(TP8): 59,58,53,50,51
#Channel 53(CP6): 51,52,59,58,57,54,49,50
#Channel 54(CP4): 50,53,58,57,56,55,48,49,
#Channel 55(CP2): 49,54,57,56,30,,31,47,48
#Channel 56(P2): 54,57,62,29,30,31,55
#Channel 57(P4): 53,58,62,56,55,54
#Channel 58(P6): 53,52,59,61,57,54,
#Channel 59(P8): 52,60,61,58,53
#Channel 60(P10): 59
#Channel 61(PO8): 59,58,62,63
#Channel 62(PO4): 58,61,63,57,56,29,,28
#channel 63(O2): 61,62,29,28,27
#channel 64:(A2)
#channel 65(A1) 
#CHannel 66-69 are ground leds 



class create_graphs():
  def __init__(self):
    self.eeg_data=0    
    self.data_dict={}   #this will store the data_dict temporarily as class moves through data
    self.final_dict={}  
    self.total_samples=0
    #load eeg data
  def load_data(self,data): 
    self.eeg_data=data
    self.eeg_data=self.eeg_data.astype('float32')
    self.total_samples=len(data)
    print ('loaded data')
  def create_graphs_from_data(self,start,end,sample_num,use_globals=True): 
    #since we don't really known the globals, lets set them to 1?  #we will be using a interaction network so globals are not required. 
    
    
    globals_ = [1.0,1.0,1.0,1.0]

    nodes=[[self.eeg_data[sample_num,0,start:end]],
          [self.eeg_data[sample_num,1,start:end]],
          [self.eeg_data[sample_num,2,start:end]],
          [self.eeg_data[sample_num,3,start:end]],
          [self.eeg_data[sample_num,4,start:end]],
          [self.eeg_data[sample_num,5,start:end]],
          [self.eeg_data[sample_num,6,start:end]],
          [self.eeg_data[sample_num,7,start:end]],
          [self.eeg_data[sample_num,8,start:end]],
          [self.eeg_data[sample_num,9,start:end]] ,
          [self.eeg_data[sample_num,10,start:end]],
          [self.eeg_data[sample_num,11,start:end]],
          [self.eeg_data[sample_num,12,start:end]],
          [self.eeg_data[sample_num,13,start:end]],
          [self.eeg_data[sample_num,14,start:end]],
          [self.eeg_data[sample_num,15,start:end]],
          [self.eeg_data[sample_num,16,start:end]],
          [self.eeg_data[sample_num,17,start:end]],
          [self.eeg_data[sample_num,18,start:end]],
          [self.eeg_data[sample_num,19,start:end]],
          [self.eeg_data[sample_num,20,start:end]],
          [self.eeg_data[sample_num,21,start:end]],
          [self.eeg_data[sample_num,22,start:end]],
          [self.eeg_data[sample_num,23,start:end]],
          [self.eeg_data[sample_num,24,start:end]],
          [self.eeg_data[sample_num,25,start:end]],
          [self.eeg_data[sample_num,26,start:end]],
          [self.eeg_data[sample_num,27,start:end]],
          [self.eeg_data[sample_num,28,start:end]],
          [self.eeg_data[sample_num,29,start:end]],
          [self.eeg_data[sample_num,30,start:end]],
          [self.eeg_data[sample_num,31,start:end]],
          [self.eeg_data[sample_num,32,start:end]],
          [self.eeg_data[sample_num,33,start:end]],
          [self.eeg_data[sample_num,34,start:end]],
          [self.eeg_data[sample_num,35,start:end]],
          [self.eeg_data[sample_num,36,start:end]],
          [self.eeg_data[sample_num,37,start:end]],
          [self.eeg_data[sample_num,38,start:end]],
          [self.eeg_data[sample_num,39,start:end]],
          [self.eeg_data[sample_num,40,start:end]],
          [self.eeg_data[sample_num,41,start:end]],
          [self.eeg_data[sample_num,42,start:end]],
          [self.eeg_data[sample_num,43,start:end]],
          [self.eeg_data[sample_num,44,start:end]],
          [self.eeg_data[sample_num,45,start:end]],
          [self.eeg_data[sample_num,46,start:end]],
          [self.eeg_data[sample_num,47,start:end]],
          [self.eeg_data[sample_num,48,start:end]],
          [self.eeg_data[sample_num,49,start:end]],
          [self.eeg_data[sample_num,50,start:end]],
          [self.eeg_data[sample_num,51,start:end]],
          [self.eeg_data[sample_num,52,start:end]],
          [self.eeg_data[sample_num,53,start:end]],
          [self.eeg_data[sample_num,54,start:end]],
          [self.eeg_data[sample_num,55,start:end]],
          [self.eeg_data[sample_num,56,start:end]],
          [self.eeg_data[sample_num,57,start:end]],
          [self.eeg_data[sample_num,58,start:end]],
          [self.eeg_data[sample_num,59,start:end]],
          [self.eeg_data[sample_num,60,start:end]],
          [self.eeg_data[sample_num,61,start:end]],
          [self.eeg_data[sample_num,62,start:end]],
          [self.eeg_data[sample_num,63,start:end]],
          [self.eeg_data[sample_num,64,start:end]],
          [self.eeg_data[sample_num,65,start:end]]]
      #the edges are not useful, so fil lwith 0 there will be 8 of them, because of the way the graph is connected


    senders = [0,0,0,0,
              1,1,1,1,
              2,2,2,2,2,2,2,
               3,3,3,3,3,3,3,
               4,4,4,4,4,
               5,5,5,5,5,5,5,
               6,6,6,6,
               7,7,7,7,7,
               8,8,8,8,8,8,8,
               9,9,9,9,9,9,9,9,
               10,10,10,10,10,10,10,10,
               11,11,11,11,11,11,11,11,
               12,12,12,12,12,12,12,12,
               13,13,13,13,13,13,13,13,
               14,14,14,14,14,
               15,15,15,15,15,15,
               16,16,16,16,16,16,16,16,
               17,17,17,17,17,17,17,17,
               18,18,18,18,18,18,18,18,
               19,19,19,19,19,19,19,
               20,20,20,20,20,20,20,
               21,21,21,21,21,21,21,
               22,22,22,22,22,
               23,23,23,
               24,24,24,24,
               25,25,25,25,25,25,25,25,
               26,26,26,26,26,
               27,27,27,
               28,28,28,28,28,28,
               29,29,29,29,29,29,29,29,
               30,30,30,30,30,30,
               31,31,31,31,31,31,31,31,
               32,32,32,
               33,33,33,
               34,34,34,34,
               35,35,35,35,35,
               36,36,36,36,36,36,36,36,
               37,37,37,37,37,37,
               38,38,38,38,38,38,
               39,39,39,39,39,39,39,
               40,40,40,40,40,40,
               41,41,41,41,
               42,42,42,42,42,
               43,43,43,43,43,43,43,43,
               44,44,44,44,44,44,44,44,
               45,45,45,45,45,45,45,45,
               46,46,46,46,46,46,46,46,
               47,47,47,47,47,47,47,47,
               48,48,48,48,48,48,48,48,
               49,49,49,49,49,49,49,49,
               50,50,50,50,50,50,50,50,
               51,51,51,51,51,
               52,52,52,52,52,
               53,53,53,53,53,53,53,53,
               54,54,54,54,54,54,54,54,
               55,55,55,55,55,55,55,55,
               56,56,56,56,56,56,56,
               57,57,57,57,57,57,
               58,58,58,58,58,58,
               59,59,59,59,59,
               60,60,60,
               61,61,61,61,
               62,62,62,62,62,62,62,
               63,63,63,63,63
               

               
               
               ]  # Index of the sender node for edge 3

    receivers = [32,36,2,1,
                 0,2,5,6,
                0,1,5,4,3,36,32,
                 37,46,10,9,4,2,36,
                 3,10,9,8,5,2,
                 4,9,8,7,6,1,2,
                 5,8,7,1,
                 6,8,13,14,
                 9,12,13,14,7,6,5,
                 10,11,12,13,8,5,4,3,
                 46,47,11,12,9,4,3,37,
                 47,31,18,17,12,9,10,46,
                 11,18,17,16,13,8,9,10,
                 9,12,17,16,15,14,7,8,
                 13,16,15,7,8,
                 14,13,16,21,22,23,
                 12,17,20,21,22,15,14,13,
                 11,18,19,20,21,16,13,12,
                 31,30,19,20,17,12,11,47,
                 31,30,29,25,20,17,18,
                 18,19,25,24,21,16,17,
                 17,20,25,24,22,15,16,
                 21,24,23,15,16,
                 22,24,15,
                 25,26,22,21,
                 29,28,26,24,21,20,19,30,
                 25,29,28,27,24,
                 63,28,26,
                 62,63,27,26,25,29,
                 56,62,63,28,26,25,19,30,
                 56,29,19,18,31,55,
                 48,55,56,30,19,18,11,47,
                 33,36,0,
                 34,35,32,
                 41,40,35,33,
                 34,40,39,38,33,
                 33,35,32,38,37,3,2,0,
                 36,38,45,46,10,3,
                 35,39,44,45,46,37,
                 40,43,44,45,38,35,34,
                 41,43,44,39,35,34,
                 42,43,40,34,
                 51,50,43,40,41,
                 42,51,50,49,44,39,40,41,
                 43,50,49,48,45,38,39,40,
                 44,49,48,47,46,37,38,39,
                 45,48,47,11,10,3,37,38,
                 45,48,55,31,18,11,10,46,
                 45,44,49,54,55,31,47,46,
                 43,50,53,54,55,48,45,44,
                 51,52,53,54,49,44,43,42,
                 52,53,50,43,42,
                 59,58,53,50,51,
                 51,52,59,58,57,54,49,50,
                 50,53,58,57,56,55,48,49,
                 49,54,47,56,30,31,47,48,
                 54,57,62,29,30,31,55,
                 53,58,62,56,55,54,
                 53,52,59,61,57,54,
                 52,60,61,58,53,
                 59,52,61,
                 59,58,62,63,
                 58,61,63,57,56,29,28,
                 61,62,29,28,27




                 
                 
                 ]  # Index of the receiver node for edge 3

    edges=[]
    for i in range(len(receivers)):
      edges.append([[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0],[0.0]])


    data_dict={
      "globals": globals_,
      "nodes": nodes,
      "edges": edges,
      "senders": senders,
      "receivers": receivers}
    return data_dict

  def get_graphs(self,data_slice):
    data_size=len(self.eeg_data[0,0]) #find the total number of data in datapoints. 
    num_slices=data_size//data_slice #finds number of slices that can be done. 
    print (f'number of slices to be created: ' , num_slices)
    start=0
    end=start+data_slice
    time_stamps=[] #list of for a single sample it will contain all the time stamps
    single_samp=[]

    for i in range(self.total_samples):
      for j in range(num_slices):
        time_stamps.append(self.create_graphs_from_data(start,end,i))
        start=end
        end+=data_slice
      single_samp.append(time_stamps)
      start=0
      end=data_slice
      time_stamps=[]
    return single_samp
