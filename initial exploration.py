import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# read in data 
data = pd.read_csv(r"C:\Users\orion\Downloads\Data Carrard et al. 2022 MedTeach.csv")
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
train = data.sample(frac=0.5, random_state=1)
val = data.loc[~data.index.isin(train.index)]

print(len(train))
print(len(val))

train.to_csv(r"C:\Users\orion\Downloads\MedTeach_train.csv", index=False)
val.to_csv(r"C:\Users\orion\Downloads\MedTeach_val.csv", index=False)
