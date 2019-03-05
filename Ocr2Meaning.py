import requests
import json


def ocr_space_file(filename, overlay=False, api_key='<Your_api_key>', language='eng'):
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    return r.content.decode()


def ocr_space_url(url, overlay=False, api_key='<Your_api_key>', language='eng'):
    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    return r.content.decode()

test_file = ocr_space_file(filename='6.png', language='eng')
to_json = json.loads(test_file)
k = to_json['ParsedResults'][0]['ParsedText']
print("The extracted text is:")
print(k)




app_id = '<Your_app_id>'
app_key = '<Your_api_key>'

language = 'en'
word_id = k

url = "	https://od-api.oxforddictionaries.com:443/api/v1/entries/" + language + '/' + word_id.lower()
json_data = requests.get(url, headers={'app_id': app_id, 'app_key': app_key}).json()
definitions = json_data["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["definitions"]
print("The meaning of this extracted text is")
print(definitions)