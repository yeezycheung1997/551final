import os


def createFolder(job_title: str) -> None:
    title_folder = r"{}\{}".format(os.getcwd(), job_title)
    if not os.path.exists(title_folder):
        os.makedirs(title_folder)
        print("{} is created".format(title_folder))
        os.makedirs(r"{}\{}-Ads".format(title_folder, job_title))
        os.makedirs(r"{}\{}-Pages".format(title_folder, job_title))
    else:
        print("{} is existed".format(title_folder))


if __name__ == '__main__':
    job_title_list = ["Data Engineer", "Data Scientist", "Software Engineer"]
    for title in job_title_list:
        createFolder(title)
