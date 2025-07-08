from typing import List
import matplotlib.pyplot
from pandas import DataFrame, Series
import pandas as pd


x: str = "./Sleep_health_and_lifestyle_dataset.csv"

def load_sleep(x: str) -> DataFrame:
    df = pd.read_csv(x)
    return df

def get_daily_steps(x: DataFrame) -> List[float]:
    ds: Series = x["Daily Steps"]
    return ds
def split_into_regions(x: DataFrame) -> List[pd.DataFrame]:
    y: List[pd.DataFrame] = []
    z = pd.unique(x["Quality of Sleep"])
    for val in z:
        y.append(x[x["Quality of Sleep"]==val])
    return y
def get_avg_steps_per_region(x: List[pd.DataFrame]) -> List[float]:
    y: List[float] = []
    vol: Series = pd.Series({'A' : []})
    idx: int = 0
    while idx < len(x):
        vol = x[idx]["Daily Steps"]
        y.append(vol.mean())
        idx += 1
    return y
def get_sleep_quality(x: DataFrame) -> List[float]:
    sq: Series = x["Quality of Sleep"]
    return sq

print(split_into_regions(load_sleep(x)))

sq: List[float] = [6, 4, 7, 5, 8, 9]
ds = get_avg_steps_per_region(split_into_regions(load_sleep(x)))

matplotlib.pyplot.scatter(ds, sq, s=None, alpha=0.5, linewidths=None, edgecolors=None, plotnonfinite=False, data=None)
matplotlib.pyplot.xlabel("Average Daily Steps", labelpad=4.0, loc='center')
matplotlib.pyplot.ylabel("Sleep Quality", labelpad=4.0, loc='center')
matplotlib.pyplot.title("Sleep Quality by Average Daily Steps", loc='center')
matplotlib.pyplot.show()
print(ds)
print(split_into_regions(load_sleep(x)))