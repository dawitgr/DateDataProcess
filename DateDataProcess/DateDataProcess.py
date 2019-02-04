
import re
import numpy as np
import pandas as pd
import pandas as pd

doc = []
with open('datedata.txt') as file:
    for line in file:
        doc.append(line)

df = pd.Series(doc)

def date_sorter():
    
    reg_one = df.str.extract(r'((?:\d{,2}\s)?(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*(?:-|\.|\s|,)\s?\d{,2}[a-z]*(?:-|,|\s)?\s?\d{2,4})')
    reg_two = df.str.extract(r'((?:\d{1,2})(?:(?:\/|-)\d{1,2})(?:(?:\/|-)\d{2,4}))')
    reg_three = df.str.extract(r'((?:\d{1,2}(?:-|\/))?\d{4})')
    final_dates = pd.to_datetime(reg_one.fillna(reg_two).fillna(reg_three).replace('Decemeber','December',regex=True).replace('Janaury','January',regex=True))
    final_data = pd.Series(final_dates.sort_values())# Your answer here
    return final_data.index
date_sorter()




