# import 
import streamlit as st
import numpy as np
import pandas as pd
from PIL  import Image
#pip freeze| grep numpy

#生データの読み込み
data_path = "Data_new_問題番号振り直し.xlsx"
data=pd.read_excel(data_path, dtype=object,sheet_name=None, na_values=(''),skipinitialspace=True,header=0)
sheet_name=data.keys()

data_url="https://github.com/RyoMikami/JHPS_CPS_streamlit/raw/master/Data_new_問題番号振り直し.xlsx"
# title
st.title("JHPS_CPS")

# sentence
"""
このページでは「くらしの好みと満足度についてアンケート」で提供されるデータセットの説明を行っています。
データを利用・分析する際の資料としてご活用ください。
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



#　side bar
st.sidebar.write("どのような質問をお探しですか？")

option1 = st.sidebar.selectbox(
    "大問区分",
    list(sheet_name)
)


text=st.sidebar.text_input("sasa")
condition=st.sidebar.slider("あなたの調子は",0,10,5)




"えらんだ",option1,"か"

# display
st.dataframe(data[option1])


"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```

"""





text

if st.checkbox("show image"):
    img=Image.open("image.png")
    st.image(img,caption="りんご",use_column_width=True)


left_column,right_column =st.beta_columns(2)
button=left_column.button("右に表示")

if button:
    right_column.write("ここは右")

expander1=st.beta_expander("問い合わせ1")
expander1.write("回答1")
expander2=st.beta_expander("問い合わせ2")
expander2.write("回答2")
expander3=st.beta_expander("問い合わせ3")
expander3.write("回答3")
