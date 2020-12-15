import pandas as pd
from sklearn.svm import SVC
from nltk.corpus import stopwords
from sklearn.decomposition import TruncatedSVD
from sklearn.feature_extraction.text import TfidfVectorizer

STOPWORDS = set(stopwords.words('english'))
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_colwidth', 1000)


def run(path, df_new):
    df_new.dropna(axis=0, how="any", inplace=True)
    df_new.columns = ['text', 'jobT']

    print(f"A total of {len(df_new)} data have been read")

    test = pd.read_csv(path, header=None, encoding="utf-8", sep=",")

    x_train, y_train = df_new['text'], df_new['jobT']
    x_test = test[0]

    transformer = TfidfVectorizer(norm="l2", use_idf=True, stop_words=STOPWORDS)
    svd = TruncatedSVD(n_components=100)
    train_cut_text = list(x_train.astype("str"))

    transformer_model = transformer.fit(train_cut_text)

    df1 = transformer_model.transform(train_cut_text)
    svd_model = svd.fit(df1)
    df2 = svd_model.transform(df1)

    data = pd.DataFrame(df2)
    SVC_classifier = SVC(kernel='rbf', C=2)
    model = SVC_classifier.fit(data, y_train)

    cut_test = list(x_test.astype("str"))
    data_test = pd.DataFrame(svd_model.transform(transformer_model.transform(cut_test)))
    y_predict = model.predict(data_test)
    y_predict = pd.DataFrame(y_predict)
    y_predict.to_csv('./result.csv', index=False, header=False)


if __name__ == '__main__':
    df_SDE = pd.read_csv("./csvFiles/Software Engineer.csv", encoding="utf-8", sep=",")
    df_DE = pd.read_csv("./csvFiles/Data Engineer.csv", encoding="utf-8", sep=",")
    df_DS = pd.read_csv("./csvFiles/Data Scientist.csv", encoding="utf-8", sep=",")
    df_new = df_SDE.append(df_DE).append(df_DS)

    path = ""
    run(path, df_new)