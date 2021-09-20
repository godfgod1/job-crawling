

# STACK_URL = 'https://stackoverflow.com/jobs?r=true&q=python'
# WEWORK_URL = 'https://weworkremotely.com/remote-jobs/search?term=python'
# REMOTE_URL = 'https://remoteok.io/remote-python-jobs'

from  wework import export_wework_jobs
from  stack import export_stack_jobs
# from save import save_file





def export_combine_jobs(word):
    
    whole_job_lists = []
    stack_jobs = export_stack_jobs(word)
    export_wework_jobs = export_wework_jobs(word)
    # for stack_job in stack_jobs:
    #     whole_job_lists.append(stack_job)
    for wework_job in export_wework_jobs:
        whole_job_lists.append(wework_job)
    print(len(whole_job_lists))

word = 'javascript'
export_combine_jobs(word)




