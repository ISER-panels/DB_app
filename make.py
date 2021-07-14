import os
import numpy as np
import pandas as pd


data_url="https://github.com/RyoMikami/JHPS_CPS_streamlit/raw/master/Data.xlsx"
data=pd.read_excel(data_url, dtype=object,sheet_name=None, na_values=(''),header=0)
sheet_name=data.keys()


for daimon in sheet_name:
    Daimon=data[daimon]
    Daimon=Daimon[~Daimon.duplicated("問題番号")]
    for syoumon in list(set(Daimon["小問区分"])) :
        tmp=Daimon[Daimon["小問区分"]==syoumon]
        new_dir_path = "Text/"+daimon+"/"+syoumon
        shutil.rmtree(new_dir_path) # txtフォルダをクリア
        os.mkdir(new_dir_path)
        new_dir_path=new_dir_path+"/"+syoumon+".txt"
        f = open(new_dir_path, 'a', encoding='UTF-8')

        for i in tmp.index:
            print('''
            
            
            ''', file=f)
            print(str("問題番号")+str(tmp.loc[i]["問題番号"])+str(' : \n'), file=f)
            print("```\n  ", file=f)
            print('\n\n'.join(tmp.loc[i]["問題文"].splitlines())+str('\n'), file=f)
            print("```\n  ", file=f)

        f.close()
