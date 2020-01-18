# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 14:50:55 2020

@author: Grindelwald
"""

import requests
r = requests.post(
    "https://api.deepai.org/api/nsfw-detector",
    data={
        'image': 'https://gallery-of-nudes.com/wp-content/uploads/2019/03/Alece-03.jpg',
    },
    headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
)
print(r.json())
 