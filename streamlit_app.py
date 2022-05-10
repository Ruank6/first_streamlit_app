import streamlit
import pandas


streamlit.title('My Mom\'s New Healty Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')


# list all food customers can pick
fruits_selected = streamlit.multiselect("Pick some fruit: ", list(my_fruit_list.index),['Avocado','Strawberries'])

fruits_to_show=my_fruit_list.loc[fruits_selected]
# Display table on page
streamlit.dataframe(fruits_to_show)

# New section to display fruityvice api response
streamlit.header ('Fruityvice Fruit Advice! ')

import requests

fruityvice response =requests.get("https://fruityvice.com/api/fruit/" + "kiwi")
# take the json version of the response and normalize it
fruityvice normalized = pandas.json normalize(fruityvice response.json())
#output it the screen as a table
streamlit.dataframe(fruityvicenormalized)
