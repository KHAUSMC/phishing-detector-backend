"""This code trains the logistic regression model using TF-IDF and saves it.
If a word appears a lot in one email, it might be important for that email → TF (Term Frequency)
But if that word appears in every email, it's probably not useful for telling emails apart → IDF (Inverse Document Frequency)
"""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Loading the dataset
df = pd.read_csv('emails.csv')

#Computer can't read english
vectorizer = TfidfVectorizer(stop_words='english')
# Transforms it into text, so that it's readable by the model
X = vectorizer.fit_transform(df['text'])
# access values
y = df['label']

# We start by training the model
model = LogisticRegression()
model.fit(X, y)

# Step 4: We save the model and vectorizer
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)

with open('vectorizer.pkl', 'wb') as vec_file:
    pickle.dump(vectorizer, vec_file)

print("✅ Model and vectorizer saved successfully!")
