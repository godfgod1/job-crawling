

# STACK_URL = 'https://stackoverflow.com/jobs?r=true&q=python'
# WEWORK_URL = 'https://weworkremotely.com/remote-jobs/search?term=python'
# REMOTE_URL = 'https://remoteok.io/remote-python-jobs'

from  datas.stack import  export_jobs
from datas.save import save_file





def make_csv():
    save_file(export_jobs())
    return

make_csv()




