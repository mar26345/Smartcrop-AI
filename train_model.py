import pandas as pd

df = pd.read_csv(r'C:\Users\pc\Smartcrop-AI\data\crop_prediction.csv')
print(df.head())

print('\n',df.shape)
print('\n',df.columns)
print('\n',df.describe())
print('\n',df.duplicated())
print('\n',df.info())