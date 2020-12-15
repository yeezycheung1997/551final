## EE -551-WS Final Project

## Qianyi Zhang (CWID: 10455276)

[click me to zoom record link](https://stevens.zoom.us/rec/play/QI3jl1SXYF2go-rxcjTB1u3l_WM8z57TCjWHhNwJI5v_mfQPS5LDfjxZkuAf8PvoOlrfEcQ34ebgsYeY.0LcDfA8nKOdtLFFa?startTime=1608047139000)

### Project Introduction
Collect
* 5,000 Job Ads for Data Scientists

* 5,000 Job Ads for Software Engineers

* 5,000 Job Ads for Data Engineers

from Indeed.com.


Then extract the text from the html and create a csv with 1 Ad per line and 2 columns: <text>, <job title>

Train a classification model that can predict whether a given Ad is for a Data Scientist, Software Engineer or Data Engineer.
### Project Structure
```bash
/
│  classification.py
│  csvCreate.py
│  downloadHtml.py
│  folderCreat.py
│  README.md
│  __init__.py
│
├─csvFiles
│      Data Engineer.csv
│      Data Scientist.csv
│      Software Engineer.csv
│
├─test
│      test.py
│      __init__.py
```


### Instructions on how to run the scripts
#### 1. run `folderCreate.py`
`folderCreate.py` will create three folders. The created folders structure is as follows:
```
├─Data Engineer
│  ├─Data Engineer-Ads
│  └─Data Engineer-Pages
├─Data Scientist
│  ├─Data Scientist-Ads
│  └─Data Scientist-Pages
└─Software Engineer
    ├─Software Engineer-Ads
    └─Software Engineer-Pages
```
We have zipped this folder as `rawhtml.rar`.
#### 2. run `downloadHtml.py`
Please input **2** global variables: `search_city` (line 16) and `job_title` (line 18) first, then run `downloadHtml.py`. `downloadHtml.py` will download raw Ads' html file into the corresponding folder.

Sometimes the script will be blocked by Indeed.com.
If you continue to run the script, please update the global variable `cur_page` (line 20). For example the current global variables are:

``` Python
job_title = "Data Scientist"
search_city = "Kirkland"
```
Then you can get the lastest downloaded content at folder `Data Scientist/Data Scientist-Ads`:
```
DS-kirkland-page55-16.html // blocked here
DS-kirkland-page55-15.html
DS-kirkland-page55-14.html
DS-kirkland-page55-13.html
DS-kirkland-page55-12.html
```
1. please delete **all html files related to page55** at folder `Data Scientist/Data Scientist-Ads`  

2. Then please delete `DS-kirkland-page55.html` at folder `Data Scientist/Data Scientist-Pages`  
3. Update `cur_page = 55` to continue download again after a while.

#### 3. run `csvCreate.py`
Please input **1** global variable: `job` (line 5) first, then run `csvCreate.py`. `csvCreate.py` will create csv file.

#### 4. run `test/test.py`
`test.py` is for testing
```Python
if __name__ == '__main__':
    # 500 means ramdomly choose 500 rows from csv files as test set
    # There are 500 * 3 = 1500 rows in test set
    # There are 5000 * 3 - 1500 = 13500 rows in train set
    run(500)
```
the result is
```python
A total of 13499 data have been read
wrong counts: 207
wrong rate: 13.8%
accuracy  : 86.2%
```
