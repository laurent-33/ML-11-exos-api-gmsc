import pandas as pd

data = pd.read_csv('./csv/test2.csv', index_col=0)

data = data.drop(data.columns, axis=1)

data['Probability'] = 0.8

data.to_csv('./csv/test2-predictions.csv', index_label='Id')