from ex20 import readData
import re
import mimetypes


def findURL(string):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', string)
    return urls

def getListURL():
    listURL = []
    listWiki = readData()

    for ele in listWiki:
        text = ele['text']
        # print(type(ele))
        listURL.extend(findURL(text))
    return listURL
    
def filterMedia():
    listURL = getListURL()
    for url in listURL:
        typeURL = mimetypes.MimeTypes().guess_type(url)[0]
        typetypeURL = type(typeURL)
        if (typetypeURL is str) and ('image' in typeURL): 
            print(typeURL, url)

def main():
    filterMedia()

if __name__ == "__main__":
    main()