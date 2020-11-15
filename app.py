#call api for new image
import requests
import string
r = requests.get('https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US').json()

r_url ='https://bing.com' + r['images'][0]['url']
r_title = r['images'][0]['title'].translate(str.maketrans('', '', string.punctuation))

#save image with date as name
import os
if os.path.exists('C:/Users/Safin/Pictures/Wallpapers/Bing') == False:
    os.mkdir('C:/Users/Safin/Pictures/Wallpapers/Bing')

if os.path.exists('C:/Users/Safin/Pictures/Wallpapers/Bing/'+ r_title +'.jpg') == False:
    with open('C:/Users/Safin/Pictures/Wallpapers/Bing/'+ r_title +'.jpg', 'wb') as img:
        img.write(requests.get(r_url).content)

#get latest image
import glob

list_of_files = glob.glob('C:/Users/Safin/Pictures/Wallpapers/Bing/*')
latest_file = max(list_of_files, key=os.path.getctime)

#set wallpaper
import ctypes
ctypes.windll.user32.SystemParametersInfoW(20, 0, latest_file , 0)