import os
import numpy as np
import pandas as pd


data_url="https://github.com/RyoMikami/JHPS_CPS_streamlit/raw/master/Data.xlsx"
data=pd.read_excel(data_url, dtype=object,sheet_name=None, na_values=(''),header=0)
sheet_name=data.keys()


###  txtファイル作成
for daimon in sheet_name:
    Daimon=data[daimon]
    for syoumon in list(set(Daimon["小問区分"])) :
        tmp=Daimon[Daimon["小問区分"]==syoumon]
        new_dir_path="Text/"+daimon+"/"+syoumon+".txt"
        f = open(new_dir_path, 'a', encoding='UTF-8')

        for i in tmp.index:
            print('''
            
            ''', file=f)
            print(str("問題番号")+str(tmp.loc[i]["問題番号"])+str('` :  '), file=f)
            print('\n\n'.join(tmp.loc[i]["問題文"].splitlines()), file=f)
        f.close()
