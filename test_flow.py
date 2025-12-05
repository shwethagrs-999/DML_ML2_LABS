import pandas as pd

def test_data_valid():
       df = pd.DataFrame({
           "age": [25, 32, 40, 50, 60],
           "bp": [120, 130, 140, 150, 160],
           "label": [0, 0, 1, 1, 1]
       })
       assert not df.isnull().values.any(), "❌ Data contains missing values"
       assert (df["age"] > 0).all(), "❌ Invalid age detected"
