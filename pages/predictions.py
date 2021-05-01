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

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            #### Where is the closest hot stpring?

            Enter the demographic data for your location.

            """
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        dcc.Markdown("Hispanic percentage of population:"),
        dcc.Input(
            id='Hispanic',
            type='number',
        ),
        dcc.Markdown("Percentage who drive to work:"),
        dcc.Input(
            id='Drive',
            type='number',
        ),
        dcc.Markdown("Mean Commute Time:"),
        dcc.Input(
            id='MeanCommute',
            type='number',
        ),
        dcc.Markdown("African American percentage of population:"),
        dcc.Input(
            id='Black',
            type='number',
        ),
        dcc.Markdown("Percentage who work in the public sector:"),
        dcc.Input(
            id='PublicWork',
            type='number',
        )
    ]
)

column3 = dbc.Col(
    [
        html.H4('Nearest thermal spring (predicted probability): ', className='mb-5'), 
        html.Div(id='prediction-content', className='lead')
    ]
)

@app.callback(
    Output('prediction-content', 'children'),
    [Input('Hispanic', 'value'), Input('Drive', 'value'), Input('MeanCommute', 'value'), Input('Black', 'value'), Input('PublicWork', 'value')],
)
def predict(Hispanic, Drive, MeanCommute, Black, PublicWork):
    test = np.array([Hispanic, Black, Drive, MeanCommute, PublicWork])
    test = test.reshape((1,-1))
    y_pred = dectree_model.predict(test)[0]
    y_prob = dectree_model.predict_proba(test)
    prob = max(y_prob[0])
    return f'{y_pred} ({round(prob*100)}%)'

if __name__ == "__main__":
    app.run_server(debug=True)
    # Debug set to False in run.py eliminates callback error

layout = dbc.Row([column1, column2, column3])

#joblib==1.0.1
#scikit-learn==0.22.2.post1