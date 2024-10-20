#core pkgs
import streamlit as st
import streamlit.components.v1 as stc

# EDA
import pandas as pd

# plot
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import altair as alt

# NLP pkgs
import neattext.functions as nfx
from wordcloud import WordCloud
from collections import Counter
from textblob import TextBlob

#tags
from TAGS import TAGS
            # working fxns
#column 1
def get_pos_tags(docx):
    blob = TextBlob(docx)
    tagged_docx = blob.tags
    tagged_df = pd.DataFrame(tagged_docx,columns=['tokens','tags'])
    return tagged_df

def my_tag_visualizer(tagged_docx):
    colored_text = []
    for i in tagged_docx:
        if i[1] in TAGS.keys():
            token = i[0]
            color_for_tag = TAGS.get(i[1])
            result = f'<span style="color:{color_for_tag}">{token}</span>'
            colored_text.append(result)
    result = ' '.join(colored_text)
    print(result)
    return result
            

def plotWordFreq(docx,num):
    word_freq = Counter(docx.split())
    most_common_tokens = word_freq.most_common(num)
    st.info('matplotlib')
    x,y = zip(*most_common_tokens)
    fig = plt.figure()
    plt.bar(x,y)
    st.pyplot(fig)

    st.info('altair')
    plotWordFreqWithAltair(docx,num)
    
def plotWordFreqWithAltair(docx,num):
    word_freq = Counter(docx.split())
    most_common_tokens = dict(word_freq.most_common(num))

    word_freq_df = pd.DataFrame({'tokens':most_common_tokens.keys(),'counts':most_common_tokens.values()})
    brush = alt.selection(type='interval',encodings=['x'])

    c = alt.Chart(word_freq_df).mark_bar().encode(
        x='tokens',
        y='counts',
        ).add_selection(brush)

    st.altair_chart(c,use_container_width=True)


#column 2
def processTextFxn(docx):
    processed_text = nfx.remove_stopwords(docx)
    st.write(processed_text)


def plotWordCloud(docx):
    # create wordclud from our text
    myWordCloud = WordCloud().generate(docx)
    
    #putting the plot into a figure
    fig = plt.figure()
    plt.imshow(myWordCloud,interpolation='bilinear')

    plt.axis('off') # to turn off the labelling/names_and_value of X and Y axis
    st.pyplot(fig)


def plotStylometryCurve(docx):
    word_length = [len(token) for token in docx.split()]
    word_length_count = Counter(word_length)
    sorted_word_length_count = sorted(dict(word_length_count).items())

    x,y = zip(*sorted_word_length_count)
    mendelhall_df = pd.DataFrame({'tokens':x,'counts':y})
    st.line_chart(mendelhall_df['counts'])


# structural fxn
def layoutApp(raw_text,num_of_most_common):
    col1,col2 = st.columns(2)
    with col1:
        with st.expander('Original Text'):
            st.write(raw_text)

        with st.expander('PoS Tagged Text'):
            # tagged_docx = get_pos_tags(raw_text)
            # st.dataframe(tagged_docx)
            tagged_docx = TextBlob(raw_text).tags
            processed_tags = my_tag_visualizer(tagged_docx)
            stc.html(processed_tags,scrolling=True)

        with st.expander('Plot Word Freq'):
            plotWordFreq(raw_text,num_of_most_common)
    
    with col2:
        with st.expander('Processed Text'):
            processTextFxn(raw_text)

        with st.expander('Plot WordCloud'):
            plotWordCloud(raw_text)

        with st.expander('Plot Mendelhall Curve'):
            plotStylometryCurve(raw_text)

#main fxn
def textAnalysis(raw_text,num_of_most_common):
    layoutApp(raw_text,num_of_most_common)


if __name__ == '__main__':
    main()