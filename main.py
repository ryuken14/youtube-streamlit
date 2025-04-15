import streamlit as st
import time

st.title("streamlit 超入門")

st.write("プログレスバー")

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

"Done!!!!!"

left_column,right_column=st.columns(2)
button=left_column.button("右カラムに文字を表示")
if button:
    right_column.write("右カラムに文字表示します")

expander1=st.expander("問合せ1")
expander1.write("問合せ１の回答")
expander2=st.expander("問合せ2")
expander2.write("問合せ2の回答")
expander3=st.expander("問合せ3")
expander3.write("問合せ3の回答")
# tensu=st.slider('あなたの今の調子は',0,100,20)
# "私の今の調子は",tensu,"です"

# option=st.selectbox(
#     "Your favorites number?",
#     [1,2,3,4,5,6,7,8,9,10]
# )
# "あなたの好きな数字は",option,"です"

# if st.checkbox('Show Image'):
#     img=Image.open("cat.png")
#     st.image(img,caption='Masaki Okamura',use_container_width=True)