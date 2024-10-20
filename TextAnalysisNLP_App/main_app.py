#core pkgs
import streamlit as st

#app
from textAnalysisApp import textAnalysis



#fxns
def callTextAnalysisApp():
    raw_text = st.text_area("Enter Text Here")
    most_common_token = st.sidebar.number_input(label='Token Number',min_value=5,max_value=15)
    #submit button
    if st.button('Analyze'):

        if len(raw_text) >= 2:
            textAnalysis(raw_text,most_common_token)
            
        elif len(raw_text) == 1:
            st.warning('Insufficient Data')
        else:
            st.warning('Enter Text')

def main():
    st.title('text analysis app'.upper())
    choice = st.sidebar.selectbox("Menu",['Home','Text Analysis','About'])
    if choice == 'Home':
        st.subheader('Home')
    elif choice == 'Text Analysis':
        callTextAnalysisApp()
    else:
        st.subheader('About')

if __name__ == '__main__':
    main()