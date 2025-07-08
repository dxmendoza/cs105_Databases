from pandas import DataFrame, Series

import pandas as pd

x: str = "./avocado.csv"

def load_avocado(x: str) -> DataFrame:
    return pd.read_csv(x)

def get_avg_total_volume(x: DataFrame) -> float:
    vol: Series = x["Total Volume"]
    return vol.mean()

print(get_avg_total_volume(load_avocado(x)))
