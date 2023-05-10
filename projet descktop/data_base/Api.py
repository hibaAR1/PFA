import requests
from PIL import Image
import random
def getLink(query):
    r = requests.get("https://api.qwant.com/v3/search/images",
                     params={
                         'count': 21,
                         'q': query,
                         't': 'images',
                         'safesearch': 1,
                         'locale': 'en_US',
                         'offset': 0,
                         'device': 'desktop'
                     },
                     headers={
                         'User-Agent': 'Mozilla/5.0'
                     }
                     )

    response = r.json().get('data').get('result').get('items')
    urls = [r.get('media') for r in response]
    return urls[random.randint(0, 20)]

def getImage(query,i):
    try:
        with open('media/'+query.replace(' ','_')+str(i)+'.png', 'wb') as handle:
            response = requests.get(getLink(query), stream=True)
            if not response.ok:
                print(response)
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)
        image = Image.open('media/'+query.replace(' ','_')+str(i)+'.png')
        new_image = image.resize((200, 200))
        new_image.save('media/'+query.replace(' ','_')+str(i)+'.png')
    except:
        pass
