import pandas as pd
import requests
import streamlit

streamlit.title('Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinash & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Eggs')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruits_selected = streamlit.multiselect('Pick some fruits: ', list(my_fruit_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# if fruits_to_show.empty:
#   streamlit.dataframe(my_fruit_list)
# else:
streamlit.dataframe(fruits_to_show)

fruit_choice = streamlit.text_input('What fruit would you like to information about', 'Kiwi')
streamlit.write('The user entered ', fruit_choice)

response = requests.get(f'https://fruityvice.com/api/fruit/{fruit_choice}')
fruityvice_normalized = pd.json_normalize(response.json())
streamlit.dataframe(fruityvice_normalized)
