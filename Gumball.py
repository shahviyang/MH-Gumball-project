#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# !pip install dash


# In[ ]:


'''
import numpy as np
import matplotlib.pyplot as plt


#normal pdf function
def normal_dist(lst, mean , sd):
    prob_density = (np.pi*sd) * np.exp(-0.5*((lst-mean)/sd)**2)
    return prob_density

all_guesses = []

task = input("What would you like to do? ")

while task != "stop":
    if task == "guess":
        try:
            guess = int(input("What's your guess? "))
            all_guesses.append(guess)
        except:
            print("Please enter a valid whole number")
    elif task == "histogram":
        plt.hist(all_guesses)
        plt.show
    elif task == "graph pdf":
        mean = np.mean(all_guesses)
        sd = np.std(all_guesses)

        #Apply function to the data.
        pdf = normal_dist(all_guesses,mean,sd)
 
        #Plotting the Results
        plt.plot(all_guesses,pdf , color = 'red')
        plt.xlabel('Data points')
        plt.ylabel('Probability Density')
    else:
        print("Please enter a valid command.")

    task = input("What would you like to do? ")
'''


# In[ ]:


# Here are all the imports needed for the web-app dashboard.
import pandas as pd
import numpy as np
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
#from jupyter_dash import JupyterDash
import plotly.express as px
import matplotlib.pyplot as plt
#import yfinance as yf


# In[ ]:


app = dash.Dash(__name__)

# Clear the layout and do not display exception till callback gets executed
app.config.suppress_callback_exceptions = True


# In[ ]:



guess_df = pd.DataFrame(columns = ['Guess value'])

# In[ ]:


app.layout = html.Div([dcc.Store(id='guess', storage_type='local'),
    html.H1('Gumball Guess',  style={'textAlign': 'center', 'color':'#C33C54','font-size':36}),
    html.Div(
        html.H2('Enter your guess here: ',
        style={'margin-right': '2em'})),
    html.Div(dcc.Input(id='input-guess',value=None,type='number',style={'height':'50px','font-size':35})),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div([], id='hist-plot')])


'''
app.layout = html.Div([
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic',
             children='Enter a value and press submit')
])

@app.callback(
    dash.dependencies.Output('container-button-basic', 'children'),
    [dash.dependencies.Input('submit-val', 'n_clicks')],
    [dash.dependencies.State('input-on-submit', 'value')])
def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )


'''



@app.callback(
    dash.dependencies.Output('hist-plot', 'children'),
    [dash.dependencies.Input('submit-val', 'n_clicks')],
    [dash.dependencies.State('input-guess', 'value')])
def graph_guesses(n_clicks, value):
    if value is None:
        # prevent the None callbacks is important with the store component.
        # you don't want to update the store for nothing.
        raise PreventUpdate
    guess_df.loc[len(guess_df)] = value
    dist_fig = px.histogram(guess_df, x = 'Guess value', nbins=10)
    return dcc.Graph(figure=dist_fig)


# In[ ]:


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)


# Next steps:
# Add button to submit number guess.
# Add histogram to visualize guesses.



