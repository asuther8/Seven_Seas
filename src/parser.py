# %%
import json,os
import matplotlib.pyplot as plt
from os import path

# Main function
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
        totalTorrents = 0
        for list in v:
            for dict in list:
                tempName = ""
                tempScore = 0
                for k, v in dict.items():
                    if "Torrents" in k:
                        tempScore = int(v)
                    if "Name" in k:
                        tempName = v.replace("\n","")

                if tempName in torrentData:
                    torrentData[tempName] += tempScore
                else:
                    torrentData[tempName] = tempScore

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
