from numpy.lib.arraysetops import unique
import pandas as pd
import numpy as np
import openpyxl
import xlrd
import plotly.express as px

d = pd.read_excel('Sample - Superstore.xls' , sheet_name='Orders', engine='xlrd')
import plotly.graph_objects as go
import streamlit as st
st.set_page_config(page_title='Sample Business Growth', page_icon='💶📊', layout='wide')
max = d['Profit'].astype('int').max()
min = d['Profit'].astype('int').min()

unique_seg = d['Segment'].unique().tolist()
unique_cat = d['Category'].unique().tolist()
lst = list(range(min, max))

losses_range = st.slider('Select Profit Range', min_value=int(min), max_value=int(max),value=(int(min), int(max)))
rating_sel = st.slider('Select Review Range', min_value=0, max_value=5, value=(0,5))
select_seg = st.multiselect(label='You Can Select Segments', options=unique_seg, default=unique_seg)
select_cat = st.multiselect(label='You Can Select Category', options=unique_cat, default=unique_cat)
filter = ((d['Segment'].isin(select_seg)) & (d['Category'].isin(select_cat)) & (d['Profit'].between(*losses_range)))
df =d[filter]
superstore  = df[['Row ID',
 'Order ID',
 'Order Date',
 'Ship Date',
 'Ship Mode',
 'Customer ID',
 'Customer Name','Country',
 'City','Product Name',
 'Sales','Quantity',
 'Discount',
 'Profit']]
profit = superstore[superstore['Profit'] >=0]['Profit'].sum()
st.write('Total Profit :' + str(profit))
Loss = superstore[superstore['Profit'] <=0]['Profit'].sum()
st.write('Total Loss :' + str(Loss))
Neat = profit -  Loss
st.write('Neat :' + str(Neat))
st.write('Total Percentage of Loss : ')
st.write((abs(Loss)/Neat)*100)
st.write('Percentage Gained Profit : ')
st.write((abs(profit)/Neat)*100)
pivot = df.pivot_table(index='Product Name', values=['Sales', 'Profit'])
st.subheader('Pivot Table')
st.write(pivot)

import plotly.graph_objects as go




res = pd.read_csv('zomato.csv', encoding='unicode-escape')
res = res[(res['Aggregate rating'].between(*rating_sel))]
st.subheader('Connecting Your Business Worldwide. View The Acquired Ratings.')
fig = px.scatter_mapbox(res, 
                    lat='Latitude', 
                    lon='Longitude', 
                    hover_name='Aggregate rating', 
                    hover_data=['City','Address'],
                    color='Aggregate rating',
                    zoom=3,
                    color_continuous_scale=px.colors.cyclical.IceFire,
                    range_color=(0,5),
                    mapbox_style='mapbox://styles/kundu/ckskru8yc1zjq17pjextsjr9s',
                    center = dict(
                      lat = 37.0902,
                      lon= -95.7129
                    )    
                    )
fig.update_layout(mapbox_accesstoken='pk.eyJ1Ijoia3VuZHUiLCJhIjoiY2s4bzN0Nmt4MTR6aDNqbzJoMGI5cWp4byJ9.oXdKRoD0eXu_qynttt3wSw')
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(figure_or_data=fig)
st.subheader('Connecting Your Business Worldwide. View The Acquired Ratings.')
fig = px.line_mapbox(res, 
                    lat='Latitude', 
                    lon='Longitude', 
                    hover_name='Aggregate rating', 
                    hover_data=['City','Address'],
                    color='City',
                    zoom=3,
                    center = dict(
                      lat = 36,
                      lon = -99
                    ),
                    mapbox_style='mapbox://styles/kundu/ckskru8yc1zjq17pjextsjr9s'
                    )
fig.update_layout(mapbox_accesstoken='pk.eyJ1Ijoia3VuZHUiLCJhIjoiY2s4bzN0Nmt4MTR6aDNqbzJoMGI5cWp4byJ9.oXdKRoD0eXu_qynttt3wSw')
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(figure_or_data=fig)

st.subheader('Locations of Business Expansion')
res['lat'] = res['Latitude']
res['lon'] = res['Longitude']
st.map(res[['lat', 'lon']])

st.title('Business Dataset')
st.write(df)


#Profitable Segments
st.title('Profitable Segments : ')
col1, col2 = st.beta_columns(2)
col1.write('Profit By Segment ')
col1.write(df.groupby('Segment').Profit.sum())
col2.write('Sales By Segment')
col2.write(df.groupby('Segment').Sales.sum())
import plotly.graph_objects as go
from plotly.subplots import make_subplots

labels = df['Segment']

