import streamlit as st
import qrcode as qr

st.title('QRコード作成アプリ')

url = st.text_input('URLを入力してください。')

img = qr.make(url)
img.save('img.png')

if st.button('決定'):
  st.image('img.png',use_column_width=True)








