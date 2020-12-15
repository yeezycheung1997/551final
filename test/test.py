import csv
import random
import pandas as pd
from classification import run as cf_run


def getIndex(sum: int) -> list:
    """
    :param sum: Randomly select sum data in each csv file
    :return:  A list of indexes used in the test set
    """
    testIndex_list = random.sample(range(5000), sum)
    return testIndex_list


def getCsvList(path: str) -> list:
    """
    :param path: the csv file path
    :return: A list of contents of csv file, except csv header
    """
    with open(path, 'r', encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = [row for row in reader]
        return rows[1:]


def getDataSet(testIndex_list: list, rows: list) -> (list, list):
    """
    :param testIndex_list: A list of indexes used in the test set
    :param rows: A list of contents of csv file, except csv header
    :return: A train set and a test set
    """
    train_list, test_list = [], []
    for index, row in enumerate(rows):
        if index in testIndex_list:
            test_list.append(row)
        else:
            train_list.append(row)
    return train_list, test_list


def writeCsv(path, num) -> None:
    """
    :param path: the csv file path
    :param num: num data to choose as the test set
    :return:
    """
    rows = getCsvList(path)
    testIndex_list = getIndex(num)
    train_list, test_list = getDataSet(testIndex_list, rows)

    with open('./test1.csv', 'a+', newline='', encoding="utf-8") as f1:
        writer = csv.writer(f1)
        for row in test_list:
            writer.writerow(row)

    with open('./test2.csv', 'a+', newline='', encoding="utf-8") as f2:
        writer = csv.writer(f2)
        for row in [[i[0]] for i in test_list]:
            writer.writerow(row)

    with open('./train.csv', 'a+', newline='', encoding="utf-8") as f3:
        writer = csv.writer(f3)
        for row in train_list:
            writer.writerow(row)


def run(num):
    path_de = "../csvFiles/Data Engineer.csv"
    path_ds = "../csvFiles/Data Scientist.csv"
    path_se = "../csvFiles/Software Engineer.csv"

    writeCsv(path_de, num)
    writeCsv(path_ds, num)
    writeCsv(path_se, num)

    df_new = pd.read_csv("../test/train.csv", encoding="utf-8", sep=",")

    path = "./test1.csv"
    cf_run('./test2.csv', df_new)
    path2 = "./result.csv"

    with open(path, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        rows = [row[1] for row in reader]

    with open(path2, 'r', encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        results = [row[0] for row in reader]

    cnt = 0
    for i in range(len(rows)):
        if rows[i] != results[i]:
            cnt += 1
    print(f"wrong counts: {cnt}")
    wrong_rate = (cnt / len(rows)) * 100
    accuracy = 100 - wrong_rate
    print(f"wrong rate: {str(wrong_rate)[:5]}%")
    print(f"accuracy  : {str(accuracy)[:5]}%")


if __name__ == '__main__':
    run(500)
