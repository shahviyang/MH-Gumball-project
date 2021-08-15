import numpy as np
import pandas as pd


guess_df = pd.DataFrame(columns = ['Guess value'])
value = 34
guess_df.loc[len(guess_df)] = value

print(guess_df.head())
#dist_fig = px.histogram(all_guesses, x = 'guesses')