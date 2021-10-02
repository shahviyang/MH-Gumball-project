import numpy as np
import pandas as pd


#guess_df = pd.read_csv('guess_df.csv')
#print(guess_df.describe())
#print(type(guess_df.describe()))
#print(guess_df.loc[len(guess_df)-1])


guess_df = pd.DataFrame(columns = ['Guess value'])
guess_df.to_csv('guess_df.csv',index=False)

#dist_fig = px.histogram(all_guesses, x = 'guesses')