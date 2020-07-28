import pandas as pd
from sklearn.metrics import roc_auc_score
from flask import Flask, request

app = Flask(__name__)


y_all = pd.read_csv('./csv/cs-training.csv',index_col=0)['SeriousDlqin2yrs']

@app.route('/submit', methods=['POST'])
def auc():
    filepath = request.form['file'][1:]
    y_pred = pd.read_csv(filepath, index_col=0)['Probability']
    y = y_all[y_pred.index]
    auc = roc_auc_score(y, y_pred)
    print(auc)

    return {'auc': auc}