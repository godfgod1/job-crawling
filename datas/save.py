import csv

def save_file(jobs):
    file = open('jobs.csv',mode='w')
    writer = csv.writer(file)
    writer.writerow(['name','company','apply'])
    for job in jobs:
        writer.writerow(list(job.values()))
    return


