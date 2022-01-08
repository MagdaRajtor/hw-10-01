import pandas as pd
iris = pd.read_csv("data/iris.csv")
with pd.ExcelWriter('iris2.xlsx') as writer:
    for name in iris.variety.unique():
        iris[iris["variety"] == name].to_excel(writer, sheet_name=name)