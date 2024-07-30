import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# df = pd.read_csv("california_housing_train.csv")

# Задача №1. Решение в группах
# 1. Изобразите отношение households к population с
# помощью точечного графика

# scatter_plot = sns.scatterplot(data = df, x="households", y="population")
# scatter_plot.set_title("Отношения между популяцией и домохозяйством")
# scatter_plot.set_xlabel("Популяция")
# scatter_plot.set_ylabel("Домохозяйства")
# plt.show()

# 2. Визуализировать longitude по отношения к
# median_house_value, используя линейный график

# sns.relplot(data=df, x="longitude", y="medianHouseValue", kind="line")
# plt.show()

# 3. Представить гистограмму по housing_median_age

# sns.histplot(data=df, x="housingMedianAge")
# plt.show()

# 4. Изобразить гистограмму по median_house_value с
# оттенком housing_median_age

# sns.histplot(data=df, x="medianHouseValue", hue="housingMedianAge")
# plt.show()


# Задача №2. Решение в группах
# Написать EDA для датасета про пингвинов
# Необходимо:
# ● Использовать 2-3 точечных графика
# ● Применить доп измерение в точечных графиках, используя
# аргументы hue, size, stile
# ● Использовать PairGrid с типом графика на ваш выбор
# ● Изобразить Heatmap
# ● Использовать 2-3 гистограммы
# Чтобы подключить датасет с
# пингвинами, воспользуйтесь данным
# скриптом:

#1 subtask
# penguins = sns.load_dataset("penguins")
# sns.scatterplot(data=penguins, x="sex", y="body_mass_g")
# plt.show()

#2 subtask

# sns.scatterplot(data=penguins, x="body_mass_g", y="flipper_length_mm", size="bill_length_mm",hue="bill_length_mm" 
            # sizes=(10, 100))
# plt.show()

#3 subtask поля входящие в график

# data_colums = ["species","island","bill_length_mm","bill_depth_mm","flipper_length_mm","body_mass_g"]
# graph = sns.scatterplot(data=penguins, x="body_mass_g", y="flipper_length_mm", hue="island", style="species")
# graph = graph.map_diag(plt.hist)
# graph = graph.map_offdiag(plt.scatter)


# plt.show()

# forth subtask

# data = penguins.pivot_table(index='species', columns='island', values='body_mass_g')
# sns.heatmap(data)
# plt.xlabel('Остров', size=14)
# plt.ylabel('Вид пингвина', size=14)
# plt.show()

# fifth subtask
# penguins['body_mass_g'].hist(bins=10)
# sns.displot(data=penguins, x="body_mass_g", kind="hist")
# plt.show()

# Задача №3. Решение в группах
# 1. Создать новый столбец в таблице с
# пингвинами, который будет отвечать за
# показатель длины клюва пингвина.
# high - длинный(от 42)
# middle - средний(от 35 до 42)
# low - маленький(до 35)

# penguins.loc[penguins['bill_length_mm'] < 35, 'height_group'] = 'low'
# penguins.loc[(penguins['bill_length_mm'] > 35) & (penguins['bill_length_mm'] < 42), 'height_group'] = 'middle'
# penguins.loc[penguins['bill_length_mm'] > 42, 'height_group'] = 'high'

# print(penguins)


# Задача №4. Решение в группах
# 1. Изобразить гистограмму по flipper_length_mm
# с оттенком height_group. Сделать анализ

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt


# data = pd.read_csv('penguins.csv')

# sns.histplot(data=data, x='flipper_length_mm', hue='height_group', multiple='dodge')
# plt.xlabel('Flipper Length (mm)')
# plt.ylabel('Count')
# plt.show()


import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data['human'] = data['whoAmI'].apply(lambda x: 1 if x == 'human' else 0)
data['robot'] = data['whoAmI'].apply(lambda x: 1 if x == 'robot' else 0)
print(data)

# get_dummies = pd.get_dummies(data)
# print(get_dummies)