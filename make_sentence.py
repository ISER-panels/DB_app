import os
import shutil
import numpy as np
import pandas as pd



data_url="https://github.com/JHPS-CPS/DB_app/raw/master/db.xlsx"
data=pd.read_excel(data_url, dtype=object,sheet_name=None, na_values=(''),header=0)
sheet_name=data.keys()


for daimon in sheet_name:    
    Daimon=data[daimon] # シートを呼び出し
    Daimon=Daimon[~Daimon.duplicated("問題番号")] # 問題番号ごとに
    for syoumon in list(set(Daimon["小問区分"])) :
        new_dir_path = "Text/"+daimon+"/"+syoumon
        shutil.rmtree(new_dir_path) # Textフォルダをクリア
        os.mkdir(new_dir_path) # 新規作成
        tmp=Daimon[Daimon["小問区分"]==syoumon] # 小問区分ごとに
        f = open(new_dir_path+"/"+syoumon+".txt", 'a', encoding='UTF-8')
        for i in tmp.index:
            print('''
            
            
            ''', file=f)
            print(str("問題番号")+str(tmp.loc[i]["問題番号"])+str(' : \n'), file=f)
            print("```\n  ", file=f)
            print('\n\n'.join(tmp.loc[i]["問題文"].splitlines())+str('\n'), file=f)
            print("```\n  ", file=f)

        f.close()
