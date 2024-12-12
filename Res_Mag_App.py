import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
data_path = r'C:\Soundhar\Project\Resource management\Processed_Final_list.csv'
data = pd.read_csv(data_path)

# Streamlit App
st.set_page_config(page_title="Industrial Workforce Analysis", layout="wide")
st.title("Industrial Workforce Analysis Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")
selected_state = st.sidebar.selectbox(
    "Select State:",
    options=["All"] + list(data['State Name'].unique()),
    index=0
)
selected_category = st.sidebar.selectbox(
    "Select Business Category:",
    options=["All"] + list(data['Business Category'].unique()),
    index=0
)

# Filter the data
filtered_data = data.copy()
if selected_state != "All":
    filtered_data = filtered_data[filtered_data['State Name'] == selected_state]
if selected_category != "All":
    filtered_data = filtered_data[filtered_data['Business Category'] == selected_category]

# Overview Metrics
st.header("Overview Metrics")
total_workers = filtered_data['Main Workers - Total -  Persons'].sum()
male_workers = filtered_data['Main Workers - Total - Males'].sum()
female_workers = filtered_data['Main Workers - Total - Females'].sum()

col1, col2, col3 = st.columns(3)
col1.metric("Total Workers", f"{total_workers:,}")
col2.metric("Male Workers", f"{male_workers:,}")
col3.metric("Female Workers", f"{female_workers:,}")

# Visualization 1: Workforce by State
st.header("Workforce Distribution by State")
states_grouped = filtered_data.groupby('State Name', as_index=False).agg({
    'Main Workers - Total -  Persons': 'sum',
    'Main Workers - Total - Males': 'sum',
    'Main Workers - Total - Females': 'sum'
})

# Sorting the data in descending order by Total Workforce
states_grouped = states_grouped.sort_values(by='Main Workers - Total -  Persons', ascending=False)

fig1 = px.bar(
    states_grouped,
    x='State Name',
    y='Main Workers - Total -  Persons',
    color='State Name',
    title='Total Workforce by State',
    labels={"Main Workers - Total -  Persons": "Total Workers"}
)
st.plotly_chart(fig1, use_container_width=True)

# Visualization 2: Workforce by Business Category
st.header("Workforce Distribution by Business Category")
category_grouped = filtered_data.groupby('Business Category', as_index=False).agg({
    'Main Workers - Total -  Persons': 'sum',
    'Main Workers - Total - Males': 'sum',
    'Main Workers - Total - Females': 'sum'
})

fig2 = px.pie(
    category_grouped,
    names='Business Category',
    values='Main Workers - Total -  Persons',
    title='Workforce by Business Category'
)
st.plotly_chart(fig2, use_container_width=True)

# Visualization 3: Gender Distribution in Workforce
st.header("Gender Distribution in Workforce")
gender_grouped = filtered_data.agg({
    'Main Workers - Total - Males': 'sum',
    'Main Workers - Total - Females': 'sum'
})

gender_data = pd.DataFrame({
    "Gender": ["Male", "Female"],
    "Count": [
        gender_grouped['Main Workers - Total - Males'],
        gender_grouped['Main Workers - Total - Females']
    ]
})

fig3 = px.pie(
    gender_data,
    names='Gender',
    values='Count',
    title='Gender Distribution in Workforce'
)
st.plotly_chart(fig3, use_container_width=True)

# Insights Section
st.header("Key Insights")
st.markdown(
    """
    - **Total Workforce**: The dataset shows the distribution of workers across different states and industries.
    - **Male vs Female Workforce**: Analyze gender disparity in workforce participation.
    - **State-level Analysis**: Identify states with the highest workforce participation.
    - **Business Category Trends**: Understand the dominance of specific industries in certain regions.
    - This data can guide policy-making and employment strategies to ensure balanced workforce distribution.
    """
)
