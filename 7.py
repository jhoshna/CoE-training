import streamlit as st
basic=st.number_input("enter a number",min_value=100,max_value=50000,step=1)
hra=0
da=0
if st.button("calculate"):

    if basic < 10000:
        hra = (67 / basic)*10
        da = (73 / basic)*100
    elif basic < 20000:
        hra = (69 / basic)*100
        da = (76 / basic)*100
    else:
        hra = (73/basic)*100
        da = (89/basic)*100
gs = hra + da + basic
#st.success(gs)
st.write(":blue[gross salary]:", gs)

