import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


# Process whole documents
text = ("""Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals. 
Leading AI textbooks define the field as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals. 
Colloquially, the term "artificial intelligence" is often used to describe machines (or computers) that mimic "cognitive" functions that humans associate with the human mind, such as "learning" and "problem-solving".
As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect. 
A quip in Tesler's Theorem says "AI is whatever hasn't been done yet." 
For instance, optical character recognition is frequently excluded from things considered to be AI, having become a routine technology.
Modern machine capabilities generally classified as AI include successfully understanding human speech, competing at the highest level in strategic game systems (such as chess and Go), autonomously operating cars, and intelligent routing in content delivery networks and military simulations.
Artificial intelligence was founded as an academic discipline in 1956, and in the years since has experienced several waves of optimism, followed by disappointment and the loss of funding (known as an "AI winter"), followed by new approaches, success, and renewed funding.""")

def summarizer(rawdocs):
    stop_words = list(STOP_WORDS)


    stop_words=list(STOP_WORDS)
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(rawdocs)

    tokens=[token.text for token in doc]
    #print(tokens)
    word_freq={}
    for word in doc:
        if word.text.lower() not in stop_words and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text]=1
            else:
                word_freq[word.text]+=1
    #print(word_freq)
    max_word_freq=max(word_freq.values())     
    for word in word_freq.keys():
        word_freq[word]=word_freq[word]/max_word_freq

    #sent_tokens=[sent for sent in doc]
    sent_tokens = list(doc.sents)
    #print(sent_tokens)
    sent_scores={}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent]=word_freq[word.text]
                else:
                    sent_scores[sent]+=word_freq[word.text]
    # print(sent_scores)
    select_len=int(len(sent_tokens)*0.3)
    summary=nlargest(select_len,sent_scores,key=sent_scores.get)
    #print(summary)
    final_summary=[word.text for word in summary]
    summary=' '.join(final_summary)

    return summary,doc,len(rawdocs.split(' ')),len(summary.split(' '))