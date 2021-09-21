from bs4 import BeautifulSoup
import requests


def get_jobs(soup):
    table = soup.find('table',{'id':'jobsboard'})
    lists = table.find_all('tr',{'class':'job'})
    REMOTE_URL = 'https://remoteok.io'
    jobs_info =[]
    print('scrapping page 1 in remoteok')
    for li in lists:
        title = li.find('h2').string
        company = li.find('h3').string
        apply = li.find('a',{'class':'preventLink'})['href']
        apply = REMOTE_URL+apply
        jobs_info.append({'title':title,'company':company,'apply':apply,'from':'Remoteok'})
    return jobs_info


def export_remote_jobs(word):
    # word = 'python'
    SEARCH_URL = f"https://remoteok.io/remote-dev+{word}-jobs?hide_sticky=&compact_mode=true&location=anywhere"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',}
    r = requests.post(SEARCH_URL, headers=headers)
    r.raise_for_status()
    soup = BeautifulSoup(r.text,'html.parser')
    get_remote_jobs = get_jobs(soup)
    return get_remote_jobs

# export_remote_jobs('javascript')