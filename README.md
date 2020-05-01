# EEG Tool
This is a rudimentary repository of various tools required to work with .edf files and import data into python to allow work on ML libraries

eeg_extract requires pyEDFlib 
Install it using: 
pip install pyEDFlib

epoch_extract.read('file name') - Read .edf file 
epoch_extract.process() - Extract Epochs based on labels, and extracts labels, and ennumerates the labels. 
epochs, labels= epoch_extract.output() - Output epochs, and labels. 
