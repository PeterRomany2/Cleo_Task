import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px

# Streamlit page configuration
st.set_page_config(page_title="Complaints Analysis", layout="wide")

@st.cache_data
def load_escalation():
    escalation = pd.read_excel('Peter Assessment.xlsx', sheet_name='Escalation Sheet')
    return escalation

df = load_escalation()



pd.set_option("display.max_rows", None)
pd.set_option("expand_frame_repr", False)


# """
# there is extra space here:Items with issue  Dermatique
#                                                              the most important columns to do the analysis:
# 'Timestamp'  'The Brand name'    'Complaint Type'  'Comment about case'  'Priorty'  'Channel'  'Total Order Amount' 'Follow up date' 'Feedback/ last update'
# 'Gift Order status'  'Whole case Status'
#
# 'Items with issue Blankie', 'Items with issue cleo',
#        'Items with issue  Dermatique', 'Item with issue skin side'
# """
#
#
# '''                                                         Data wrangling
#                                 preparing raw data for analysis via convert raw data into analysis-ready data.
# '''

# Check data types for any type mismatch
# df.info()

# '''
# After conducting a thorough check for type mismatch within the dataset, these columns contain type mismatch:
# Total Order Amount column is numerical but there are some strings. (wrong data entry)
# '''


# Check missing data
# col00='Total Order Amount'
# print(df[df[col00].isnull()])#row has null

# '''
# After conducting a thorough check for missing data within the dataset, these columns contain missing data:
# Total Order Amount(3 rows contain null)
# '''

# Handle missing data
df.drop(df[df['Total Order Amount'].isnull()].index,inplace=True)
# Handle wrong data entry
df.drop(df[df['Total Order Amount']=="visa"].index,inplace=True)

# Handle type mismatch
mismatch_features = ['Total Order Amount']
df[mismatch_features] = df[mismatch_features].astype(int)


# '''                           Data mining and analysis   or   Exploratory Data Analysis (EDA)
#                                         extracting knowledge(insights) from data begins
# '''
#
# """Notes: the priority based on complaint type there is person took good with 17000 and its priorty meduim must be based on  Complaint Type and Total Order Amount
# """
# 'Insights'
# print(df['The Brand name'].value_counts())
# print(df['Complaint Type'].value_counts())
# print(df['Channel'].value_counts())
# print(df['Priorty'].value_counts())
# print(df['Gift Order status'].value_counts())
# print(df['Whole case Status'].value_counts())


# Handle outliers
# TotalOrderAmount_outliers=peter_romany_module.dealing_with_outlier(df,'Total Order Amount',show_outliers=False)
# """
# =============================== Total Order Amount ===========================================
# minus= 279.01535266631754 mean= 517.1973913043478 plus= 755.379429942378
#  CV= 46.052443930033405 % CV_Rate= 69.73913043478261 %
# =================================================================================
# skewness= 0.4711560124041401 rate 58.95652173913043 % [ 339 out of 575 ] [ most in low [where mode locate (mode < median= 450.0 < mean= 517.1973913043478)] ]
# ==============================================================================================================================================================
#
# perform insights_by_descriptive_analytics
# =============================== Total Order Amount ===========================================
# minus= -4013680.412368067 mean= 175294.03826086957 plus= 4364268.488889806
#  CV= 2389.6844936591497 % CV_Rate= 99.82608695652175 %
# =================================================================================
# skewness= 23.979155938546167 rate 99.82608695652175 % [ 574 out of 575 ] [ most in low [where mode locate (mode < median= 450.0 < mean= 175294.03826086957)] ]
# ==============================================================================================================================================================
# """

# '''The method dealing_with_outlier() alternates between activation and deactivation to ensure the acquisition of accurate and comprehensive information from actual data.
# It identifies outliers, storing them for further study and insight extraction purposes.'''

# peter_romany_module.insights_by_descriptive_analytics(df,'Total Order Amount')


