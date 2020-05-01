# EEG Tool
This is a rudimentary repository of various tools to work with .edf files and import data into python to allow work on ML libraries. 

eeg_extract is a wrapper class for pyEDFlib. The class reads, extracts labels, and epochs. 

eeg_extract requires pyEDFlib 
Install it using: 
pip install pyEDFlib

1. epoch_extract.read('file name') - Read .edf file 

2. epoch_extract.process() - Extract Epochs based on labels, and extracts labels, and ennumerates the labels. 

3. epochs, labels= epoch_extract.output() - Output epochs, and labels. 
