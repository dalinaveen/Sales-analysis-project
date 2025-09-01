#----Creating function-----
import pandas as pd
import warnings
import ctypes
import time as t

def explore_data(df):
    print("Shape Rows & Columns :",df.shape)
    print("Columns Names :\n",list(df.columns))
    print("Data Types + Null :",df.info())
    print("Description :",df.describe() )

def missing_report(df):
    null_count=df.isnull().sum()
    Total_count =len(df)

    Missing_report =pd.DataFrame({
        "Null Count":null_count,
        "Total count":Total_count,
        "missing %":(null_count/Total_count)*100
    })
    print(Missing_report)

def check_duplicate(df):
    duplicates=df.duplicated().sum()
    if duplicates> 0:
        t.sleep(2)
        choice=ctypes.windll.user32.MessageBoxW(
            0,                                                                  # handle (0 = default)
            f"{duplicates} duplicate rows found!\nDo you want to delete them?", # message
             "Data Alert",                                                      # title
             4|48                                                               # buttons (1 = OK/Cancel)
        )
        t.sleep(3)
        if choice==6: #Yes
            df=df.drop_duplicates()
            ctypes.windll.user32.MessageBoxW(
            0,
            "Duplicates deleted successfully ✅",
            "Action Complete",

             0|64
            )
        else: # NO
            ctypes.windll.user32.MessageBoxW(
            0,
            "Duplicates Were Not removed❌",
            "Action Cancelled",

             0|48
            )


    else:
        t.sleep(2)
        ctypes.windll.user32.MessageBoxW(
            0,
            "No duplicate rows found! ✅",
            "Data Alert",
             0
            )
    return df

    