# # Calculate the resolution time in days
# df['Resolution Time (Days)'] = (df['Follow up date'] - df['Timestamp'].dt.normalize()).dt.days
#
# # print(df.head())
#
# # Group by 'The Brand name' and calculate the average resolution time
# sla_per_brand = df.groupby('The Brand name')['Resolution Time (Days)'].mean().reset_index()
#
# # Rename columns for clarity
# sla_per_brand = sla_per_brand.rename(columns={'Resolution Time (Days)': 'Average Resolution Time (Days)'})
#
# # Display the result
# # print(sla_per_brand)
#
#
# import matplotlib.pyplot as plt
# import seaborn as sns
#
# # Set the style of the plot
# sns.set(style="whitegrid")
#
# # Create a barplot of the average resolution time per brand
# plt.figure(figsize=(10, 6))
# sns.barplot(x='Average Resolution Time (Days)', y='The Brand name', data=sla_per_brand, palette='viridis')
#
# # Add titles and labels
# plt.title('Average Resolution Time (Days) per Brand', fontsize=16)
# plt.xlabel('Average Resolution Time (Days)', fontsize=12)
# plt.ylabel('Brand', fontsize=12)
#
# # Show the plot
# plt.show()







# Calculate the resolution time in days
df['Resolution Time (Days)'] = (df['Follow up date'] - df['Timestamp'].dt.normalize()).dt.days



# df['Blankie']=df[df['The Brand name']=="Blankie"]['Resolution Time (Days)']
# df['Cleo']=df[df['The Brand name']=="Cleo"]['Resolution Time (Days)']
# df['Cleo (Studio skin)']=df[df['The Brand name']=="Cleo (Studio skin)"]['Resolution Time (Days)']
# df['Dermatique']=df[df['The Brand name']=="Dermatique"]['Resolution Time (Days)']
# df['Kayanek']=df[df['The Brand name']=="Kayanek"]['Resolution Time (Days)']
# df['Skin side']=df[df['The Brand name']=="Skin side"]['Resolution Time (Days)']


#
# peter_romany_module.dealing_with_outlier(df,'Blankie',show_outliers=True)
# peter_romany_module.dealing_with_outlier(df,'Cleo',show_outliers=True)
# peter_romany_module.dealing_with_outlier(df,'Cleo (Studio skin)',show_outliers=True)
# peter_romany_module.dealing_with_outlier(df,'Dermatique',show_outliers=True)
# peter_romany_module.dealing_with_outlier(df,'Kayanek',show_outliers=True)
# peter_romany_module.dealing_with_outlier(df,'Skin side',show_outliers=True)
#
# # Step 1: Calculate the Average Resolution Time without outliers for each brand
# peter_romany_module.insights_by_descriptive_analytics(df,'Blankie')
# peter_romany_module.insights_by_descriptive_analytics(df,'Cleo')
# peter_romany_module.insights_by_descriptive_analytics(df,'Cleo (Studio skin)')
# peter_romany_module.insights_by_descriptive_analytics(df,'Dermatique')
# peter_romany_module.insights_by_descriptive_analytics(df,'Kayanek')
# peter_romany_module.insights_by_descriptive_analytics(df,'Skin side')



















def check_login(username, password):
    return username == "omar" and password == "cleo"

def login_page():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if check_login(username, password):
            st.session_state.logged_in = True  # Set session state
            st.success("Login successful!")
            st.rerun()  # Redirect to the main app
        else:
            st.error("Invalid username or password")

if "logged_in" not in st.session_state or not st.session_state.logged_in:
    login_page()
    st.stop()  # Stop further execution of the page


st.title("SLA Report for Complaints Follow-Up")



# Introduction
st.write("This report calculates the **Service Level Agreement (SLA)** for complaints follow-up by each brand.")
st.write("The SLA is determined based on the **mean resolution time** and **descriptive analytics**.")

# SLA Calculation Overview
st.header("SLA Calculation Overview")
st.write(
    """
    Based on the provided **descriptive statistics**, the SLA for each brand is calculated considering:
    - The **mean resolution time** for complaints.
    - The **skewness** of the resolution time distribution (indicating if complaints are mostly resolved quickly, or if there are outliers).
    - **Coefficient of Variation (CV)**, which indicates the level of variability in resolution times.
    - **Mode, Median**, and other statistics were also used to determine a reasonable SLA for each brand.

    The SLA is set to slightly round up the **mean resolution time** to account for outliers, ensuring a more realistic and achievable service level for each brand.
    """
)

# Display metrics for each brand
st.header("SLA for Each Brand")
st.write("")



