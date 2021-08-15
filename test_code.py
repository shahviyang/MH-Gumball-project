import numpy as np
import pandas as pd


guess_df = pd.DataFrame(columns = ['Guess value'])
guess_df.to_csv('guess_df.csv',index=False)
#dist_fig = px.histogram(all_guesses, x = 'guesses')