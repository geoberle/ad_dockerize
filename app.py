import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
from flask import Flask
import os
from time import gmtime
import rpy2.rlike.container as rlc
import pandas
import json
import datetime

app = Flask(__name__)
ad = importr("AnomalyDetection")


def doit(series):
    df = robjects.DataFrame(
        rlc.OrdDict([
            ("timestamp", robjects.POSIXct([gmtime(p[0]) for p in series])),
            ("count", robjects.IntVector([p[1] for p in series]))
        ])
    )
    res = ad.AnomalyDetectionTs(df, max_anoms=0.02, direction='both', plot=False)
    return res

if __name__ == "__main__":
    with open('data.json', 'r') as f:
        data = json.loads(f.read())
        series = data['results']
        for i, p in enumerate(series):
            p[0] = p[0]+i*600
        print(doit(series))
    #app.run(host="127.0.0.1", port=5100, debug=True)


