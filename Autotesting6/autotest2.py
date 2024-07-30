import pandas as pd
df = pd.read_csv("california_housing_test.csv")
max_households_in_min_population = df[df["population"] == df["population"].min()]["households"].max()
print(max_households_in_min_population)