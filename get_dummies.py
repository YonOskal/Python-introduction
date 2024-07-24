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