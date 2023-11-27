import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st

# Configure the Streamlit page
st.set_page_config(page_title='Insights', layout="wide", page_icon="📈")

# Add a title
st.title("Movie Revenue Data Insights with Tableau")

dashboard = """

<div class='tableauPlaceholder' id='viz1701024276246' style='position: relative'>
    <noscript>
        <a href='#'><img alt='Movie Revenue ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;CS&#47;CSE_6242_Movie_Revenue&#47;MovieRevenue&#47;1_rss.png' style='border: none' /></a>
    </noscript>
    <object class='tableauViz'  style='display:none;'>
        <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
        <param name='embed_code_version' value='3' /> 
        <param name='site_root' value='' />
        <param name='name' value='CSE_6242_Movie_Revenue&#47;MovieRevenue' />
        <param name='tabs' value='no' />
        <param name='toolbar' value='yes' />
        <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;CS&#47;CSE_6242_Movie_Revenue&#47;MovieRevenue&#47;1.png' /> 
        <param name='animate_transition' value='yes' />
        <param name='display_static_image' value='yes' />
        <param name='display_spinner' value='yes' />
        <param name='display_overlay' value='yes' />
        <param name='display_count' value='yes' />
        <param name='language' value='en-US' />
        </object>
</div>

<script type='text/javascript'>
    var divElement = document.getElementById('viz1701024276246');
    var vizElement = divElement.getElementsByTagName('object')[0];
    if ( divElement.offsetWidth > 800 ) { 
        vizElement.style.width='1600px';
        vizElement.style.height='927px';
    } else if ( divElement.offsetWidth > 500 ) { 
        vizElement.style.width='1600px';
        vizElement.style.height='927px';
    } else { 
        vizElement.style.width='100%';
        vizElement.style.height='2627px';
    }
    var scriptElement = document.createElement('script');
    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

"""

st.components.v1.html(dashboard, height=800, scrolling=True)