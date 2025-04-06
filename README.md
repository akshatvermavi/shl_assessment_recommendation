# SHL Assessment Recommendation Engine

## 📌 Overview

This is a simple recommendation engine that suggests SHL assessments based on a given job description or role. It uses TF-IDF vectorization and cosine similarity on a mock SHL product catalog.

## 🚀 How It Works

- Loads a product catalog (`shl_product_catalog.csv`)
- Preprocesses the tags field for similarity computation
- Takes job description input from the user
- Outputs the top 3 relevant SHL assessments

## 🧰 Technologies Used

- Python
- pandas
- scikit-learn
- TF-IDF Vectorization

## 📁 Project Structure

shl_assessment_recommendation/`<br>`
├── app/`<br>`
│   ├── recommender.py`<br>`
│   └── utils.py`<br>`
├── data/`<br>`
│   └── shl_product_catalog.csv`<br>`
├── main.py`<br>`
├── requirements.txt`<br>`
└── README.md`<br>`


# SHL Assessment Recommendation Engine Approach

## Objective

Build an API that takes a job role or description as a query and returns relevant SHL assessments based on textual similarity.

## Tools Used

- **FastAPI**: For creating the API
- **scikit-learn (TF-IDF)**: To vectorize and compare text similarity
- **pandas**: For data handling
- **Uvicorn**: ASGI server to serve FastAPI app
- **Render**: Deployment platform

## How It Works

1. Load the SHL product catalog from CSV
2. Use TF-IDF vectorization on descriptions
3. Compare the input query to catalog descriptions using cosine similarity
4. Return top 3 most relevant assessments in JSON format

## API Usage

- Endpoint: `/recommend`
- Method: `GET`
- Query Parameter: `?query=your_search_term`

Example:
\`GET https://shl-assessment-recommendation-1.onrender.com/recommend?query=backend%20developer%20with%20coding%20skills\`

## Example Output

\`\`\`json
[
  {
    \"AssessmentName\": \"Developer Role Assessment\",
    \"Description\": \"Tests coding, debugging, and technical problem solving\"
  },
  {
    \"AssessmentName\": \"Finance Aptitude Test\",
    \"Description\": \"Measures understanding of financial concepts and numeracy\"
  },
  {
    \"AssessmentName\": \"Project Management Test\",
    \"Description\": \"Assesses planning, risk management, and execution skills\"
  }
]
\`\`\`
" > APPROACH.md
