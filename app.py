import streamlit as st
import pandas as pd
import numpy as np
import pickle 
import os

# Load data
data = pd.read_csv('food.csv')
recipes_1 = pickle.load(open('recipes_list.pkl','rb'))

similarity = pickle.load(open('similarity.pkl','rb'))
recipes_list = recipes_1['title'].values




st.header("Recipe Recommendation System")
# Dropdown
selected_recipe = st.selectbox("Select a recipe:", recipes_list)

import streamlit.components.v1 as components

def recom(recipes_1):
    index = recipes_1[recipes_1['title'] == recipes_1].index[0]
    distance = sorted(list(enumerate(similarity[index])),reverse=True,key =lambda vector:vector[1])
    recom_food = []
    for i in distance[1:5]:
        recom_food.append(recipes_1.iloc[i[0]].title)
    return recom_food

if st.button("Get Recommendations"):
    recommendations = recom(selected_recipe)
    st.write('**Recommended Recipes:**')
    for rec in recommendations:
        st.write(f"**Recipe Name:** {rec['title']}")
        st.write(f"**Required Time:** {rec['RequiredTime']} minutes")
        st.write(f"**Ingredients:** {rec['Ingredients']}")
        st.write(f"**Description:** {rec['Description']}")
        st.write('---')
























'''import streamlit as st
import pandas as pd
import numpy as np
import pickle 
import pandas as pd
data = pd.read_csv('food.csv')

recipe_list1 = pickle.load(open('recipes_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
recipes_list2 = recipe_list1['recipes'].values
#st.image('food.jpg', use_column_width=True)

st.header("Recipe Recommandation System")

#dropDown
selecte_recipes = st.selectbox("Select a recipe: ",recipes_list2)

import streamlit.components.v1 as components

def recommend(recipe):
    index = new_recipes[new_recipes['title'] == recipe].index[0]
    distance = sorted(list(enumerate(similarity.iloc[index])), reverse=True, key=lambda x: x[1])
    recommended_recipes = []
    for i in distance[1:6]:
        recommended_recipes.append(new_recipes.iloc[i[0]])
    return recommended_recipes

# Streamlit app
st.title('Recipe Recommendation System')

selected_recipe = st.selectbox('Select a recipe:', new_recipes['title'])

if st.button('Get Recommendations'):
    recommendations = recommend(selected_recipe)
    st.write('**Recommended Recipes:**')
    for rec in recommendations:
        st.write(f"**Recipe Name:** {rec['title']}")
        st.write(f"**Required Time:** {rec['RequiredTime']} minutes")
        st.write(f"**Ingredients:** {rec['Ingredients']}")
        st.write(f"**Description:** {rec['Description']}")
        st.write('---')

'''




'''
def recommend(recipe):
    index = recipe_list1[recipe_list1['recipes'] == recipe].index[0]
    distance = sorted(list(enumerate(similarity[index])) , reverse = True , key = lambda vector:vector[1])
    recommend_recipe = []
    for i in distance[1:6]:
        #recipe_id = recipes.iloc[i[0]].id
        recommend_recipe.append(recipe_list1.iloc[i[0]].recipe)
    return recommend_recipe

if st.button("Show Recommandation"):
    recipe_name   = recommend(selecte_recipes)
    col1 , col2 , col3 , col4 , col5 = st.columns(5)
    with col1:
        st.text(recipe_name[0])
    with col2:
        st.text(recipe_name[1])
    with col3:
        st.text(recipe_name[2])
    with col4:
        st.text(recipe_name[3])
    with col5:
        st.text(recipe_name[4])'''
