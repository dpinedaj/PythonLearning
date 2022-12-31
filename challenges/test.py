import numpy as np
import pandas as pd


matrix = [(22, 16, 23), (33, np.NaN, 11), (44, 34, 11), (55, 35, np.NaN), (66, 36, 13)]
# Create a DataFrame object
dfObj = pd.DataFrame(matrix, index=list("abcde"), columns=list("xyz"))

dfObj = dfObj.drop(columns=dfObj.columns[dfObj.max().argmax()])
dfObj.columns[dfObj.max().argmax()]
