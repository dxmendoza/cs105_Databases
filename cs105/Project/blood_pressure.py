from typing import List
import matplotlib.pyplot
from pandas import DataFrame, Series
import pandas as pd

x: str = "./Sleep_health_and_lifestyle_dataset.csv"
y: str = "./New_Sleep_Dataset.csv"

def load_sleep(x: str) -> DataFrame:
    df = pd.read_csv(x)
    df[['Systolic Pressure', 'Diastolic Pressure']] = df['Blood Pressure'].str.extract(r'(\d+\.?\d*).*?(\d+\.?\d*)')
    # look for blanks in Sleep Disorders
    df['Sleep Disorder'] = df ['Sleep Disorder'].fillna('Nothing')
    return df

def get_systolic_pressure(x: DataFrame) -> List[float]:
    sp: Series = x["Systolic Pressure"]
    return sp
def get_diastolic_pressure(x: DataFrame) -> List[float]:
    dp: Series = x["Diastolic Pressure"]
    return dp
def get_age(x: DataFrame) -> List[float]:
    ag: Series = x["Age"]
    return ag

#save new dataset
df = pd.read_csv(x)
df2 = pd.read_csv(y)
#df.to_csv("New_Sleep_Dataset.csv", index=False)

#pd.merge(x, y, )
apnea = df2[(df2["Sleep Disorder"] == "Sleep Apnea") & ((df2["Age"] >= 20) & (df2["Age"] <= 40))]
gen = df2[(df2["Gender"] == "Female")]
apneaGen1 = pd.merge(apnea, gen, on='Person ID', how='inner')
apneaGen2 = pd.concat([apnea, gen])
print(apneaGen2)
#apnea.to_csv("Apnea_Age_Dataset.csv", index=False)
#apneaGen1.to_csv("Apnea_Gen_Merge.csv", index=False)
#apneaGen2.to_csv("Apnea_Gen_Union.csv", index=False)


ag = get_age(load_sleep(x))
sp = get_systolic_pressure(load_sleep(x))
dp = get_diastolic_pressure(load_sleep(x))



matplotlib.pyplot.scatter(sp, ag, s=None, alpha=0.5, linewidths=None, edgecolors=None, plotnonfinite=False, data=None)
matplotlib.pyplot.xlabel("Systolic Pressure", labelpad=4.0, loc='center')
matplotlib.pyplot.ylabel("Age", labelpad=4.0, loc='center')
matplotlib.pyplot.title("Relationship between Age and Systolic Blood Pressure", loc='center')
matplotlib.pyplot.show()

matplotlib.pyplot.scatter(dp, ag, s=None, alpha=0.5, linewidths=None, edgecolors=None, plotnonfinite=False, data=None)
matplotlib.pyplot.xlabel("Diastolic Pressure", labelpad=4.0, loc='center')
matplotlib.pyplot.ylabel("Age", labelpad=4.0, loc='center')
matplotlib.pyplot.title("Relationship between Age and Diastolic Blood Pressure", loc='center')
matplotlib.pyplot.show()