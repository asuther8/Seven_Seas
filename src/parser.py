import json,os
from os import path

# Main function
def main():

    # Attempts to form path where the data is located from current directory
    dataPath = os.path.join(os.path.dirname(__file__), os.pardir, 'data')

    files = []

    # Iterates through files in the data directory
    for file in os.listdir(dataPath):

        # Calls jsonToList on each file
        files.append(jsonToList(os.path.join(dataPath, file)))

        # Prints the results
        print(file,':')
        for jsonList in files:
            for list in jsonList:
                for dict in list:
                    for k, v in dict.items():
                        print('   ',k, ' : ', v)

                    print('\n')

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