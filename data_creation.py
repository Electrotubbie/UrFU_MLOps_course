import pandas as pd
import os
from sklearn.model_selection import train_test_split

TRAIN_PATH = './train/'
TEST_PATH = './test/'
PATH_LIST = [TEST_PATH, TRAIN_PATH]

for path in PATH_LIST:
    if not os.path.isdir(path):
        os.mkdir(path)

dataset = pd.read_csv('https://raw.githubusercontent.com/Electrotubbie/datasets_to_studying/main/diamonds.csv', index_col=0)

df_train, df_test = train_test_split(dataset, test_size=0.3, random_state=42)

df_train.to_csv(f'{TRAIN_PATH}diamonds_train.csv')
df_test.to_csv(f'{TEST_PATH}diamonds_test.csv')