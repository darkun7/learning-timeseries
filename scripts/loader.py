# The Dataset that loaded from the source is based on the book:
# Time Series Analysis Univariate and Multivariate Methods SECOND EDITION 
# William W. S. Wei

import pandas as pd
import requests

#  Source: https://sites.temple.edu/wwei/files/2020/08/data_sets-1.pdf
DATASETS = {
    'w1'   : 'https://sites.temple.edu/wwei/files/2020/08/W1.txt',
    'w2'   : 'https://sites.temple.edu/wwei/files/2020/08/W2.txt',
    'w3'   : 'https://sites.temple.edu/wwei/files/2020/08/W3.txt',
    'w4'   : 'https://sites.temple.edu/wwei/files/2020/08/W4.txt',
    'w5'   : 'https://sites.temple.edu/wwei/files/2020/08/W5.txt',
    'w6'   : 'https://sites.temple.edu/wwei/files/2020/08/W6.txt',
    'w7'   : 'https://sites.temple.edu/wwei/files/2020/08/W7.txt',
    'w8'   : 'https://sites.temple.edu/wwei/files/2020/08/W8.txt',
    'w9'   : 'https://sites.temple.edu/wwei/files/2020/08/W9.txt',
    'w10'  : 'https://sites.temple.edu/wwei/files/2020/08/W10.txt',
    'w11'  : 'https://sites.temple.edu/wwei/files/2020/08/W11.txt',
    'w12-1': 'https://sites.temple.edu/wwei/files/2020/08/W12-1.txt',
    'w12-2': 'https://sites.temple.edu/wwei/files/2020/08/W12-2.txt',
    'w13-1': 'https://sites.temple.edu/wwei/files/2020/08/W13-1.txt',
    'w13-2': 'https://sites.temple.edu/wwei/files/2020/08/W13-2.txt',
    'w13-3': 'https://sites.temple.edu/wwei/files/2020/08/W13-3.txt',
    'w14'  : 'https://sites.temple.edu/wwei/files/2020/08/W14.txt',
    'w15-1': 'https://sites.temple.edu/wwei/files/2020/08/W15-1.txt',
    'w15-2': 'https://sites.temple.edu/wwei/files/2020/08/W15-2.txt',
    'w16'  : 'https://sites.temple.edu/wwei/files/2020/08/W16.txt',
}


def loadDataset(url):
    f = requests.get(url)
    res = f.text
    return res

data = {}
for key in DATASETS:
    data[key] = []
    data_raw = loadDataset(DATASETS[key])
    print('⚠️ Processing data ➡️', key)
    for i in data_raw.split('\n'):
        if (len(i)>0):
            for j in i.split():
                data[key].append(float(j))

writer = pd.ExcelWriter('dataset_william.xlsx', engine='xlsxwriter')
for key in DATASETS:
    pd.DataFrame(data[key]).to_excel(writer,sheet_name=f'{key}', index=False, header=None)
writer.save()