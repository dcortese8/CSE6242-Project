import streamlit as st
import pandas as pd
import numpy as np
import os

st.set_page_config(page_title='Home', layout="wide", page_icon="🏠")

st.title('Analyzing and Predicting Movie Theatrical Release Success')
st.divider()
st.text("""
Welcome! The goal of this dashboard is meant to provide movie directors and producers a tool to verify that the assets \n
they are using in their movie will extract the maximum amount of revenue after release. More specifically, it focuses \n
on revenue adjust for inflation, due to the incorporation of movie revenue data across multiple decades. The user can \n
navigate through different pages on the left-hand pane. You can also read further to learn the functionality of each page.  
""")

st.header("Revenue Projection", divider="blue")
st.text("""
The first page provides the main functionality of this dashboard. Here, a user is able to input multiple pieces of \n
in regards to their movie production, such as budget, runtime, cast members, and genre. Pressing the "Predict Movie \n
Success" button will invoke a number of machine learning models to project the adjusted revenue using this information \n
based on historical trends. While you are able to view the projection of all models at the same time at the bottom of the \n
screen, the dropdown box on the left-hand pane will allow the user to choose which model they would This plot provides \n
information on the model's performance on unseen like to view in plot that appears below the selection.data. It is worth \n
noting based on these plots that these models, in general, underestimate adjusted revenue. In other words, there is a good \n
chance that a movie will make more money than what is projected. More information on these models is described below.
\n
Once you enter your information and generate predictions, you can view additional information on how much better your \n
movie will perform over movies in the same genre categories. Note that these plots only generate if you provide genres \n
to the model!
""")

st.subheader("Linear Regression", divider="blue")
st.write("From Wikipedia: [Linear Regression](https://en.wikipedia.org/wiki/Linear_regression)")
st.text("""
"Linear regression is a linear approach for modelling a predictive relationship between a scalar response and one or more \n
explanatory variables (also known as dependent and independent variables), which are measured without error. The case of \n
one explanatory variable is called simple linear regression; for more than one, the process is called multiple linear \n
regression. This term is distinct from multivariate linear regression, where multiple correlated dependent variables are \n
predicted, rather than a single scalar variable."
""")

st.subheader("K-Nearest Neighbors Regression", divider="blue")
st.write("From Wikipedia: [KNN Regression](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm#:~:text=In%20k%2DNN%20regression%2C%20the,of%20that%20single%20nearest%20neighbor.)")
st.text("""
"In k-NN regression, the output is the property value for the object. This value is the average of the values of k nearest\n
neighbors. If k = 1, then the output is simply assigned to the value of that single nearest neighbor."
""")

st.subheader("Random Forest Regression", divider="blue")
st.write("From Wikipedia: [Random Forest](https://en.wikipedia.org/wiki/Random_forest)")
st.text("""
"Random forests or random decision forests is an ensemble learning method for classification, regression and other tasks \n
that operates by constructing a multitude of decision trees at training time. For classification tasks, the output of the \n
random forest is the class selected by most trees. For regression tasks, the mean or average prediction of the individual \n
trees is returned. Random decision forests correct for decision trees' habit of overfitting to their training set."
""")


st.header("Insights", divider="green")
st.text("""
This page displays information and graphs about the historical data itself. The charts focus on adjusted revenue and how \n
it is distributed across other variables for each movie in the dataset. We recommend viewing this page in "Full Screen" \n
mode by selecting the option in the bottom right corner of the embedded dashboard (you can scroll left/right on this window).
""")

st.header("Topic Analysis", divider="orange")
st.text("""
The Topic Analysis page focuses on movie summaries in the historical data. More specifically, we use an algorithm called \n
Latent Dirichlet Allocation (LDA) to extract significant topics and keywords from the movie summaries. Having this capability \n
allows users to select a set of pre-made topics for input in the Revenue Projections Page. 

The left-hand pane allows you to select the number of topics to extract and visualize. Once a visualization is displayed, you \n
can hover your mouse over a topic to view the keywords most associated with that topic on the right-hand side.
""")
