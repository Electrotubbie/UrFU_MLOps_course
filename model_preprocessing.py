import pandas as pd
import numpy as np
from typing import Literal
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OrdinalEncoder
from data_creation import TEST_PATH, TRAIN_PATH


TRAIN_FILE = f'{TRAIN_PATH}diamonds_train.csv'
TEST_FILE = f'{TEST_PATH}diamonds_test.csv'


def X_y_save(path, train_test: Literal['train', 'test'], df, target_column):
    '''
    Функция для сохранения массивов параметров и целевых переменных.
    path - путь для сохранения массивов;
    train_test - наменование части набора данных. 'train' или 'test';
    df - набор данных;
    target_column - колонка с целевой переменной.
    '''
    np.save(f'{path}X_{train_test}.npy', df.drop(columns=[target_column]).values)
    np.save(f'{path}y_{train_test}.npy', df[target_column].values)


def preprocessing(X_train, X_test, num_columns=None, cat_columns=None):
    if num_columns:
        scaler = MinMaxScaler()
        X_train[num_columns] = scaler.fit_transform(X_train[num_columns])
        X_test[num_columns] = scaler.transform(X_test[num_columns])
    if cat_columns:
        encoder = OrdinalEncoder()
        X_train[cat_columns] = encoder.fit_transform(X_train[cat_columns])
        X_test[cat_columns] = encoder.transform(X_test[cat_columns])
    return X_train, X_test


df_train = pd.read_csv(TRAIN_FILE, index_col=0)
df_test = pd.read_csv(TEST_FILE, index_col=0)
# извлечение столбцов с числовыми данными и категориальными
cat_cols = df_train.dtypes[df_train.dtypes == 'object'].index.to_list()
num_cols = df_train.drop('price', axis=1).dtypes[~(df_train.dtypes == 'object')].index.to_list()
# предобработка данных перед обучением модели
df_train, df_test = preprocessing(df_train, df_test, num_columns=num_cols, cat_columns=cat_cols)
# сохранение полученных данных
X_y_save(TRAIN_PATH, 'train', df_train, 'price')
X_y_save(TEST_PATH, 'test', df_test, 'price')