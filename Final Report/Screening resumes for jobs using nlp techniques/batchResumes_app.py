from operator import index
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
import spacy
import streamlit as st
from PIL import Image
from wordcloud import WordCloud
from fileReader import *

import Similar

nlp = spacy.load("en_core_web_md")

columns = ["Name", "Context", "Cleaned", "Selective", "Selective_Reduced", "TF_Based"]
resumesContent = read_files(resume_names, resume_dir)
Doc = get_cleaned_words(resumesContent)
Database = pd.DataFrame(Doc, columns=columns)
Database.to_csv("Resume_Data.csv", index=False)

jobDescriptionContent = read_files(job_description_names, job_desc_dir)
Jd = get_cleaned_words(jobDescriptionContent)
jd_database = pd.DataFrame(Jd, columns=columns)
jd_database.to_csv("Job_Data.csv", index=False)

image = Image.open('Images//logo.png')
st.image(image, use_column_width=True)

st.title("Resume Matcher")

# Reading the CSV files prepared by the fileReader.py
Resumes = pd.read_csv('Resume_Data.csv')
Jobs = pd.read_csv('Job_Data.csv')

# ############################## JOB DESCRIPTION CODE ######################################
# Checking for Multiple Job Descriptions
# If more than one Job Descriptions are available, it asks user to select one as well.
if len(Jobs['Name']) <= 1:
    st.write("There is only 1 Job Description present. It will be used to create scores.")
else:
    st.write("There are ", len(Jobs['Name']), "Job Descriptions available. Please select one.")

# Asking to Print the JD
if len(Jobs['Name']) > 1:
    option_yn = st.selectbox("Show the Job Description Names?", options=['YES', 'NO'])
    if option_yn == 'YES':
        index = [a for a in range(len(Jobs['Name']))]
        fig = go.Figure(data=[go.Table(header=dict(values=["Job No.", "Job Desc. Name"], line_color='darkslategray',
                                                   fill_color='#8ec3eb', font=dict(color='black', family="Source Sans Pro", size=20)),
                                       cells=dict(values=[index, Jobs['Name']], line_color='darkslategray',
                                                  fill_color='#2a6592'))
                              ])
        fig.update_layout(width=700, height=400)
        st.write(fig)

# Asking to choose the Job Description
index = st.slider("Which JD to select ? : ", 0, len(Jobs['Name']) - 1, 1)
option_yn = st.selectbox("Show the Job Description ?", options=['YES', 'NO'])
if option_yn == 'YES':
    st.markdown("---")
    st.markdown("### Job Description")
    fig = go.Figure(data=[go.Table(
        header=dict(values=["Job Description"],
                    fill_color='#f0a500',
                    align='center', font=dict(color='white', size=16)),
        cells=dict(values=[Jobs['Context'][index]],
                   fill_color='#f4f4f4',
                   align='left',
                   font=dict(color='black')))])

    fig.update_layout(width=800, height=500)
    st.write(fig)
    st.markdown("---")


# # ################################### SCORE CALCUATION ################################
@st.cache()
def calculate_scores(resumes, job_description):
    scores = []
    for x in range(resumes.shape[0]):
        score = Similar.match(resumes['TF_Based'][x], job_description['TF_Based'][index])
        scores.append(score)
    return scores


Resumes['Scores'] = calculate_scores(Resumes, Jobs)
Ranked_resumes = Resumes.sort_values(by=['Scores'], ascending=False).reset_index(drop=True)
Ranked_resumes['Rank'] = pd.DataFrame([i for i in range(1, len(Ranked_resumes['Scores']) + 1)])

# ##################################### SCORE TABLE PLOT ####################################
fig1 = go.Figure(data=[go.Table(
    header=dict(values=["Rank", "Name", "Scores"],
                fill_color='#00416d',
                align='center', font=dict(color='white', size=16)),
    cells=dict(values=[Ranked_resumes.Rank, Ranked_resumes.Name, Ranked_resumes.Scores],
               fill_color='#d6e0f0',
               align='left',
               font=dict(color='black')))])

fig1.update_layout(title="Top Ranked Resumes", width=700, height=700)
st.write(fig1)

st.markdown("---")


option_2 = st.selectbox("Show the Best Matching Resumes?", options=['YES', 'NO'])
if option_2 == 'YES':
    indx = st.slider("Which resume to display ?:", 1, Ranked_resumes.shape[0], 1)

    st.write("Displaying Resume with Rank: ", indx)
    st.markdown("---")
    st.markdown("## **Resume** ")
    value = Ranked_resumes.iloc[indx - 1, 2]
    st.markdown("#### The Word Cloud For the Resume")
    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          colormap='viridis', collocations=False,
                          min_font_size=10).generate(value)
    plt.figure(figsize=(7, 7), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    st.pyplot(plt)

    st.write("With a Match Score of :", Ranked_resumes.iloc[indx - 1, 6])
    fig = go.Figure(data=[go.Table(
        header=dict(values=["Resume"],
                    fill_color='#f0a500',
                    align='center', font=dict(color='white', size=16)),
        cells=dict(values=[str(value)],
                   fill_color='#f4f4f4',
                   align='left',
                   font=dict(color='black')))])

    fig.update_layout(width=800, height=1200)
    st.write(fig)
    st.markdown("---")
