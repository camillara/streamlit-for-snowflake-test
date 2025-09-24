import streamlit as st

st.title("Hierarchical Data Viewer")
st.header("this is a header")
st.subheader("subheader")
st.caption("caption")

st.write("this is write")
st.text("this is text")
st.code("v = variable()\nnanother_cal()", "phyton")
st.markdown("**bold**")
st.markdown("*italic*")
st.divider()

st.latex("...")

st.error("this is a error")
st.info("this is a info")
st.warning("this is a warning")
st.success("this is a success")

st.balloons()
st.snow()

