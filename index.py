

# STACK_URL = 'https://stackoverflow.com/jobs?r=true&q=python'
# WEWORK_URL = 'https://weworkremotely.com/remote-jobs/search?term=python'
# REMOTE_URL = 'https://remoteok.io/remote-python-jobs'

from  datas.wework import export_wework_jobs
from  datas.stack import export_stack_jobs
from  datas.remote import export_remote_jobs
# from save import save_file





def export_combine_jobs(word):
    whole_job_lists = []
    stack_jobs = export_stack_jobs(word)
    wework_jobs = export_wework_jobs(word)
    remote_jobs = export_remote_jobs(word)
    for stack_job in stack_jobs:
        whole_job_lists.append(stack_job)
    for wework_job in wework_jobs:
        whole_job_lists.append(wework_job)
    for remote_job in remote_jobs:
        whole_job_lists.append(remote_job)
    return whole_job_lists


# print(len(export_combine_jobs('python')))


