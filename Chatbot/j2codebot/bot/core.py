import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from .talks import greetings_inputs, greetings_answers, small_talks
from .preprocessing import preprocessing_func, vectorizer, tfidf, df


# implement get_closest_sentence(query, tf_idf, vectorizer)
def get_closest_sentence(query, tfidf, vectorizer):
    query_tfidf = vectorizer.transform([preprocessing_func(query)]).toarray()
    sim = cosine_similarity(query_tfidf, tfidf)
    return sim.max(), sim.argmax()


def greetings(sentence, inputs, outputs):
    for word in sentence.split():
        if word.lower() in inputs:
            return outputs[np.random.randint(len(outputs))]


# implement the function CovidBot

def covidbot(query, tf_idf=tfidf, vectorizer=vectorizer, database=df):
    print('your query is: ', query)

    greet = greetings(query, greetings_inputs, greetings_answers)

    if(greet!=None):
        answer = greet
    elif query.lower()=="bye":
        answer = "Bye! Have a wonderful day!"
    else:
        sim, closest = get_closest_sentence(query, tf_idf, vectorizer)
        if sim > 0.1:
            answer = database["data"].iloc[closest]
        else:
            answer = small_talks[np.random.randint(len(small_talks))]
    print(answer)
    return answer
