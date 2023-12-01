import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(page_title='Home', layout="wide", page_icon="🏠")

st.title('Analyzing and Predicting Movie Theatrical Release Success')
st.divider()
st.markdown("""
Welcome! The goal of this dashboard is meant to provide movie directors and producers a tool to verify that the assets
they are using in their movie will extract the maximum amount of revenue after release. More specifically, it focuses 
on revenue adjust for inflation, due to the incorporation of movie revenue data across multiple decades. The user can
navigate through different pages on the left-hand pane. You can also read further to learn the functionality of each page.  
""")

st.header("Revenue Projection", divider="blue")
st.markdown("""
The first page provides the main functionality of this dashboard. Here, a user is able to input multiple features
regarding their movie production, such as budget, runtime, cast members, and genre. Pressing the "Predict Movie
Success" button will invoke a number of machine learning models to project the adjusted revenue using this information,
based on historical trends. While you are able to view the projection of all models at the same time at the bottom of the
screen, the dropdown box on the left-hand pane will allow the user to select a single model at a time to view the model's 
performance. It is worth noting based on these plots that these models, in general, underestimate adjusted 
revenue. In other words, there is a good chance that a movie will make more money than what is projected. More information 
on these models is described below.
\n
Once you enter your information and generate predictions, you can view additional information on how much better your
movie will perform over movies in the same genre categories. Note that these plots only generate if you provide genres
to the model!
""")

st.subheader("Linear Regression", divider="blue")
st.write("From Wikipedia: [Linear Regression](https://en.wikipedia.org/wiki/Linear_regression)")
st.markdown("""
"Linear regression is a linear approach for modelling a predictive relationship between a scalar response and one or more
explanatory variables (also known as dependent and independent variables), which are measured without error. The case of
one explanatory variable is called simple linear regression; for more than one, the process is called multiple linear
regression. This term is distinct from multivariate linear regression, where multiple correlated dependent variables are
predicted, rather than a single scalar variable."
""")

st.subheader("K-Nearest Neighbors Regression", divider="blue")
st.write("From Wikipedia: [KNN Regression](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm#:~:text=In%20k%2DNN%20regression%2C%20the,of%20that%20single%20nearest%20neighbor.)")
st.markdown("""
"In k-NN regression, the output is the property value for the object. This value is the average of the values of k nearest
neighbors. If k = 1, then the output is simply assigned to the value of that single nearest neighbor."
""")

st.subheader("Random Forest Regression", divider="blue")
st.write("From Wikipedia: [Random Forest](https://en.wikipedia.org/wiki/Random_forest)")
st.markdown("""
"Random forests or random decision forests is an ensemble learning method for classification, regression and other tasks
that operates by constructing a multitude of decision trees at training time. For classification tasks, the output of the
random forest is the class selected by most trees. For regression tasks, the mean or average prediction of the individual
trees is returned. Random decision forests correct for decision trees' habit of overfitting to their training set."
""")


st.subheader("Support Vector Regression", divider="blue")
st.write("From Wikipedia: [Support Vector Regression](https://en.wikipedia.org/wiki/Support_vector_machine#Regression)")
st.markdown("""
"The model produced by support vector classification (as described above) depends only on a subset of the training data,
because the cost function for building the model does not care about training points that lie beyond the margin. Analogously,
the model produced by SVR depends only on a subset of the training data, because the cost function for building the model
ignores any training data close to the model prediction."
""")


st.header("Insights", divider="green")
st.markdown("""
This page displays information and graphs about the historical data itself. The charts focus on adjusted revenue and how
it is distributed across other variables for each movie in the dataset. We recommend viewing this page in "Full Screen"
mode by selecting the option in the bottom right corner of the embedded dashboard (you can scroll left/right on this window).
""")

st.header("Topic Analysis", divider="orange")
st.markdown("""
The Topic Analysis page focuses on movie summaries in the historical data. More specifically, we use an algorithm called
Latent Dirichlet Allocation (LDA) to extract significant topics and keywords from the movie summaries. Having this capability
allows users to select a set of pre-made topics for input in the Revenue Projections Page. 

The left-hand pane allows you to select the number of topics to extract and visualize. Once a visualization is displayed, you
can hover your mouse over a topic to view the keywords most associated with that topic on the right-hand side.
""")
