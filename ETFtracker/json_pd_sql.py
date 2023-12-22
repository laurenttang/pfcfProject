import json
import pandas as pd
#from glom import glom

# 爬回存放區
resource_path = r'./res_gossiping'

 
# Opening JSON file
with open(f'{resource_path}/output.json', 'r') as openfile:
    json_object = json.load(openfile)
 
# REF : https://towardsdatascience.com/how-to-convert-json-into-a-pandas-dataframe-100b2ae1e0d8


df_all =pd.read_json(f'{resource_path}/output.json')
print(df_all.size)

dd=pd.DataFrame()
# Normalizing data
for i in range(df_all.size):
    try:
        # print(i)
        df = pd.json_normalize(df_all['a1'].iloc[i], record_path =['msgArray'])
        dd=dd.append(df,ignore_index=True)
    except:
        pass

dd = dd.rename(columns={
    'a': 'ETF_no',
    'b': 'name',
    'c': 'issued_unit',
    'd': 'issue_diff',
    'e': 'price',
    
    'f': 'est_bv',
    'g': 'est_premium',
    'h': 'last_bv',
    'i': 'date',
    'j': 'time',
    
    'k': 'k'
})
# data cleansing

def transformer(x):
    if (type(x) == float) or (type(x) == int):
        tic=str(x).strip(',')

    else:
        tic=x.strip(',')
    return tic

from openfunction.timemodule import Str_to_time

dd['issued_unit']=dd['issued_unit'].apply(lambda x: transformer(x))
dd['k']=dd['date']+' '+dd['time']
dd['recordtime']=dd['k'].apply(lambda x: Str_to_time(x,'%Y%m%d %H:%M:%S'))
dd=dd.drop(['date','k'],axis=1)

from decouple import config
from sqlalchemy import create_engine
'''
use .gitignore ,then git will pass the files in .gitignore
use .env to set userID,password as default, to pass through config and save in Variables
'''
#for mysql db use
host = config('host',default='localhost')
user = config('user',default='root')
password = config('password',default='root')

'''
from sqlalchemy.types import NVARCHAR, Float, Integer
dtypedict = {
'ETF_no':NVARCHAR(length=255),
'name':NVARCHAR(length=255),
'issued_unit': NVARCHAR(length=255),
'issue_diff':NVARCHAR(length=255),
'price':Float(),
'est_bv':Float(),
'est_premium':NVARCHAR(length=255),
'last_bv':Float(),
'date':NVARCHAR(length=255),
'time':NVARCHAR(length=255),
'k': NVARCHAR(length=255),
'id':Integer()
}
'''
# To local db
engine2 = create_engine(f'mysql+pymysql://{user}:{password}@{host}:3306/strategy?charset=utf8')
dd.to_sql('etf_tracker', engine2, if_exists = 'append',index=False)
          #, dtype=dtypedict)
