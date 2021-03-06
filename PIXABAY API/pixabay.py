import json, requests, os
from dotenv import load_dotenv

load_dotenv()

# Insert your key on this variable 
apikey = os.environ.get("PIXABAY_KEY")


def downloadImg(keyWords,quantity=1):
    keyWords = keyWords.replace(" ","+")
    url="https://pixabay.com/api"
    params = {"key":apikey,"lang":"en","q":keyWords}

    r = requests.get(url=url,params=params)
    photos = [i["largeImageURL"] for i in r.json()["hits"]]    

    for i in range(quantity):
        print(i)
        img = requests.get(photos[i]).content

        
        with open(keyWords+str(i+1)+".jpg","wb") as handler:
            handler.write(img)
    print("Saved!")
    


def downloadVideo(keyWords,quantity=1,quality=4):
    videoSize = {1:"tiny",2:"small",3:"medium",4:"large"}
    quality = videoSize[quality]
    keyWords = keyWords.replace(" ","+")
    url="https://pixabay.com/api/videos/"
    params = {"key":apikey,"lang":"es","q":keyWords}

    r = requests.get(url=url,params=params)
    photos = [i["videos"][quality]["url"] for i in r.json()["hits"]]    
    
    for i in range(quantity):
        img = requests. get(photos[i]).content

        
        with open(keyWords+str(i+1)+".mp4","wb") as handler:
            handler.write(img)
    print("Saved!")
    

downloadVideo("pc",10)