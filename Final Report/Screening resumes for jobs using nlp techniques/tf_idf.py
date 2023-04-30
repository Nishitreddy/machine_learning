from sklearn.feature_extraction.text import TfidfVectorizer


def do_tfidf(token):
    """
        this will convert the sentence into useful tokens
    """
    tfidf = TfidfVectorizer(max_df=0.05, min_df=0.002)
    tfidf.fit_transform(token)
    sentence = " ".join(tfidf.get_feature_names())
    return sentence
