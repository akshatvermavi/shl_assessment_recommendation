# from app.recommender import SHLRecommender

# def main():
#     catalog_path = "data/shl_product_catalog.csv"
#     recommender = SHLRecommender(catalog_path)
    
#     print("Welcome to SHL Assessment Recommender Engine!")
#     jd = input("Enter a job description or role: ")
#     recommendations = recommender.recommend(jd)
    
#     print("\nTop SHL Assessment Recommendations:\n")
#     print(recommendations.to_string(index=False))

# if __name__ == "__main__":
#     main()

from fastapi import FastAPI, Query
from app.recommender import SHLRecommender

app = FastAPI()
recommender = SHLRecommender("data/shl_product_catalog.csv")

@app.get("/")
def read_root():
    return {"message": "SHL Assessment Recommender API is up!"}

@app.get("/recommend")
def get_recommendations(query: str = Query(..., description="Job description or role")):
    results_df = recommender.recommend(query)
    return results_df.to_dict(orient="records")
