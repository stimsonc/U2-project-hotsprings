# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Insights

            (The Sample Data page has a random selection of rows that can be used to try out the model. Enter the latitude and longitude values into a map to locate the county in question and see if you can find the nearest thermal spring!)

            The primary insight is that using demographic data, it is possible to predict the location of thermal springs in the United States with a relatively high degree of accuracy. 

            However, because the target variable is imprecise, even if the model accurately predicts a spring is close by, that just means one is somewhere inside a circle with a radius of 20 miles, which is equivalent to 1,257 square miles. 

            Therefore, in the alien invasion scenario, the resistance forces would still have a lot of work to do after getting a prediction. Searching 1,000-plus square miles of Wyoming for a thermal spring is no mean feat, though at very least they would be very unlikely to be sent searching some county in Iowa for a nonexistent spring. 

            Given what we can learn about thermal springs in the United States from looking at their distribution on a map for a few seconds, a simpler “predictive model” might be to simply tell the resistance forces to head to the Rocky Mountains and start looking. But this is only one of many plot holes in my scenario that will need to be fixed before it is made into a Netflix series. 

            In terms of a data problem, it is interesting to consider why it was possible to build such an accurate model. After all, thermal springs are a geologic phenomenon, while the census data is all socioeconomic factors. The key is that both thermal springs and socioeconomic factors are unevenly distributed, and this uneven distribution happens to align enough to make predictions feasible. 

            The graphic on the home page is a scatter plot of the latitudes and longitudes of all the “swimmable” springs included in the model. If you squint, it is possible to see a rough outline of the continental United States. The springs are overwhelmingly concentrated west of the Mississippi River, mostly in the Rocky Mountains and the Pacific coast ranges, with a smaller number in the Appalachian Mountains in the east. 

            These mountainous areas tend to be rural, which means people rely on automobiles rather than public transport; to have smaller minority populations, especially in the Mountain West; and to have large areas of federal- and state-owned land, which are managed by government employees. And these three traits are reflected in the five most important features in permutation: the percentage of the population who drive to work, the percentages who are hispanic and black, and the mean commute time. These areas also tend to be poorer, which is reflected in the sixth and seventh most important features (income per capita, child poverty rate). Only the top five were included in the model.  

            In one sense the model is interpretable. That is, the features it uses to generate its predications have a logic that is understandable to anyone with basic knowledge of the domain. 

            My original goal was to produce a model that could be memorized by resistance forces in the field so they would not have to depend on anything digital. I thought it would be possible to memorize the coefficients of a relatively short regression formula, or the cut-off points of a smallish decision tree, then enter in local data to get a result. However, the final decision tree is fairly large at 13 levels deep, which is not realistic to memorize. Accuracy was too low with smaller trees to make them useful, the same with regression models using fewer features. 

            A final note on feature engineering. Though I did very little for this project, I believe it would be possible to improve the model with some creative ideas. Building on the traits mentioned above could be a fruitful avenue. Adding elevation to the data is one thing that could have a big impact, as most thermal springs are located in the mountains. But this almost feels like feature leakage, and it might blow the cover story of the model being a harmless demographic tool. 

            """
        ),

    ],
)

column2 = dbc.Col(
    [
        html.Img(src='assets/wildspring.jpg', className='img-fluid'),
    ]
)

layout = dbc.Row([column1, column2])