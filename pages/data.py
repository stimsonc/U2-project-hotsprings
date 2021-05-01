# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
# My imports
import pandas as pd
import numpy as np
import plotly.express as px
from joblib import load
dectree_model = load('assets/dectree.joblib')

# Imports from this application
from app import app

# Load census dataframe
file = 'https://raw.githubusercontent.com/stimsonc/Unit2_thermal_predictor/master/census.csv'
census = pd.read_csv(file)

# Small df with only features, target, results 
def wrangle(df, model):
  # Columns to include from original dataframe
  cols = ['Hispanic', 'Drive', 'MeanCommute', 'Black', 'PublicWork', 'Latitude', 'Longitude', 'to_spring_cat']
  
  # Predictions
  X = df[['Hispanic', 'Black', 'Drive', 'MeanCommute', 'PublicWork']]
  y_pred = model.predict(X)
  # Maximum probabilty for each row
  y_prob = model.predict_proba(X)
  probs = []
  for i in range(len(y_prob)):
    probs.append(max(y_prob[i]))
  
  new = df[cols]
  # Column of preciction = true/false
  new['Prediction'] = y_pred
  # Whether the prediction is correct or not
  correct = new['to_spring_cat'] == new['Prediction']
  new['Correct'] = correct
  # Column of probabiliities
  new['Probability'] = probs
  # Rename column
  new.rename(columns={"to_spring_cat": "True"}, inplace=True)
  return new

wrangle_df = census.copy()
dash_df = wrangle(wrangle_df, dectree_model)

# Display random sample of dash_df
import plotly.graph_objects as go
n=12
sample = dash_df.sample(n=n)

fig = go.Figure(data=[go.Table(
    header=dict(values=list(sample.columns),
                fill_color='paleturquoise',
                align='left'),
    cells=dict(values=[sample.Hispanic, sample.Drive, sample.MeanCommute, sample.Black, sample.PublicWork, sample.Longitude, sample.Latitude, sample['True'], sample.Prediction, sample.Correct, sample.Probability],
               fill_color='lavender',
               align='left'))
])

column1 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1])