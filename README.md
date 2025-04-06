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
shl_assessment_recommendation/<br>
├── app/<br>
│   ├── recommender.py<br>
│   └── utils.py<br>
├── data/<br>
│   └── shl_product_catalog.csv<br>
├── main.py<br>
├── requirements.txt<br>
└── README.md<br>

