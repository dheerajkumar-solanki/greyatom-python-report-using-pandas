# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here
df = pd.read_csv(path)
df["state"] = df["state"].str.lower()

df["total"] = df["Jan"] + df["Feb"] + df["Mar"]

sum_row = df[["Jan", "Feb", "Mar", "total"]].sum()
df_final = df.append(sum_row, ignore_index=True)
# Code ends here


# --------------
import requests

# Code starts here

url = "https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations"

response = requests.get(url)

df1 = pd.read_html(response.content)[0]
columns_val = list(df1.iloc[11])
df1 = df1.iloc[12:]

df1.columns = columns_val
 
print(df1)
# Code ends here


# --------------





df1['United States of America'] = df1['United States of America']\
                                        .astype(str)\
                                        .apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# print(df_final["state"])

# Code starts here
mapping = df1.set_index("United States of America")["US"].to_dict()

df_final.insert(6, "abbr", "")

df_final["abbr"] = df_final["state"].map(mapping)
# Code ends here


# --------------
# Code stars here




df_final.set_value(df_final[df_final['state']=="mississipi"].index[0], "abbr", "MS")
df_final.set_value(df_final[df_final['state']=="tenessee"].index[0], "abbr", "TN")

# Code ends here


# --------------
# Code starts here

# Calculate the total amount
# df_final = df_final[df_final.index != 15]
df_sub=df_final[["abbr", "Jan", "Feb", "Mar", "total"]].groupby("abbr").sum()
print(df_sub.shape)
print(df_sub)
# Add the $ symbol
formatted_df = df_sub.applymap(lambda x: "${}".format(x))

# Code ends here


# --------------
# Code starts here
sum_row = df_sub.sum()

df_sub_sum = pd.DataFrame(sum_row).T

df_sub_sum = df_sub_sum.applymap(lambda x: "${}".format(x))

final_table = formatted_df.append(df_sub_sum)

final_table.rename(index={0:"Total"}, inplace=True)
print(final_table)
# Code ends here


# --------------
# Code starts here
print(df_sub["total"])

df_sub["total"].plot(kind="pie")

plt.show()
# Code ends here


