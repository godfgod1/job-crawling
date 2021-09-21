
from bs4 import BeautifulSoup
import requests

def load_last_pages(soup):
    pages = soup.find("div",{"class":"s-pagination"}).find_all('a',{"class":"s-pagination--item"})
    
    last_page = pages[-3].get_text(strip=True)
    # print(last_page)
    return int(last_page) 

def get_jobs(url,pages):
    # n = 0
    STACK_URL = 'https://stackoverflow.com/'

    job_info = {}
    jobs_info = []
    # print(url)
    for page in range(pages):
        print(f'scrapping page {page+1} in stack_overflow')
        # https://stackoverflow.com/jobs?q=python&r=true&pg=2

        page = f'{url}&pg={page+1}'
        # print(page)
        req = requests.get(page)        
        soup = BeautifulSoup(req.text,'html.parser')
        result = soup.find('div',{'class':'listResults'})
        jobs = result.find_all("div", {"class":"-job"})
        for job in jobs:
            title = job.find('h2').find('a')['title']
            company = job.find('h3').find('span').get_text(strip=True)
            apply = job.find('h2').find('a')['href']
            apply = STACK_URL+apply
            job_info = {'title':title,'company':company,'apply':apply,'from':'Stack-OverFlow'}
            jobs_info.append(job_info) 
        # print(jobs_info)
    return jobs_info
            

def export_stack_jobs(word):
    SEARCH_URL = f'https://stackoverflow.com/jobs?q={word}&r=true'
    req = requests.get(SEARCH_URL)
    soup = BeautifulSoup(req.text,'html.parser')
    last_pages = load_last_pages(soup)
    get_stack_jobs = get_jobs(SEARCH_URL,last_pages)
    
    return  get_stack_jobs


# print(len(export_stack_jobs()))


