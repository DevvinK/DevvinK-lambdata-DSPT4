# my_lambdata/my_script.py

import pandas
from my_lambdata.my_mod import enlarge

print("Happy Tuesday night.")

df = pandas.DataFrame({"x": [1,2,3], 'y':[4,5,6]})
print(df.head())

x=5
print('Enlarged', x, 'To', enlarge(x))

