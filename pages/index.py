# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Soak in Springs: 
            ## Defeat the Aliens

            The only known way to repel the invaders is to soak in a thermal spring for 10 mintues, giving immunity to their weapons for 24 hrs. But an alien info-attack will soon erase all digital and hard-copy information on thermal springs. 

            ✅ This model uses 2017 U.S Census data to predict the distance from a county's population center to the nearest swimmable (≤110 F) spring.

            ✅ The model will eventually be disguised as a demographic analysis tool. As it will likely fall into enemy hands, the predictions must be imprecise (<20 miles, 20-50 miles, >50 miles).
            """
        ),
        dcc.Link(dbc.Button('Find a spring', color='primary'), href='/predictions')
    ],
    md=4,
)

# Load census dataframe
file = 'https://raw.githubusercontent.com/stimsonc/Unit2_thermal_predictor/master/swimmers.csv'
swimmers = pd.read_csv(file)

# Histogram of lat/lon of swimmable springs 
fig = px.scatter(swimmers, x='Longitude', y='Latitude', color='Max_surface_temp_F', hover_name='Max_surface_temp_F')

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])