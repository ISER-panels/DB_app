# title: main.py
# data 2021/07/14
# email: ryomyself@gmail.com
# written by Ryo Mikami

# import 
import os
import streamlit as st
import numpy as np
import pandas as pd
from PIL  import Image
#pip freeze| grep numpy

#生データの読み込み
data_url="https://github.com/RyoMikami/JHPS_CPS_streamlit/raw/master/db.xlsx"
data=pd.read_excel(data_url, dtype=object,sheet_name=None, na_values=(''),header=0)
sheet_name=data.keys()


# title
st.title("JHPS_CPS")
