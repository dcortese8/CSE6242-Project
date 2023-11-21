import pandas as pd
import streamlit.components.v1 as components
import streamlit as st

# Configure the Streamlit page
st.set_page_config(page_title='Insights', layout="wide", page_icon="📈")

# Add a title
st.title("Movie Revenue Data Insights with Tableau")

# # Import your data
# df = pd.read_csv("data/cleaned_movies_NEW.csv")

# # Generate the HTML using Pygwalker
# pyg_html = pyg.walk(df, return_html=True)

# # Embed the generated HTML into the Streamlit app
# components.html(pyg_html, height=1000, scrolling=True)

dashboard = """
<div class='tableauPlaceholder' id='viz1700535101842' style='position: relative'>
    <noscript>
        <a href='#'>
            <img alt='Dashboard 1 ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;C2&#47;C2ZYQ6F5H&#47;1_rss.png' style='border: none' />
        </a>
    </noscript>
    <object class='tableauViz'  style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
        <param name='embed_code_version' value='3' /> 
        <param name='path' value='shared&#47;C2ZYQ6F5H' /> 
        <param name='toolbar' value='yes' />
        <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;C2&#47;C2ZYQ6F5H&#47;1.png' />
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='en-US' />
    </object>
</div>

<script type='text/javascript'>

var divElement = document.getElementById('viz1700535101842');
var vizElement = divElement.getElementsByTagName('object')[0];

if ( divElement.offsetWidth > 800 ) {
    vizElement.style.width='100%';
    vizElement.style.maxWidth='1850px';
    vizElement.style.height=(divElement.offsetWidth*0.75)+'px';vizElement.style.maxHeight='887px';
    }

else if ( divElement.offsetWidth > 500 ) {
    vizElement.style.width='100%';
    vizElement.style.maxWidth='1850px';
    vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
    vizElement.style.maxHeight='887px';
    } 

else {
    vizElement.style.width='100%';
    vizElement.style.height='1777px';
    }
    
var scriptElement = document.createElement('script');
scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
vizElement.parentNode.insertBefore(scriptElement, vizElement);

</script>
"""

st.components.v1.html(dashboard, height=800, scrolling=True)