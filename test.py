from random import random

from syntetic_data import AddressTextGenerator

from collections import OrderedDict

a = AddressTextGenerator()

df = a.generate_address_dataset()

print(df)

# print(df['Input'])

# print(df['Target Format'].value_counts())