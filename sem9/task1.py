import pandas as pd
# Задача №1. Решение в группах
# 1. Прочесть с помощью pandas файл
# california_housing_test.csv, который находится в папке
# sample_data
# 2. Посмотреть сколько в нем строк и столбцов
# 3. Определить какой тип данных имеют столбцы

data = pd.read_csv("california_housing_test.csv")

#2 print(data.shape)

#3 print(data.dtypes)

# print(data.info())

# Задача №2. Решение в группах
# 1. Проверить есть ли в файле пустые значения
# 2. Показать median_house_value где median_income < 2
# 3. Показать данные в первых 2 столбцах
# 4. Выбрать данные где housing_median_age < 20 и
# median_house_value > 70000

#1 print(all(data.isnull()))
#1 print(data.isnull().sum())

#2 print(data[data["median_income"] < 2]["median_house_value"])

#3 print(data[['longitude','latitude']])
#3 print(data.iloc[:, :2])

#4 print(data[(data["housing_median_age"] < 20) & (data["median_house_value"] > 70000)])

# Задача №3. Решение в группах
# 1. Определить какое максимальное и минимальное
# значение median_house_value
# 2. Показать максимальное median_house_value, где
# median_income = 3.1250
# 3. Узнать какая максимальная population в зоне
# минимального значения median_house_value

# 1 print(f"Минимальное значение median_house_value - {data["median_house_value"].min()}, Максимальное значение - {data["median_house_value"].max()}")

# print(type(data["median_house_value"]))

# 2 print(data[data["median_income"] == 3.1250]["median_house_value"].max())

# 3 print(data[data["median_house_value"] == data["median_house_value"].min()]["population"].max())

