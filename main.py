from app.recommender import SHLRecommender

def main():
    catalog_path = "data/shl_product_catalog.csv"
    recommender = SHLRecommender(catalog_path)
    
    print("Welcome to SHL Assessment Recommender Engine!")
    jd = input("Enter a job description or role: ")
    recommendations = recommender.recommend(jd)
    
    print("\nTop SHL Assessment Recommendations:\n")
    print(recommendations.to_string(index=False))

if __name__ == "__main__":
    main()
