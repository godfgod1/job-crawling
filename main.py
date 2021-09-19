"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

import requests
from bs4 import BeautifulSoup


STACK_URL = 'https://stackoverflow.com/jobs?r=true&q=python'
WEWORK_URL = 'https://weworkremotely.com/remote-jobs/search?term=python'
REMOTE_URL = 'https://remoteok.io/remote-python-jobs'

urls = [STACK_URL,WEWORK_URL,REMOTE_URL]



def call_html():
    req = requests.get(STACK_URL)
    soup = BeautifulSoup(req.text,'html.parser')
    return soup

call_html()    

