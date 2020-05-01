# EEG Tools
This is a rudimentary repository of various tools to work with .edf files and import data into python to allow work on ML libraries. 

eeg_extract is a wrapper class for pyEDFlib. The class reads, extracts labels, and epochs. 

### eeg_extract
eeg_extract requires pyEDFlib 
Install pyEDFlib it using: 

```pip install pyEDFlib```

Available functions: 

``` epoch_extract.read('file name') ```  Read .edf file


```epoch_extract.process() ``` - Extract Epochs based on labels, and extracts labels, and ennumerates the labels.


```epochs, labels= epoch_extract.output() ```- Output epochs, and labels. 

The structure of the output data will be a dict with the key of structure '[epoch_number]C[channel_number]'
