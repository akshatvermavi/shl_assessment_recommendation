# # from app.recommender import SHLRecommender

# # def main():
# #     catalog_path = "data/shl_product_catalog.csv"
# #     recommender = SHLRecommender(catalog_path)
    
# #     print("Welcome to SHL Assessment Recommender Engine!")
# #     jd = input("Enter a job description or role: ")
# #     recommendations = recommender.recommend(jd)
    
# #     print("\nTop SHL Assessment Recommendations:\n")
# #     print(recommendations.to_string(index=False))

# # if __name__ == "__main__":
# #     main()

# from fastapi import FastAPI, Query
# from app.recommender import SHLRecommender

# app = FastAPI()
# recommender = SHLRecommender("data/shl_product_catalog.csv")
# @app.get("/health")
# def health_check():
#     return {"status": "healthy"}

# @app.get("/")
# def read_root():
#     return {"message": "SHL Assessment Recommender API is up!"}

# @app.get("/recommend")
# def get_recommendations(query: str = Query(..., description="Job description or role")):
#     results_df = recommender.recommend(query)
#     return results_df.to_dict(orient="records")




from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from app.recommender import SHLRecommender

app = FastAPI()
recommender = SHLRecommender("data/shl_product_catalog.csv")

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy"}

# Root endpoint (optional)
@app.get("/")
def read_root():
    return {"message": "SHL Assessment Recommender API is live."}

# Request and response models
class RecommendRequest(BaseModel):
    query: str

class Assessment(BaseModel):
    url: str
    adaptive_support: str
    description: str
    duration: int
    remote_support: str
    test_type: List[str]

class RecommendResponse(BaseModel):
    recommended_assessments: List[Assessment]

# POST /recommend endpoint (required by SHL)
@app.post("/recommend", response_model=RecommendResponse)
def recommend_assessments(payload: RecommendRequest):
    query = payload.query
    raw_results = recommender.recommend(query)

    # Convert DataFrame rows to list of Assessment objects with dummy metadata
    recommendations = []
    for _, row in raw_results.iterrows():
        recommendations.append({
            "url": "https://www.shl.com/solutions/products/product-catalog/view/" + row["AssessmentName"].lower().replace(" ", "-") + "/",
            "adaptive_support": "No",
            "description": row["Description"],
            "duration": 15,  # you can customize this per assessment if needed
            "remote_support": "Yes",
            "test_type": ["Knowledge & Skills"]
        })

    return {"recommended_assessments": recommendations}
