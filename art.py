# All art related functionality goes here. 

from typing import Final
import os
from dotenv import load_dotenv

import requests 
from bs4 import BeautifulSoup

import random
 
'''
Grab a random image url with the given tag
'''
def get_random_tag_image(tag : str) -> str:
    url = 'https://www.google.com/search?q={0}&tbm=isch'.format(tag)
    content = requests.get(url).content
    soup = BeautifulSoup(content, 'lxml')
    images = soup.findAll('img')

    image = random.choice(images).get('src')
    return image

if __name__ == "__main__":
    url = get_random_tag_image("RobiFly Honkai Star Rail")
    print(url)
