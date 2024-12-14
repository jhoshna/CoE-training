import streamlit as st
project = st.number_input("project score", min_value=1)
internal = st.number_input("enter the internal score", min_value=1)
external = st.number_input("enter the external score", min_value=1)
if st.button("calculate"):
    if project >= 50 and internal >= 50 and external >= 50:
        p = (70 / 100)*project
        i = (10/100)*internal
        e = (20/100)*external
        total = p+i+e
        st.write(total)
        if total > 90:
            st.write("grade A")
        elif total > 80:
            st.write("grade B")
        else:
            st.write("grade c")

    elif internal < 50 and external < 50:
        st.write("you failed in both")
    elif internal < 50:
        st.write("you failed in internal")
    elif external < 50:
        st.write("you failed in external")

    else:
        st.write("you failed in project")