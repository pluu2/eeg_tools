#Let's  start with building the general structure of EEG graph data  

#Actual data is applied here. 
# Global features for graph 0. This is applied to all the features within the node 
#We will need the connectivity, but not the features. This is important because the nodes
#Will still feed into the the networks found within the edges, but the features still feed into the edge networks.
#Also need to figure out how to do use tf to compare loss functions. 

#This needs to be put into a data loader
#the output will most likely be a dict of a dict.
#eeg data will be put into [sample,channel,datapoints] 
#this function will split by channel and datapoints. 
#the layout of the connections will be hard coded right now. 
#remember the layout of the graph will be 

#node 0= channel 2 
#node 1= channel 5
#node 2= channel 9
#node 3 = channel 3
#node 4= channel 4

class create_graphs():
  def __init__(self):
    self.eeg_data=0    
    self.data_dict={}   #this will store the data_dict temporarily as class moves through data
    self.final_dict={}  
    self.total_samples=0
    #load eeg data
  def load_data(self,data): 
    self.eeg_data=data
    self.total_samples=len(data)
    print ('loaded data')
  def create_graphs_from_data(self,start,end,use_globals=True): 
    #since we don't really known the globals, lets set them to 1? 
    sample_num=0
    
    globals_ = [[1],[1],[1],[1]]

    nodes=[self.eeg_data[sample_num,2,start:end],
          self.eeg_data[sample_num,5,start:end],
          self.eeg_data[sample_num,9,start:end],
          self.eeg_data[sample_num,3,start:end],
          self.eeg_data[sample_num,4,start:end]]
      #the edges are not useful, so fil lwith 0 there will be 8 of them, because of the way the graph is connected
    edges=[[0],[0],[0],[0],[0],[0],[0],[0]]

      # The sender and receiver nodes associated with each edge for graph 1.
    senders = [0,  # Index of the sender node for edge 0
                1,  # Index of the sender node for edge 1
                2,  # Index of the sender node for edge 2
                3,
                4,
                4,
                4,
                4]  # Index of the sender node for edge 3

    receivers = [4,  # Index of the receiver node for edge 0
                  4,  # Index of the receiver node for edge 1
                  4,  # Index of the receiver node for edge 2
                  4,
                  0,
                  1,
                  2,
                  3 ]  # Index of the receiver node for edge 3

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
        time_stamps.append(self.create_graphs_from_data(start,end))
        start=end
        end+=data_slice
      single_samp.append(time_stamps)
      start=0
      end=data_slice
      time_stamps=[]
    return single_samp
