import streamlit as st
import pandas as pd
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt


st.title("Hello Wilders! :smile: welcome to my application!")
st.write("I enjoy discovering streaming possibilities. Let's see what we can analyze from this dataset of cars.")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_voiture = pd.read_csv(link)

# Add a checkbox to show/hide the DataFrame
show_data_checkbox = st.checkbox("Show DataFrame")
if show_data_checkbox:
    st.write(df_voiture)

#Add an option to choose region
option_region = st.radio( "Select continent",
                 ('Japan', 'USA', 'Europe', 'All continent'))

if option_region == 'USA':
   filtered_df = df_voiture[df_voiture["continent"] == " US."]
   filtered_df

    
if option_region == 'Europe':
    filtered_df = df_voiture[df_voiture["continent"] == " Europe."]
    filtered_df

    
if option_region == 'Japan':
    filtered_df = df_voiture[df_voiture["continent"] == " Japan."]
    filtered_df
else: 
    filtered_df = df_voiture

# Plot correlation heatmap for the selected region
if show_data_checkbox and option_region != 'All continent':
    st.subheader(f"Correlation Heatmap for {option_region}")
    # Exclude non-numeric columns for correlation calculation
    numeric_columns = filtered_df.select_dtypes(include=['float64', 'int64']).columns
    corr = filtered_df[numeric_columns].corr()
    
    # Specify the figure to use
    fig, ax = plt.subplots()
    
    # Plot heatmap on the specified figure
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    
    # Display the plot using st.pyplot() with the specified figure
    st.pyplot(fig)

# Create a bar chart for the number of cars per category
option_categorique = st.selectbox("Sélectionner une variable catégorique", ['mpg', 'cylinders', 'cubicinches', 'hp'])

# Group the data by the categorical variable and count the number of cars in each category
count_by_category = filtered_df[option_categorique].value_counts()

# Display the bar chart
st.bar_chart(count_by_category)