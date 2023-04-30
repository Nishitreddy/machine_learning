import os

import textract as tx

import Cleaner
import tf_idf

resume_dir = "Data/Resumes/"
job_desc_dir = "Data/JobDesc/"
resume_names = os.listdir(resume_dir)
job_description_names = os.listdir(job_desc_dir)


def read_files(list_of_resumes, resume_directory):
    """
        this function is to read all the files in the give directory
    """
    placeholder = []
    for res in list_of_resumes:
        if res == ".DS_Store":
            continue
        temp = [res]
        text = tx.process(resume_directory + res, encoding='ascii')
        text = str(text, 'utf-8')
        temp.append(text)
        placeholder.append(temp)
    return placeholder


def read_file(resumeName, resume_directory):
    """
        this function is to read a given file in the give directory
    """
    placeholder = []
    temp = [resumeName]
    text = tx.process(resume_directory + resumeName, encoding='ascii')
    temp.append(str(text, 'utf-8'))
    placeholder.append(temp)
    return placeholder


def get_cleaned_words(document, tfidf=False):
    """
        this function is to preprocess the texts
    """
    for content in document:
        raw = Cleaner.Cleaner(content[1])
        for processed in raw:
            content.append(" ".join(processed))
        if tfidf:
            content.append(content[3])
        else:
            sentence = tf_idf.do_tfidf(content[3].split(" "))
            content.append(sentence)
    return document
