
def isolateData(selector,channel,labels,data):
  selected=[]
  for i in  range(len(labels)): 
    if labels[i]==selector:
      selected.append(data[str(i)+'c'+str(channel)])#epochs with class AGMSY5
  return selected
