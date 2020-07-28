import pandas as pd

data = pd.read_csv('./csv/cs-training.csv', index_col=0)

lim = int(0.8*len(data))
train = data.iloc[:lim, :]
test = data.iloc[lim:, :]

test.to_csv('./csv/test2.csv')