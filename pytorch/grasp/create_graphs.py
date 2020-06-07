
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


from torch_geometric.data import Data
import torch

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
    
    nodes=[]
    
    #so there is 32 total 
    for i in range(32):  #32 channels 
      #print (i)
      nodes.append(self.eeg_data[sample_num,i,start:end])
    node_tensor = torch.tensor(nodes)
      #the edges are not useful, so fil lwith 0 there will be 8 of them, because of the way the graph is connected

    
#will subtract 1 from these later.
    senders = [1,1,1,1,
               2,2,2,2,
               3,3,3,
               4,4,4,4,4,
               5,5,5,5,5,5,5,
               6,6,6,6,6,
               7,7,7,
               8,8,8,8,
               9,9,9,9,
               10,10,10,10,
               11,11,11,11,
               12,12,12,12,
               13,13,13,13,
               14,14,14,14,
               15,15,15,15,
               16,16,16,16,
               17,17,
               18,18,18,18,
               19,19,19,19,
               20,20,20,20,
               21,21,21,21,
               22,22,
               23,23,23,23,23,
               24,24,24,24,24,
               25,25,25,25,25,25,25,
               26,26,26,26,26,26,
               27,27,27,27,27,
               28,28,28,
               29,29,29,29,29,
               30,30,30,30,30,
               31,31,31,31,31,
               32,32,32,
               ]  # Index of the sender node for edge 3

    receivers = [3,4,5,2,
                 1,5,6,7,
                 1,4,8,
                 1,5,9,8,3,
                 2,6,10,14,9,4,1,
                 2,7,11,10,5,
                 11,6,2,
                 3,4,13,12,
                 4,5,14,13,
                 5,6,15,14,
                 6,7,16,15,
                 3,8,18,17,
                 8,9,19,18,
                 9,10,20,19,
                 10,11,21,20,
                 7,11,21,22,
                 12,23,
                 12,13,24,23,
                 13,14,25,24,
                 14,15,26,25,
                 15,16,27,26,
                 16,27,
                 17,18,24,29,28,
                 18,19,25,29,23,
                 19,20,26,31,30,29,24,
                 20,21,27,31,30,25,
                 26,21,22,32,31,
                 17,23,29,
                 23,24,25,30,28,
                 24,25,26,31,29,
                 25,26,27,32,30,
                 31,27,22     

    ]  # Index of the receiver node for edge 3
    #print (len(senders))
    #print (len(receivers))
    senders=[x-1 for x in senders]
    receivers=[x-1 for x in receivers]
    #print (senders)
    #print (receivers)
    #convert the old senders and receivers into another one. 
    #print (len(receivers))
    #print (len(senders))
    #print (receivers[166])
    #print (modified_channels[receivers[166]])
    

    #for pytorch-geometric the attach the sender and receivers into a a list. 
    connections = [] 
    connections.append(senders)
    connections.append(receivers)
    edge_connections=torch.tensor(connections) 

    edges=[] #this can stay the same, and is just a appending of edge features, (there are automatically 400 here). 
    for i in range(len(senders)): #this will need to be figurd out
      edges.append([0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])
    edges_tensor=torch.tensor(edges)

    data_graph=Data(x=node_tensor,edge_attr=edges_tensor,edge_index=edge_connections)


    return data_graph

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
