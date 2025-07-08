from typing import List
import matplotlib.pyplot
from pandas import DataFrame, Series
import pandas as pd

x: str = "./Sleep_health_and_lifestyle_dataset.csv"

def load_sleep(x: str) -> DataFrame:
    df = pd.read_csv(x)
    return df

def get_activity_level(x: DataFrame) -> List[float]:
    ds: Series = x["Physical Activity Level"]
    return ds
def get_daily_steps(x: DataFrame) -> List[float]:
    ds2: Series = x["Daily Steps"]
    return ds2
def get_sleep_quality(x: DataFrame) -> List[float]:
    sq: Series = x["Quality of Sleep"]
    return sq

#print(get_activity_level(load_sleep(x)))

sq = get_sleep_quality(load_sleep(x))
ds = get_activity_level(load_sleep(x))
ds2 = get_daily_steps(load_sleep(x))

matplotlib.pyplot.scatter(ds, sq, s=None, alpha=0.5, linewidths=None, edgecolors=None, plotnonfinite=False, data=None)
matplotlib.pyplot.xlabel("Activity Level(Minutes per Day)", labelpad=4.0, loc='center')
matplotlib.pyplot.ylabel("Sleep Quality", labelpad=4.0, loc='center')
matplotlib.pyplot.title("Sleep Quality by Physical Activity", loc='center')
matplotlib.pyplot.show()

matplotlib.pyplot.scatter(ds2, sq, s=None, alpha=0.5, linewidths=None, edgecolors=None, plotnonfinite=False, data=None)
matplotlib.pyplot.xlabel("Daily Steps", labelpad=4.0, loc='center')
matplotlib.pyplot.ylabel("Sleep Quality", labelpad=4.0, loc='center')
matplotlib.pyplot.title("Sleep Quality by Daily Steps", loc='center')
matplotlib.pyplot.show()
