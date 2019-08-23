import pandas as pd

titanic = pd.read_csv("D:\\Sarita Naik\\Python\\train.csv")
titanic.isnull().sum()