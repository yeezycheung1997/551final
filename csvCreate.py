import os
import re
import csv
from bs4 import BeautifulSoup

job = "Data Scientist"
csv_path = r'{}\{}\{}.csv'.format(os.getcwd(), job, job)
ads_list = os.listdir(r'{}\{}\{}-Ads'.format(os.getcwd(), job, job))


def createCsv():
    cnt = 0
    for index, ad in enumerate(ads_list):
        try:
            path = r'{}\{}\{}-Ads\{}'.format(os.getcwd(), job, job, ad)
            htmlFile = open(path, 'r', encoding='utf-8')
            htmlHandle = htmlFile.read()
            soup = BeautifulSoup(htmlHandle, 'lxml')
            job_text = soup.find("div", class_="jobsearch-jobDescriptionText").get_text()

            # remove obvious terms
            if job == "Data Engineer":
                job_text = re.sub('data eng[a-z]+', ' ', job_text, re.I)
            elif job == "Data Scientist":
                job_text = re.sub('data sci[a-z]+', ' ', job_text, re.I)
            elif job == "Software Engineer":
                job_text = re.sub('software eng[a-z]+', ' ', job_text, re.I)

            # write job_text into the csv files
            with open(csv_path, 'a+', newline='', encoding='utf-8')as f:
                f_csv = csv.writer(f)
                f_csv.writerow([job_text, job])
            print(index)
            cnt += 1
        except:
            print(ad)
            pass
        if cnt > 5000:
            break


if __name__ == '__main__':
    headers = ['text', 'job title']
    with open(csv_path, 'w', newline='')as f:
        f = csv.writer(f)
        f.writerow(headers)
    createCsv()
