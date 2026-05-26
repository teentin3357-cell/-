import random
import streamlit as st
if st.button("숫자 뽑기", type="primary"):
 random_numbers = random.sample(range(1, 101), 5)
 random_numbers.sort()
 st.success("🎉 추출된 숫자입니다!")
 cols = st.columns(5)
 for i, num in enumerate(random_numbers):
 cols[i].metric(label=f"{i+1}번째 숫자", value=num)
