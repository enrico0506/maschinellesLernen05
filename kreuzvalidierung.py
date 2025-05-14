import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

#anzahl der stichproben
n_samples = 1000
n_features = 5

#zufällige seed setzen für reproduzierbarkeit
np.random.seed(50)

#uffällige eingabedaten ergeugen
X = np.random.randn(n_samples, n_features)
y = np.random.randint(0, 2, n_samples)


# In einen DataFrame umwandeln
data = pd.DataFrame(X, columns=[f'Feature_{i}' for i in range(n_features)])
data['Label'] = y

print(data.head())

#feature alst 2d array holen
feature_matrix = data.drop(columns="Label").values.tolist()
print(feature_matrix)

label_list = data["Label"].values.tolist()
print(label_list)

def split_even(lst, k):
    n = len(lst)
    q, r = divmod(n, k)
    parts = []
    start = 0
    for i in range(k):
        size = q + (1 if i < r else 0)
        parts.append(lst[start:start+size])
        start += size

    return parts

print(split_even(feature_matrix, 4))