# Define the SLA for each brand
brand_sla = {
    'Blankie': 5,
    'Cleo': 5,
    'Cleo (Studio skin)': 5,
    'Dermatique': 5,
    'Kayanek': 5,
    'Skin side': 4
}

# Function to calculate the number of complaints resolved within SLA and other metrics
def calculate_complaints_metrics(df, brand_sla):
    result = {}

    for brand, sla in brand_sla.items():
        # Filter the data for the specific brand
        brand_data = df[df['The Brand name'] == brand]

        # Total number of complaints for the brand
        total_complaints = brand_data.shape[0]

        # Complaints resolved within SLA
        complaints_within_sla = brand_data[brand_data['Resolution Time (Days)'] <= sla].shape[0]

        # Complaints exceeding SLA
        complaints_exceeding_sla = brand_data[brand_data['Resolution Time (Days)'] > sla].shape[0]

        # Percentage of complaints resolved within SLA
        percentage_resolved_within_sla = (complaints_within_sla / total_complaints) * 100 if total_complaints > 0 else 0

        avg_sla = sla  # SLA is pre-defined as the expected resolution time, so it's directly used here

        # Store the results for each brand
        result[brand] = {
            'Complaints Resolved Within SLA': complaints_within_sla,
            'Complaints Exceeding SLA': complaints_exceeding_sla,
            'Percentage Resolved Within SLA': percentage_resolved_within_sla,
            'Total Complaints': total_complaints,
            'Average SLA (Days)': avg_sla

        }

    return result

# Calculate complaints metrics
metrics = calculate_complaints_metrics(df, brand_sla)



# Create circles for each brand containing Total Complaints and Average SLA
st.write("### Brand SLA and Total Complaints")
col1, col2, col3, col4, col5, col6 = st.columns(6)

# Loop over each brand to display metrics in circles
brands = list(brand_sla.keys())
for i, brand in enumerate(brands):
    with locals()[f'col{i + 1}']:  # Dynamically reference the columns
        total_complaints = metrics[brand]['Total Complaints']
        avg_sla = metrics[brand]['Average SLA (Days)']

        # Display circle with both Total Complaints and Average SLA
        st.metric(
            label=brand,
            value=f"{total_complaints} Complaints",
            delta=f"SLA: {avg_sla} days",
            delta_color="normal",  # Customize color as needed
            help=f"Total Complaints: {total_complaints}, SLA: {avg_sla} days"
        )

# Prepare data for the clustered bar chart
brands = list(brand_sla.keys())
resolved_values = [metrics[brand]['Complaints Resolved Within SLA'] for brand in brands]
exceeding_values = [metrics[brand]['Complaints Exceeding SLA'] for brand in brands]
resolved_percentages = [metrics[brand]['Percentage Resolved Within SLA'] for brand in brands]

# Create the clustered bar chart using Plotly
fig = go.Figure()

# Add Complaints Resolved Within SLA bars
fig.add_trace(go.Bar(
    x=brands,
    y=resolved_values,
    name='Complaints Resolved Within SLA',
    marker=dict(color='red'),
    text=[f"{val} ({perc:.2f}%)" for val, perc in zip(resolved_values, resolved_percentages)],  # Text with count and percentage
    textposition='outside',  # Position of the text inside the bars
))

# Add Complaints Exceeding SLA bars
fig.add_trace(go.Bar(
    x=brands,
    y=exceeding_values,
    name='Complaints Exceeding SLA',
    marker=dict(color='rgb(58, 71, 80)'),
    text=[f"{val} ({perc:.2f}%)" for val, perc in zip(exceeding_values, [100 - perc for perc in resolved_percentages])],  # Text with count and percentage
    textposition='outside',  # Position of the text inside the bars
))

# Update layout for the clustered bar chart
fig.update_layout(
    title="Complaints Resolved vs Exceeding SLA by Brand",
    xaxis_title="Brand",
    yaxis_title="Number of Complaints",
    barmode='group',  # Clustered bars
    template="plotly_dark",  # Dark theme
    showlegend=True
)

# Display the chart
st.plotly_chart(fig, use_container_width=True)


st.write('---')











st.title("Complaints Analysis Dashboard")


