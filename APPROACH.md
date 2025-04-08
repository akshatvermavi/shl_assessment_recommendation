# SHL Assessment Recommendation Engine – Final Submission

## ✅ Objective

Build a web-based API tool that recommends SHL assessments based on a user's input query (job role or description), following the provided API schema and format.

---

## 🛠️ Tech Stack

- **FastAPI** – Web framework for API development
- **scikit-learn** – TF-IDF vectorizer and cosine similarity for recommendations
- **pandas** – Data handling and transformation
- **Uvicorn** – ASGI server to run FastAPI
- **Render** – Deployment platform (free tier)
- **GitHub** – Source code hosting and version control

---

## ⚙️ How It Works

1. Load SHL's product catalog (CSV) containing `AssessmentName`, `Description`, and `Tags`.
2. Preprocess tags using a simple cleaner (`utils.py`) to remove punctuation and lowercase the text.
3. Apply **TF-IDF vectorization** on tags.
4. On receiving a POST query, compute **cosine similarity** between the query and catalog entries.
5. Return the top 3 matching assessments with additional required metadata.

---

## 🚀 API Endpoint Summary

- **Base URL:** `https://shl-assessment-recommendation-1.onrender.com`
- **POST /recommend** – Main recommendation endpoint
- **GET /health** – Health check endpoint

---

### 🔸 `POST /recommend`

- **Request:**

```json
{
  "query": "backend developer"
}
```


- **Request:**

```json
{
  "recommended_assessments": [
    {
      "url": "https://www.shl.com/solutions/products/product-catalog/view/developer-role-assessment/",
      "adaptive_support": "No",
      "description": "Tests coding, debugging, and technical problem solving",
      "duration": 15,
      "remote_support": "Yes",
      "test_type": ["Knowledge & Skills"]
    },
    ...
  ]
}

```


## ✅ Links

* 🔗 **Web App (Swagger UI):** [https://shl-assessment-recommendation-1.onrender.com/docs](https://shl-assessment-recommendation-1.onrender.com/docs)
* 🔗 **GitHub Repository:** [https://github.com/akshatvermavi/shl_assessment_recommendation](https://github.com/akshatvermavi/shl_assessment_recommendation)
* 🔗 **Base URL for the API end point:**
  * [https://shl-assessment-recommendation-1.onrender.com/recommend](https://github.com/akshatvermavi/shl_assessment_recommendation)
* 🔗 **URL of the webapp that you built:**
  * [https://shl-assessment-recommendation-1.onrender.com/docs](https://github.com/akshatvermavi/shl_assessment_recommendation)


## 🧠 Notes

* The tool is fully API-based, deployed, and publicly accessible.
* All responses follow the schema attached in SHL's GenAI assignment instructions.


### ✅ Next Steps:

    

1. Copy the content above and replace your existing `APPROACH.md` file.
2. Then push it to GitHub:

```bash
git add APPROACH.md
git commit -m "Updated approach document to match SHL API format"
git push origin main
```

✅ **How to Run Locally**:

    1. Clone the repo

    git clone https://github.com/akshatvermavi/shl_assessment_recommendation

### 
    2. Create and activate a virtual environment

    python -m venv venv

    ./venv/Scripts/activate

### 
    3. Install dependencies

    pip install -r requirements.txt

### 
    4. Start the API server

    uvicorn main:app --reload
