import numpy as np


all_guesses = np.empty(2)
np.append(all_guesses, value)
guess_df = pd.DataFrame({'guesses':all_guesses})

print(guess_df)
#dist_fig = px.histogram(all_guesses, x = 'guesses')