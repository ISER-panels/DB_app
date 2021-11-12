# title: main.py
# data 2021/07/14
# email: ryomyself@gmail.com
# written by Ryo Mikami

# import 
import streamlit as st
import os
import numpy as np
import pandas as pd
from PIL  import Image 
#pip freeze| grep numpy

#生データの読み込み
data_url="https://github.com/RyoMikami/JHPS_CPS_streamlit/raw/master/db.xlsx"
data=pd.read_excel(data_url, dtype=object,sheet_name=None, na_values=(''),header=0)
sheet_name=data.keys()


# title
st.title("JHPS_CPS ver1.0")


# sentence
"""
このページでは「くらしの好みと満足度についてアンケート」で提供されるデータセットの説明を行っています。
データを利用・分析する際にご活用ください。

左のメニューから質問内容を検索できます。
"""

# progress bar (ただの飾り)
latest_iteration=st.empty()
bar = st.progress(0.0)
for i in range(0,100):
    latest_iteration.text(f'{(i+1)} %')
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


# text=st.sidebar.text_input("問題文を検索")

option3 = st.sidebar.selectbox(
    "問題番号",
    list(data_option2["問題番号"].unique())
)
data_option3=data_option2[data_option2["問題番号"]==option3]




st.sidebar.write("------問題文詳細-------")


option4 = st.sidebar.selectbox(
    "詳細1",
    [i if i is not np.nan else ""  for i in list(data_option3["問題文2"].unique())] 
)
if option4!="":
    data_option4=data_option3[data_option3["問題文2"]==option4]
else:
    tmp=[ True if i is np.nan else False  for i in data_option3["問題文3"] ]
    data_option4=data_option3[tmp]


option5 = st.sidebar.selectbox(
    "詳細2",
    [i if i is not np.nan else ""  for i in list(data_option4["問題文3"].unique())] 
)
if option5!="":
    data_option5=data_option4[data_option4["問題文3"]==option5]
else:
    tmp=[ True if i is np.nan else False  for i in data_option4["問題文3"] ]
    data_option5=data_option4[tmp]


############

########### display


# text for option 1
"大問区分"
tmp_path="Text/"+option1+".txt"
f= open(tmp_path,"r")
text_option1=f.read()
f=f.close
expander_option1=st.beta_expander(option1)
expander_option1.write(text_option1)


# text for option2
"小問区分"
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
"""


-------------------------------- 検索結果 --------------------------------
"""
st.write("   ")


'問題番号',option3
# sentence 1

sentence1='\n\n'.join(data_option3.at[data_option3.index[0],"問題文"].splitlines())
sentence1


sentence2=""
if option4!=None:
    sentence2='\n\n'.join(option4.splitlines()) 
    sentence2_list=""
    for i in  list(data_option3["問題文2"].unique()):
        sentence2_list+="```\n"+str(i)+"\n"+"```\n"
    
expander_sentence2=st.beta_expander("")
expander_sentence2.write(sentence2_list) 
sentence2

sentence3=""
if option5!=None:
    sentence3='\n\n'.join(option5.splitlines())
    sentence3_list=""
    for i in  list(data_option3["問題文3"].unique()):
        sentence3_list+="```\n"+str(i)+"\n"+"```\n"
    

expander_sentence3=st.beta_expander("")
expander_sentence3.write("") 
sentence3

target= ' '.join(list(data_option5["質問対象者"].unique()))
expander_target=st.beta_expander("質問対象者")
expander_target.write(target)


choise=""
for i in data_option5.index:
    choise+=str( data_option5.at[i,"選択肢"])+str('\n\n')

expander_choise=st.beta_expander("選択肢")
expander_choise.write(choise)





# Question table
tmp=['年' in i for i in list(data_option5.columns) ]
Year_row=list(data_option5.columns[tmp])
target_row=["選択肢"]+Year_row
Question=data_option5[target_row].fillna("")
row_names=[ i[1:]  for i in Year_row ]  
Question.columns=["選択肢"]+row_names
expander_option3=st.beta_expander("実施年度")
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
