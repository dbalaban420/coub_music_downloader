import requests
import sys
import os
import json
from bs4 import BeautifulSoup

try:
    url = sys.argv[1]
except Exception:
    os._exit(0)

try:
    music_name = sys.argv[2]
except Exception:
    music_name = sys.argv[1].split('/')[-1]

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
coubPageCoubJson = soup.find(id = "coubPageCoubJson")
coubPageCoubJson = str(coubPageCoubJson).split('>')[1]
coubPageCoubJson = coubPageCoubJson.split('<')[0]

json_ = json.loads(coubPageCoubJson)
music_url = json_["file_versions"]["html5"]["audio"]["high"]["url"]

if not os.path.isdir(os.path.dirname(sys.executable) + "\music"):
    os.mkdir(os.path.dirname(sys.executable) + "\music")

music = requests.get(music_url)
with open (fr"{os.path.dirname(sys.executable)}\music\{music_name}.mp3", "wb") as f:
    f.write(music.content)