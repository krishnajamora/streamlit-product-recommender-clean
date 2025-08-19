# 🛒 E-commerce Product Recommendation System

This project is an **E-commerce Product Recommendation App** built using **Python** and **Streamlit**.  
It suggests similar products to users based on the item they select, similar to Amazon/Flipkart recommendations.

---

## 🚀 Features
- Product-based recommendation system
- Content-based filtering using **TF-IDF** and **Cosine Similarity**
- Interactive **Streamlit UI**
- Displays product details: Title, Price, and Image
- Deployed on **Streamlit Cloud** for easy access

---

## 🛠️ Tech Stack
- **Python**
- **Streamlit**
- **Pandas**
- **Scikit-learn**
- **TF-IDF Vectorizer**
- **Cosine Similarity**

---

## 📊 Dataset
The dataset contains product information such as:
- Title  
- Category  
- Description  
- Price  
- Image URL  

---

## ⚙️ Workflow
1. **Data Preprocessing** – Clean and prepare product data.  
2. **Feature Extraction** – Use TF-IDF to convert product descriptions into vectors.  
3. **Similarity Calculation** – Compute similarity between products using Cosine Similarity.  
4. **Recommendation Function** – Input: selected product → Output: Top N similar products.  
5. **Streamlit UI** – Interactive interface to search/select product and view recommendations.  
6. **Deployment** – Hosted on **Streamlit Cloud**.  

---

## 💻 Code Snippets

### Data Preprocessing

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(products['description'])


Recommendation Function
from sklearn.metrics.pairwise import cosine_similarity

cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def get_recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    top_items = [i[0] for i in sim_scores[1:6]]
    return products.iloc[top_items]

Streamlit UI
import streamlit as st

st.title("E-commerce Recommendation App")
product = st.selectbox("Choose a product:", products['title'])
recommendations = get_recommendations(product)

for _, r in recommendations.iterrows():
    st.image(r['image'])
    st.write(r['title'], "-", r['price'])

📦 Installation & Run

1.Clone this repository:

2.git clone https://github.com/yourusername/ecommerce-recommendation.git
cd ecommerce-recommendation


Install dependencies:

1.pip install -r requirements.txt

2.Run the Streamlit app:

streamlit run app.py

🌐 Deployment

>Deployed on Streamlit Cloud

>Accessible via shareable URL

📌 Future Scope

>Add collaborative filtering for user-personalized recommendations

>Integrate deep learning NLP models (BERT/Transformers)

>Enhance UI with advanced filters (price range, category)

👩‍💻 Author

Developed by [Your Name]

Do you want me to also create a **`requirements.txt` file** for this project so it’s ready to run?

