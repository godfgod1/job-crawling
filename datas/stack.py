# from common import call_html
from bs4 import BeautifulSoup
import requests

STACK_URL = 'https://stackoverflow.com/'

def load_last_pages(soup):
    pages = soup.find("div",{"class":"s-pagination"}).find_all('a',{"class":"s-pagination--item"})
    # print(pages)
    last_page = pages[-3].get_text(strip=True)
    return int(last_page) + 1
 

def get_jobs(url,pages):
    # n = 0
    job_info = {}
    jobs_info = []
    
    for page in range(pages):
        if page == 0:
            continue
        else:
            print(f'scrapping page {page}')
            page = f'{url}&r=true&pg={page}'
        
            req = requests.get(page)        
            soup = BeautifulSoup(req.text,'html.parser')
            jobs = soup.find_all("div", {"class":"-job"})

            for job in jobs:
                title = job.find('h2').find('a')['title']
                company = job.find('h3').find('span').get_text(strip=True)
                apply = job.find('h2').find('a')['href']
                apply = f'{STACK_URL}{apply}'
                job_info = {'title':title,'company':company,'apply':apply}
                jobs_info.append(job_info) 
            # print(jobs_info)
    return jobs_info
            # for job in jobs:

def export_jobs(word):
    SEARCH_URL = f'https://stackoverflow.com/jobs?r=true&q={word}'
    req = requests.get(SEARCH_URL)
    soup = BeautifulSoup(req.text,'html.parser')
    last_pages = load_last_pages(soup)
    jobs = get_jobs(SEARCH_URL,last_pages)
    # print(jobs)
    return  jobs





