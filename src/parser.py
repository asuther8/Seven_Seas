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

    
    for k,v in files.items():
        totalTorrents = 0
        name = ""
        print(k,':     ')
        for list in v:
            for dict in list:
                for k, v in dict.items():
                    if "Torrents" in k:
                        totalTorrents += int(v)
                    if "Name" in k:
                        name = v

                    print('   ',k.replace("\n",""), ' : ', v.replace("\n",""))

        
                print('\n')
        print(name, ": ",totalTorrents,"\n")
        plt.bar(1,totalTorrents,color='green')
        plt.xlabel("Torrents")
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
