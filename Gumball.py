

'''

Quan's code:

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




# Here are all the imports needed for the web-app dashboard.
import pandas as pd
import numpy as np
import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
#from jupyter_dash import JupyterDash
import plotly.express as px
import matplotlib.pyplot as plt

import time
#import yfinance as yf




app = dash.Dash(__name__)

# Clear the layout and do not display exception till callback gets executed
app.config.suppress_callback_exceptions = True



guess_df = pd.read_csv('guess_df.csv')


app.layout = html.Div([dcc.Store(id='guess', storage_type='local'),
    html.H1('Gumball Guess',  style={'textAlign': 'center', 'color':'#C33C54','font-size':36}),
    html.Div(
        html.H2('Enter your guess here: ',
        style={'margin-right': '2em'})),
    html.Div(dcc.Input(id='input-guess',value=None,type='number',style={'height':'50px','font-size':35})),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Button('Show resutls', id='show-res', n_clicks=0),
    html.Button('Hide resutls', id='hide-res', n_clicks=0),
    html.Div([], id='hist-plot')])

'''
Adding hide/show button steps:

1. html.Button('Show/hide results')
2. if statements in callback function


'''

#dash.dependencies.Input('show-res', 'n_clicks')

'''
if n_clicks1 > 0:
        n_clicks1 = 0
        ret_disp = 'Your guess value is updated.'
    else:
        ret_disp = dcc.Graph(figure=dist_fig)
'''


@app.callback(
    dash.dependencies.Output('hist-plot', 'children'),
    [dash.dependencies.Input('submit-val', 'n_clicks'),
    dash.dependencies.Input('show-res', 'n_clicks'),
    dash.dependencies.Input('hide-res', 'n_clicks')],
    [dash.dependencies.State('input-guess', 'value')])
def graph_guesses(btn1, btn2, btn3, value):
    if value is None:
        raise PreventUpdate
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]
    if 'submit-val' in changed_id:
        guess_df.loc[len(guess_df)] = value
        guess_df.to_csv('guess_df.csv',index=False)
        showpg = html.H3('Your guess has been recorded!')
    elif 'show-res' in changed_id:
        dist_fig = px.histogram(guess_df, x = 'Guess value', nbins=10, marginal='box')
        dist_fig.update_traces(marker_color='#19D3F3')
        showpg = html.Div([dcc.Graph(figure=dist_fig),dash_table.DataTable(id='table',columns=[{"name": i, "id": i} for i in guess_df.describe().columns],data=guess_df.describe().to_dict('records'))])
    elif 'hide-res' in changed_id:
        showpg = html.H3('Please enter the next guess.')
    return showpg

'''
Time sleep for auto-hide plot results (60 seconds).
Hide button as well to hide plot results.
Add timestamp to each guess value data, so we can plot weekly guesses and all time guesses too.
'''



# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
