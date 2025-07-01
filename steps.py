import pandas as pd
from zenml import step

@step
def loader() -> pd.DataFrame:
    print("Loading data...")
    data = {'name': ['Alice', 'Bob'], 'age': [25, 30]}
    return pd.DataFrame(data)

@step
def processor(data: pd.DataFrame) -> pd.DataFrame:
    print("Data processing...")
    data['is_adult'] = data['age'] >= 18
    print("Data has been processed:")
    print(data)
    return data