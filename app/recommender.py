import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .utils import preprocess

class SHLRecommender:
    def __init__(self, catalog_path):
        """
        Initializes the recommender with the given SHL product catalog CSV.
        """
        self.df = pd.read_csv(catalog_path)
        self.df['processed'] = self.df['Tags'].apply(preprocess)
        self.vectorizer = TfidfVectorizer()
        self.embeddings = self.vectorizer.fit_transform(self.df['processed'])

    def recommend(self, job_description, top_n=3):
        """
        Recommends top_n SHL assessments based on job description.
        """
        desc = preprocess(job_description)
        desc_vector = self.vectorizer.transform([desc])
        similarities = cosine_similarity(desc_vector, self.embeddings).flatten()
        top_indices = similarities.argsort()[-top_n:][::-1]
        return self.df.iloc[top_indices][['AssessmentName', 'Description']]
