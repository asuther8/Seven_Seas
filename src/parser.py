# %%
import json,os
import matplotlib.pyplot as plt
from os import path
class show:
    def __init__(self, name, service, total, date):
        self.name = name
        self.total = total
        self.date = date
         
class dataline:
    def __init__(self, name, date, views, file):
        self.name = name
        self.date = date
        self.views = views
        self.file = file

# Main function
def main():
    s = 'Solid Torrents-'
    e = '.json'

    # Attempts to form path where the data is located from current directory
    dataPath = os.path.join(os.path.dirname(__file__), os.pardir, 'data')

    showlist = {}

    # Iterates through files in the data directory
    for file in os.listdir(dataPath):

        # Calls jsonToList on each file
        if file != 'Solid_Torrents.json' and file != 'Solid_Torrents-Disney_16347609071.json' and file != 'ommision words.txt':
            print(file)
            newFile = jsonToList(os.path.join(dataPath, file))
            print(newFile)
            for dict in newFile:
                # iterating through each json file here
                tempName = ""
                for k, v in dict.items():

                    if "Name" in k:
                        tempName = v.replace("\n","")

                        if tempName not in showlist:
                            showlist[tempName] = show(tempName,"empty",0,0)

                    if "Torrents" in k:
                        tempScore = int(v)

                        if tempName in showlist:
                            showlist[tempName].total += tempScore
                        else:
                            showlist[tempName] = tempScore

                    if "Date" in k:

                        splitDate = v.split()
                        time = 0

                        if(splitDate[2] == "a"):
                            time = 1
                        else:
                            time = int(splitDate[2])

                        newAge = 0
                        if splitDate[3] == "days" or splitDate[3] ==  "day":
                            newAge = time * 1
                        if splitDate[3] == "months" or splitDate[3] == "month":
                            newAge = time * 30
                        if splitDate[3] == "years" or splitDate[3] == "year":
                            newAge = time * 365

                        if newAge > showlist[tempName].date:
                            showlist[tempName].date = newAge
                
                    showlist[tempName].service = file[file.find(s)+len(s):file.rfind(e)]

    for k,v in showlist.items():
        print(k)
        for var in vars(v):
            print(var,": ",getattr(v,var))
        print('')

    #plt.style.use('ggplot')
    #x_pos = [i for i, _ in enumerate(showlist.keys())]
    #plt.bar(x_pos,showlist.values(),color='green')
    #plt.xlabel("Media torrented")
    #plt.ylabel("Torrents in millions")
    #plt.xticks(x_pos,showlist.keys())
    #plt.show()


# Takes the path of each json file and returns it as a list of dictionaries
def jsonToList(path):

    with open(path, "r") as textFile:
        jsonString = textFile.read()
        return json.loads(jsonString)

# Lets main be above function declarations
if __name__ == "__main__":
    main()
# %%
