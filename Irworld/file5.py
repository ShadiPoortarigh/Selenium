
""" Export data to an excel file """


import pandas as pd
import openpyxl
from data import DATA

df = pd.DataFrame(DATA,
                 columns=['link', 'name', 'price_per_litr', 'volume', 'image', 'description', 'price', 'price_after_discount', 'discount' , 'net_price'] 
                    )

path = 'Irworld.xlsx'

with pd.ExcelWriter(path) as writer:
    df.to_excel(writer, sheet_name='care')
    