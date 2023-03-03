import json

file_path = "/home/javier/Documents/dev/pythoninstaller/pythoninstaller/config/system.json"

with open(file_path) as f:

    osystemdata = json.load(f)
    osdata = osystemdata['ossystem'][1]["osname"]
    print(osdata)
    #second_os = osdata[1]["osname"]
    #print(second_os)

