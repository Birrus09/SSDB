import requests

def scrape(map, dumpname, robots= True, modes = [0, 1, 0, 0], sizelimit = 20000000, wordslog = "AND", words = ["lorem", "ipsum"]):
    mapindex = 0
    with open(map, "r") as map:
        while True:
            url = map.readline().split()[0]
            res = requests.get(url)


            #do stuff

            mapindex += 1
            