# Create a column for combined items with issues
df['Items with issues'] = df[['Items with issue Blankie',
                               'Items with issue cleo',
                               'Items with issue  Dermatique',
                               'Item with issue skin side']].apply(
    lambda x: ', '.join(x.dropna()), axis=1)

# Handle NaN and empty entries in the 'Items with issues' column
df['Items with issues'] = df['Items with issues'].replace('', 'Empty')


# Count the complaints by Brand, Item, and Complaint Type
brand_complaints = df['The Brand name'].value_counts().reset_index()
brand_complaints.columns = ['Brand', 'Number of Complaints']

item_complaints = df['Items with issues'].value_counts().reset_index()
item_complaints.columns = ['Item', 'Number of Complaints']

reason_complaints = df['Complaint Type'].value_counts().reset_index()
reason_complaints.columns = ['Reason', 'Number of Complaints']


# Display total complaints
total_complaints = df.shape[0]
st.markdown("<hr style='width: 50%; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)

# Center the total complaints text
st.markdown("<h3 style='text-align: center;'>Total Complaints: {}</h3>".format(total_complaints), unsafe_allow_html=True)

# Add horizontal line before and after the text
st.markdown("<hr style='width: 50%; margin-left: auto; margin-right: auto;'>", unsafe_allow_html=True)


# Complaints by Brand - Pie chart

# Create the pie chart
fig_brand = px.pie(
    brand_complaints,
    names='Brand',
    values='Number of Complaints',
    title="Complaints Distribution by Brand"
)

# Update the pie chart to display the number of complaints
fig_brand.update_traces(textinfo='value+percent')

# Display the pie chart in Streamlit
st.plotly_chart(fig_brand, use_container_width=True)




# Complaints by Item - Bar chart

import plotly.express as px

fig_item = px.treemap(
    item_complaints,
    path=['Item'],  # Use the full item names for the path (for hierarchy purposes)
    values='Number of Complaints',
    title="Complaints Distribution by Item",
    hover_data={'Item': True}  # Show full item name on hover
)

# Update traces to show the truncated name inside the treemap and full name on hover
fig_item.update_traces(
    textinfo='label+value+percent entry',  # Display label, value, and percentage in the treemap boxes
    textfont=dict(size=14, color='black'),  # Increase font size for better readability
    hovertemplate='<b>%{label}</b><br>Complaints: %{value}<br>Percentage: %{percentEntry:.2f}%'  # Show full item name on hover
)

# Plot the treemap
st.plotly_chart(fig_item, use_container_width=True)


# Complaints by Reason - Bar chart



# Calculate percentages based on the total number of complaints
total_complaints = reason_complaints['Number of Complaints'].sum()
reason_complaints['Percentage'] = (reason_complaints['Number of Complaints'] / total_complaints) * 100

# Create the bar chart
fig_reason = px.bar(
    reason_complaints,
    x='Reason',
    y='Number of Complaints',
    title="Complaints Distribution by Reason",
    color='Reason',
    text=[f"{val} ({perc:.2f}%)" for val, perc in zip(reason_complaints['Number of Complaints'], reason_complaints['Percentage'])]  # Add number and percentage as text
)
fig_reason.update_layout(
    showlegend=False  # Hide the legend
)
# Show the chart in Streamlit
st.plotly_chart(fig_reason, use_container_width=True)

# Count the complaints by Brand, Item, and Complaint Type
brand_complaints = df[['The Brand name', 'Items with issues', 'Complaint Type']].groupby(
    ['The Brand name', 'Items with issues', 'Complaint Type']).size().reset_index(name='Number of Complaints')


st.write("### Complaints by Brand, Item, and Reason")

# Create the stacked bar chart
fig = px.bar(
    brand_complaints,
    x='The Brand name',  # X-axis: Brand names
    y='Number of Complaints',  # Y-axis: Number of complaints
    color='Items with issues',  # Color by Item
    hover_data=['Complaint Type'],  # Hover data to show Complaint Type
    labels={'The Brand name': 'Brand', 'Items with issues': 'Item', 'Complaint Type': 'Reason'}
)

# Update layout for better visibility
fig.update_layout(
    barmode='stack',  # Stack bars
    xaxis_title="Brand",
    yaxis_title="Number of Complaints",
    showlegend=True  # Show legend for Items and Reasons
)

# Display the chart
st.plotly_chart(fig, use_container_width=True)




