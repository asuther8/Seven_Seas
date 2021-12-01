# %%
import json,os
import matplotlib.pyplot as plt
from os import path
class show:
    def __init__(self, name, service, total, date):
        self.name = name
        self.total = total
        self.date = date
        self.service = service
         
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


    individualViews = {}

    exViews = 0
    nonExViews = 0
    globalViews = 0
    localViews = 0
    preCovid = 0
    postCovid = 0

    # Attempts to form path where the data is located from current directory
    dataPath = os.path.join(os.path.dirname(__file__), os.pardir, 'data')

    showlist = {}

    # Iterates through files in the data directory
    for file in os.listdir(dataPath):

        # Calls jsonToList on each file
        if file != 'ommision words.txt':
            individualViews[file] = 0
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
                        individualViews[file] += tempScore
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

                        if newAge < 580:
                            preCovid += newAge
                        else:
                            postCovid += newAge


                        if newAge > showlist[tempName].date:
                            showlist[tempName].date = newAge
                
                    showlist[tempName].service = file[file.find(s)+len(s):file.rfind(e)]




    for k,v in showlist.items():
        print(k)

        for var in vars(v):
            print(var,": ",getattr(v,var))
        print('')

    print(individualViews)

    for k,v in individualViews.items():
        if k == 'Solid Torrents-Non-Ex.json':
            nonExViews += v
        else:
            exViews += v

        if k != 'Solid Torrents-Non-Ex.json':
            if k == 'Solid Torrents-HBO.json' or k == 'Solid Torrents-Prime.json':
                localViews += v
            else:
                globalViews += v
        

            
    print("Non-exclusive views: ", nonExViews)
    print("Exclusive views:  ", exViews/5,'\n')

    print("International service views: ", globalViews/3)
    print("Region locked views: ", localViews/2,'\n')

    print("Pre-covid numbers: ", preCovid)
    print("Post-covid numbers: ", postCovid)


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
