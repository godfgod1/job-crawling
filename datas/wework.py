from bs4 import BeautifulSoup
import requests

WEWORK_URL = 'https://weworkremotely.com/remote-jobs/search?term=python'

def get_jobs(jobs):
    # print(jobs[0].find_all('a')[1]['href'][1:])
    jobs_info =[]
    for job in jobs:
        title = job.find('span',{'class':'title'}).string
        company = job.find('span',{'class':'company'}).string
        apply = job.find_all('a')[1]['href'][1:]
        jobs_info.append({'title':title,'company':company,'apply':apply})
        # print({'title':title,'company':company,'apply':apply})
    return jobs_info

def combine_parts(soup):
    jobs = []
    n =0
    section_list = soup.find_all('section',{'class':'jobs'})
    # print(len(section_list[2].find_all('li',{'class':'feature'})) == 0 )
    for section in section_list:
        job_lists = section.find('ul').find_all('li')
        job_lists = job_lists[:-1]
        n += 1
        print(f'scrapping part {n} in wework')
        for job_list in job_lists:
            jobs.append(job_list)
    return jobs

def export_wework_jobs(word):
    # word = 'javascript'
    SEARCH_URL = f'https://weworkremotely.com/remote-jobs/search?term={word}'
    req = requests.get(SEARCH_URL)
    soup = BeautifulSoup(req.text,'html.parser')
    jobs = combine_parts(soup)
    get_wework_jobs = get_jobs(jobs)
    # print(get_wework_jobs)
    return get_wework_jobs


