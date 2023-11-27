import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
from pyLDAvis import gensim_models, save_html
from gensim.models import LdaModel
import gensim.corpora as corpora

# Configure the Streamlit page
st.set_page_config(page_title='Insights', layout="wide", page_icon="✏")

# Add a title
st.title("Topic Analysis of Movie Summaries")

data_words = []
with open('./data/cleaned_words.txt', 'r') as f:
    for line in f:
        line = line.strip('\n\r') 
        if line != '':
            data_words.append(line.split(","))

# Create Dictionary
id2word = corpora.Dictionary(data_words)

corpus = [id2word.doc2bow(text) for text in data_words]

st.sidebar.write('Select number of topics to extract')

num_topics = st.sidebar.selectbox("Topics:", options=list(range(2,10)))

bttn = st.sidebar.button('Extract Summary Topics')

if bttn:

    # Build LDA model
    lda_model = LdaModel(corpus=corpus,
                            id2word=id2word,
                            num_topics=num_topics)

    LDAvis_prepared = gensim_models.prepare(lda_model, corpus, id2word)
    save_html(LDAvis_prepared, './modeling_and_analysis/eda/ldavis_prepared.html')

    with open('./modeling_and_analysis/eda/ldavis_prepared.html', 'r') as f:
        html_string = f.read()
    components.html(html_string, width=1100, height=800, scrolling=True)
