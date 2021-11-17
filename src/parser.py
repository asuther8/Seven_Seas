# %%
import json,os
import matplotlib.pyplot as plt
from os import path
class show:
    def __init__(self, name, service, total, date):
        self.name = name
        self.total = total
        self.date = date

# Main function
def main():

    # Attempts to form path where the data is located from current directory
    dataPath = os.path.join(os.path.dirname(__file__), os.pardir, 'data')
    list = []

    files = {}

    # Iterates through files in the data directory
    for file in os.listdir(dataPath):

        # Calls jsonToList on each file
        files[file] = (jsonToList(os.path.join(dataPath, file)))

    torrentData = {}
    showlist = []
    inlist = 0
    for k,v in files.items():
        for list in v:
            oldestDate = 0
            for dict in list:
                tempName = ""
                tempScore = 0
                tempDate = 0
                # iterating through each json file here
                for k, v in dict.items():

                    if "Name" in k:
                        tempName = v.replace("\n","")
                        for i in showlist:
                            if i.name == tempName:
                                inlist = 1
                        if inlist == 0:
                            showlist.append(show(tempName, 0, 0))

                        else: 
                            inlist = 0
               
                    if "Torrents" in k:
                        tempScore = int(v)
                        for i in showlist:
                            if i.name == tempName:
                                i.views += tempScore
                    if "Date" in k:
                        splitDate = v.split()
                        if splitDate[3] == "years":
                            tempDate = int(splitDate[2]) * 12;

                        elif splitDate[3] == "months":
                                tempDate = int(splitDate[2]);
                        for i in showlist:
                            if i.name == tempName:
                                if i.Date > tempDate:
                                    i.Date = tempDate
                if tempName in torrentData:
                    torrentData[tempName] += tempScore
                else:
                    torrentData[tempName] = tempScore







            # calculating torrents per month
            if oldestDate != 0:
                torrentData[tempName] /= oldestDate
    for i in showlist:
        print(i.name, i.date, i.views, sep=':')
    print(torrentData)
    plt.style.use('ggplot')
    x_pos = [i for i, _ in enumerate(torrentData.keys())]
    plt.bar(x_pos,torrentData.values(),color='green')
    plt.xlabel("Media torrented")
    plt.ylabel("Torrents in millions")
    plt.xticks(x_pos,torrentData.keys())
    plt.show()


# Takes the path of each json file and returns it as a list of dictionaries
def jsonToList(path):

    jsonList = []

    with open(path, "r") as textFile:
        jsonString = textFile.read()

        jsonList.append(json.loads(jsonString))

    return jsonList

# Lets main be above function declarations
if __name__ == "__main__":
    main()
# %%