# Create subplots: use 'domain' type for Pie subplot
fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
fig.add_trace(go.Pie(labels=labels, values=df['Sales'], name="Sales", title='Sales By Segment'),
              1, 1)
fig.add_trace(go.Pie(labels=labels, values=df['Profit'], name="Profit", title='Profit By Segment'),
              1, 2)

# Use `hole` to create a donut-like pie chart
fig.update_traces(hole=.4, hoverinfo="label+percent+name")
fig.update_traces(textposition='inside', textinfo='percent+label')

fig.update_layout(
    title_text="Sales and Profit",
    # Add annotations in the center of the donut pies.
)
st.plotly_chart(fig)


st.title('Progit by Segment')
st.write(df.groupby('Segment').Profit.sum())
f = px.pie(df, names='Segment', values='Profit', hover_data=['Segment'])
st.plotly_chart(f)

#Profit by category
col1, col2 = st.beta_columns(2)
col1.write(df.groupby('Category').Profit.sum().reset_index())
col2.write(df.groupby('Category').Sales.sum().reset_index())
import plotly.graph_objects as go
from plotly.subplots import make_subplots

labels = df['Category']

# Create subplots: use 'domain' type for Pie subplot
fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
fig.add_trace(go.Pie(labels=labels, values=df['Sales'], name="Sales", title='Sales By Category'),
              1, 1)
fig.add_trace(go.Pie(labels=labels, values=df['Profit'], name="Profit", title='Profit By Category'),
              1, 2)

# Use `hole` to create a donut-like pie chart
fig.update_traces(hole=.4, hoverinfo="label+percent+name")
fig.update_traces(textposition='inside', textinfo='percent+label')

fig.update_layout(
    title_text="Sales and Profit",
    # Add annotations in the center of the donut pies.
)
st.plotly_chart(figure_or_data=fig)



#Products Appearing
import plotly.graph_objects as go
from plotly.subplots import make_subplots
st.subheader('Product Appearance')
products_appearence = df['Product Name'].value_counts().nlargest(10).rename_axis('Product Name').reset_index(name='Total Sales')
st.write(products_appearence)
fig = go.Figure(data=[go.Bar(
            x=products_appearence['Product Name'], y=products_appearence['Total Sales'],
            text=products_appearence['Total Sales'],
            textposition='auto',
        )])
st.plotly_chart(figure_or_data=fig)




#Most Profutable Products
st.title('Most Profitable Products : ')
most_profitable = df.groupby('Product Name').Profit.sum().nlargest(10).reset_index()
st.write(most_profitable)
fig = go.Figure(data=[go.Bar(
            x=most_profitable['Product Name'],y=most_profitable['Profit'],
            text=most_profitable['Profit'],
            textposition='auto',
        )])
st.plotly_chart(fig)


#Less Profitable Products
st.subheader('Least Profitable Products')
st.write(df.groupby('Product Name').Profit.sum().nsmallest(10))


#Describing Your Data
st.write(df[['Profit','Discount']].mean())


superstore  = df[['Row ID',
 'Order ID',
 'Order Date',
 'Ship Date',
 'Ship Mode',
 'Customer ID',
 'Customer Name','Country',
 'City','Product Name',
 'Sales','Quantity',
 'Discount',
 'Profit']]



s = superstore.groupby(by=['Customer Name']).sum()
profit_df = s.reset_index()
profit_df['Total Discount'] = profit_df['Discount']*profit_df['Profit']/100
most_profit = profit_df.nlargest(10, 'Profit')[['Sales','Quantity','Profit','Total Discount', 'Customer Name','Total Discount']]
st.write('Most Profitable Customer')

fig = go.Figure(data=[
    go.Bar(name='Sales',x=most_profit['Customer Name'], y=most_profit['Sales'], text=most_profit['Sales']),
    go.Bar(name='Profit',x=most_profit['Customer Name'], y=most_profit['Profit'],text=most_profit['Profit']),
])

# Change the bar mode
fig.update_layout(barmode='group')
st.plotly_chart(figure_or_data=fig)

most_loses = profit_df.nsmallest(20, 'Profit').reset_index()
st.write('Most Loses Customer')
st.write(most_loses)
fig = go.Figure(data=[
    go.Bar(name='Sales',x=most_loses['Customer Name'], y=most_loses['Sales'], text=most_loses['Sales']),
    go.Bar(name='Profit',x=most_loses['Customer Name'], y=most_loses['Profit'],text=most_loses['Profit'], textposition='auto'),
])
# Change the bar mode
fig.update_layout(barmode='group')
st.plotly_chart(figure_or_data=fig)


