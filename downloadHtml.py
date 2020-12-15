import os
import time
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

requests.packages.urllib3.disable_warnings()

ua = UserAgent()

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}
session = requests.Session()

search_city = "Kirkland"

job_title = "Data Scientist"

cur_page = 1

job_abbreviation = "".join([i[0] for i in job_title.split(" ")])

folder1_path = r"{}\{}\{}-Pages".format(os.getcwd(), job_title, job_title)
folder2_path = r"{}\{}\{}-Ads".format(os.getcwd(), job_title, job_title)

end_flag = False

while not end_flag:
    index_page_name = "{job_abbreviation}-{search_city}-page{page}".format(
        job_abbreviation=job_abbreviation,
        search_city=search_city.replace(" ", "").lower(),
        page=cur_page)

    r = session.get(
        "https://www.indeed.com/jobs?q={job_title}&l={city_name}&radius=100&filter=0&start={page}".format(
            job_title=job_title.replace(" ", "+"),
            city_name=search_city.replace(" ", "+"),
            page=10 * (cur_page - 1)),
        headers=headers,
        verify=False)

    if r.status_code == 200:
        with open(r"{}\{}.html".format(folder1_path, index_page_name), "w", encoding="utf8") as f:
            f.write(r.text)

        dom = BeautifulSoup(r.text, 'html.parser')
        dom_list = dom.find_all('h2', class_="title")

        if "Next" not in str(dom.find('ul', class_="pagination-list").find_all("li")):
            end_flag = True

        job_url_lists = []
        for i in dom_list:
            tmp_url = i.find("a")["href"]
            if "/rc/clk" in tmp_url:
                job_url_lists.append("https://www.indeed.com/viewjob{}".format(tmp_url[7:]))
            else:
                job_url_lists.append("https://www.indeed.com{}".format(tmp_url))

    for index, url in enumerate(job_url_lists):
        r = session.get(url, headers={'user-agent': ua.random}, verify=False)
        if r.status_code == 200:
            with open(r"{}\{}-{}.html".format(folder2_path,
                                              index_page_name, index), "w",
                      encoding="utf8") as f:
                f.write(r.text)
        time.sleep(1)
    cur_page += 1
    time.sleep(30)
