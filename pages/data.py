# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# My imports
import pandas as pd
import numpy as np
import plotly.express as px
from joblib import load
dectree_model = load('assets/dectree.joblib')

# Imports from this application
from app import app

# Load census dataframe
#file = 'https://raw.githubusercontent.com/stimsonc/Unit2_thermal_predictor/master/swimmers.csv'
#census = pd.read_csv(file)

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Data
            """
        ),

    ],
)

layout = dbc.Row([column1])