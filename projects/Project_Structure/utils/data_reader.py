import pandas as pd

def read_login_data(file_path):
    data = pd.read_csv(file_path)
    return data.values.tolist()