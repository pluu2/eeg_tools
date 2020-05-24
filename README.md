# EEG Tools
This is a rudimentary repository of various tools to work with .edf files and import data into python to allow work on ML libraries. 



## eeg_extract
----
eeg_extract is a wrapper class for pyEDFlib. The class reads, extracts labels, and epochs. eeg_extract requires pyEDFlib 

Install pyEDFlib it using: 

```pip install pyEDFlib```

#### Available functions: 
-----
``` epoch_extract.read('file name') ```  Read .edf file


```epoch_extract.process() ``` - Extract Epochs based on labels, and extracts labels, and ennumerates the labels.

```epoch_extract.make2D (width) ``` Creates a numpy array with structure [epoch_number,channel_number,datapoints] . 

The number of datapoints will have to be specified. 

```epochs, labels,classes= epoch_extract.output() ```- Output epochs, and labels. 

The structure of the output data will be a dict with the key of structure '[epoch_number]C[channel_number]' - This function has lost some of it's usefulness, 'epochs' as an output is not as important, the make 2D function will make it much easier to work with EEG data. 

## create_graphs
-----
Very rough class function. Will take raw EEG data and generate dicts . 

#### Available Functions: 
----
```create_graphs.load_data(data) ``` loads the EEG data into the class. The data must be organized [sample,channel,data]

```graph_dict_list=create_graphs.get_graphs(data_slice)```  outputs a list of graph dict data for use in Graph_net library. 
This function only supports one graph structure. 

note: there is implementation for tensorflow-graphnets and for pytorch-geometric separately. 
