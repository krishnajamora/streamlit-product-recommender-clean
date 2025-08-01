import streamlit as st
import pandas as pd
from fuzzywuzzy import process, fuzz
import joblib

# Load similarity matrix (generated from cosine similarity of products)
similarity_df = joblib.load("product_similarity.pkl")  # Make sure this file is present

# -------- Fuzzy Suggestion Function -------- #
def get_product_suggestions(user_input, similarity_df, suggest_n=3, score_cutoff=60):
    user_input = user_input.strip().upper()

    matches = process.extractBests(
        query=user_input,
        choices=similarity_df.columns,
        scorer=fuzz.token_sort_ratio,
        limit=suggest_n,
        score_cutoff=score_cutoff
    )

    suggestions = [match[0] for match in matches]
    return suggestions

# -------- Recommend Top N Similar Products -------- #
def recommend_similar_products(product_name, similarity_df, top_n=5):
    similar_items = similarity_df[product_name].sort_values(ascending=False)[1:top_n+1]
    return pd.DataFrame(similar_items).reset_index().rename(columns={
        'index': 'Recommended Product',
        product_name: 'Similarity Score'
    })

# -------- Streamlit App UI -------- #
st.set_page_config(page_title="🛍️ Product Recommender", layout="centered")
st.title("🛒 Smart Product Recommendation System")

user_input = st.text_input("🔍 Enter product name (even partially or with typos):")

if user_input:
    suggestions = get_product_suggestions(user_input, similarity_df)

    if suggestions:
        selected = st.selectbox("✨ Select the closest matching product:", suggestions)

        if st.button("Get Recommendations"):
            st.success(f"✅ Showing recommendations similar to: **{selected}**")
            recommendations = recommend_similar_products(selected, similarity_df)
            st.dataframe(recommendations)

    else:
        st.error("❌ No close product matches found. Try a different name.")
