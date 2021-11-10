# %%
import json,os
import matplotlib.pyplot as plt
from os import path

# Main function
class show:
    def __init__(self, name, service, total):
        self.name = name
        self.service = service
        self.total = total
class dataline:
    def __init__(self, name, data, views, file){
        self.name = name
        self.data = data
        self.views = views
        self.file = file
def main():

    # Attempts to form path where the data is located from current directory
    dataPath = os.path.join(os.path.dirname(__file__), os.pardir, 'data')

    files = {}

    # Iterates through files in the data directory
    for file in os.listdir(dataPath):

        # Calls jsonToList on each file
        files[file] = (jsonToList(os.path.join(dataPath, file)))

    torrentData = {}
    for k,v in files.items():
        for list in v:
            oldestDate = 0
            for dict in list:
                tempName = ""
                tempScore = 0
                
                # iterating through each json file here
                for k, v in dict.items():
                    if "Torrents" in k:
                        tempScore = int(v)
                    if "Name" in k:
                        tempName = v.replace("\n","")
                    if "Date" in k:
                        splitDate = v.split()
                        if int(splitDate[2]) > oldestDate and splitDate[3] == "months":
                            oldestDate = int(splitDate[2])
                if tempName in torrentData:
                    torrentData[tempName] += tempScore
                else:
                    torrentData[tempName] = tempScore

            

            



            # calculating torrents per month
            if oldestDate != 0:
                torrentData[tempName] /= oldestDate

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
