import streamlit as st
import pickle
from sklearn.feature_extraction.text import CountVectorizer as cv
model = pickle.load(open('spam123.pkl','rb'))
cv=pickle.load(open('vec123.pkl','rb'))


def main():
    st.title("Email Spam Classification Appilication")
    st.write("This is a Machine Learning appilication to classify Spam mails")
    st.subheader("Classification")
    user_input=st.text_area("Enter an email to classify",height=75
    )
    if st.button("classify"):
        if user_input:
            data=[user_input]
            print(data)
            vec=cv.transform(data).toarray()
            result=model.predict(vec)
            if result[0]==0:
                st.success("This is not a spam email")
            else:
                st.error("This is a Spam Email")
        else:
            st.write("Please enter an email to classify")
main()                        