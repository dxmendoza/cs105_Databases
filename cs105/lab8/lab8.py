from typing import List
import matplotlib.pyplot
from pandas import DataFrame, Series
import pandas as pd

x: str = 'avocado.csv'

def load_avocado(x: str) -> DataFrame:
    df = pd.read_csv(x)
    return df

def split_into_regions(x: DataFrame) -> List[pd.DataFrame]:
    y: List[pd.DataFrame] = []
    z = pd.unique(x["region"])
    for val in z:
        y.append(x[x["region"]==val])
    return y

def get_avg_total_volume_per_region(x: List[pd.DataFrame]) -> List[float]:
    y: List[float] = []
    vol: Series = pd.Series({'A' : []})
    idx: int = 0
    while idx < len(x):
        vol = x[idx]["Total Volume"]
        y.append(vol.mean())
        idx += 1
    return y
def get_avg_avg_price_per_region(x: List[pd.DataFrame]) -> List[float]:
    y: List[float] = []
    pri: Series = pd.Series({'A' : []})
    idx: int = 0
    while idx < len(x):
        pri = x[idx]["AveragePrice"]
        y.append(pri.mean())
        idx += 1
    return y
df: pd.DataFrame = load_avocado(x)
regions: List[pd.DataFrame] = split_into_regions(df)
volume: List[float] = get_avg_total_volume_per_region(regions)
price: List[float] = get_avg_avg_price_per_region(regions)

matplotlib.pyplot.scatter(price, volume, s=None, alpha=0.5, linewidths=None, edgecolors=None, plotnonfinite=False, data=None)
matplotlib.pyplot.xlabel("Price", labelpad=4.0, loc='center')
matplotlib.pyplot.ylabel("Volume", labelpad=4.0, loc='center')
matplotlib.pyplot.show()

