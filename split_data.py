import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import StratifiedShuffleSplit

# read in data 
data = pd.read_csv(r".\Data Carrard et al. 2022 MedTeach.csv")
print(data)

#plot histogram of data, mbi_ex
plt.hist(data['mbi_ex'], bins=100, color='blue', edgecolor='black', alpha=0.65)
plt.xlabel('mbi_ex')
plt.ylabel('Frequency')
# plt.show()
# print(data['mbi_ex'].describe())

plt.hist(data['mbi_cy'], bins=100, color='blue', edgecolor='black', alpha=0.65)
plt.xlabel('mbi_cy')
plt.ylabel('Frequency')
# plt.show()
# print(data['mbi_cy'].describe())

plt.hist(data['mbi_ea'], bins=100, color='blue', edgecolor='black', alpha=0.65)
plt.xlabel('mbi_ea')
plt.ylabel('Frequency')
# plt.show()
# print(data['mbi_ea'].describe())


#split half of the data randomly into training and validation sets
split = StratifiedShuffleSplit(n_splits=1, test_size=0.5, random_state=42)
for train_index, val_index in split.split(data, data["mbi_ex"]):
    train = data.loc[train_index]
    val = data.loc[val_index]

#save training and validation sets to csv files
train.to_csv(r".\MedTeach_train.csv", index=False)
val.to_csv(r".\MedTeach_val.csv", index=False)