import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
import streamlit as st

nlp = spacy.load('en_core_web_sm')
spacy_text_blob = SpacyTextBlob()
nlp.add_pipe(spacy_text_blob)

text = 'Today is an amazing day!'
doc = nlp(text)

print('Polarity:', round(doc._.sentiment.polarity, 2))
print('Subjectivity:', round(doc._.sentiment.subjectivity, 2))