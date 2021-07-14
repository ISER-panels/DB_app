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
data_url="https://github.com/RyoMikami/JHPS_CPS_streamlit/raw/master/Data20210714.xlsx"
data=pd.read_excel(data_url, dtype=object,sheet_name=None, na_values=(''),header=0)
sheet_name=data.keys()


# title
st.title("JHPS_CPS")


# sentence
"""
このページでは「くらしの好みと満足度についてアンケート」で提供されるデータセットの説明を行っています。
データを利用・分析する際にご活用ください。
"""

# progress bar
latest_iteration=st.empty()
bar = st.progress(0.0)
for i in range(100):
    latest_iteration.text(f'{i+1} %')
    bar.progress(i+1)
    # time.sleep(0.1)
latest_iteration.text('')
bar.progress(0.0)


########### side bar


st.sidebar.write("どのような質問をお探しですか？")

option1 = st.sidebar.selectbox(
    "大問区分",
    list(sheet_name)
)
data_option1=data[option1]


option2 = st.sidebar.selectbox(
    "小問区分",
    list(data_option1["小問区分"].unique())
)
data_option2=data_option1[data_option1["小問区分"]==option2]


text=st.sidebar.text_input("問題文を検索")

option3 = st.sidebar.selectbox(
    "問題番号",
    list(data_option2["問題番号"].unique())
)
data_option3=data_option2[data_option2["問題番号"]==option3]




st.sidebar.write("------問題文詳細-------")


option4 = st.sidebar.selectbox(
    "詳細1",
    list(data_option3[~data_option3["問題文2"].isnull()]["問題文2"].unique())
)
if option4!=None:
    data_option4=data_option3[data_option3["問題文2"]==option4]
else:
    data_option4=data_option3


option5 = st.sidebar.selectbox(
    "詳細2",
    list(data_option4["問題文3"].unique())
)
if option5!=None:
    data_option5=data_option4[data_option4["問題文3"]==option5]
else:
    data_option5=data_option4[data_option4["問題文3"]==None]

data_option4
data_option5
data_option4["問題文3"]


############

########### display

# text for option 1
tmp_path="Text/"+option1+".txt"
f= open(tmp_path,"r")
text_option1=f.read()
f=f.close
expander_option1=st.beta_expander(option1)
expander_option1.write(text_option1)


# text for option2
tmp_path="Text/"+option1+"/"+option2+".txt"
f= open(tmp_path,"r")
text_option2=f.read()
f=f.close
expander_option2=st.beta_expander(option2)
expander_option2.write(text_option2)


# text for option3
tmp_path="Text/"+option1+"/"+option2+"/"+option2+".txt"
f= open(tmp_path,"r")
text_option3=f.read()
f=f.close



"問題一覧"
expander_option3=st.beta_expander("表示する")
expander_option3.write(text_option3)

# display  sentence

st.write("   ")
'問題番号',option3
# sentence 1
data_option3.at[data_option3.index[0],"問題文"]

if option4!=None:
    option4
if option5!=None:
    option5

# expander_sentence2=st.beta_expander("詳細1")
# expander_sentence2.write(text_option3)

# expander_sentence3=st.beta_expander("詳細2")
# expander_sentence3.write(text_option3)



# # sentence 2
# if np.isnan( data_option4.at[data_option4.index[0],"問題文2"]):
#     sentence2=""
# else:
#     sentence2=data_option4.at[data_option4.index[0],"問題文2"]
# sentence2

# # sentence 3
# if np.isnan( data_option5.at[data_option5.index[0],"問題文3"]):
#     sentence3=""
# else:
#     sentence3=data_option5.at[data_option5.index[0],"問題文3"]
# sentence3



# Question table
Year=[2005,2006,2007,2008,2009,2010,2011,2012,2013,2016,2017,2018]
Year_row=["X"+str(year)+"年"  for year in Year]
Question=data_option3[Year_row].fillna("")
Question.columns=[str(year)+"年"  for year in Year]

expander_option3=st.beta_expander("該当する変数一覧")
expander_option3.write(Question)

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```

# """



# condition=st.sidebar.slider("あなたの調子は",0,10,5)

# text

# if st.checkbox("show image"):
#     img=Image.open("image.png")
#     st.image(img,caption="りんご",use_column_width=True)


# left_column,right_column =st.beta_columns(2)
# button=left_column.button("右に表示")

# if button:
#     right_column.write("ここは右")


# expander2=st.beta_expander("問い合わせ2")
# expander2.write("回答2")
# expander3=st.beta_expander("問い合わせ3")
# expander3.write("回答3")
