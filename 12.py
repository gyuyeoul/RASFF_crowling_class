from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd
import numpy as np
import csv
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
import os
import warnings

# RASFF_Subject = pd.DataFrame(
#             columns=[
#                 "REFERENCE",
#                 "SUBJECT",
#                 "NOTIFICATION_TYPE",
#                 "NOTIFICATION_BASIS",
#                 "CLASSIFICATION",
#                 "RISK_DECISION",
#             ]
#         )


# def Make_DataFrame(table_name, *colum):
#     a = []
#     for i in colum:
#         a.append(i)
#     table_name = pd.DataFrame(columns=a)

#     return print(table_name)


# Make_DataFrame(
#     "RASFF_Subject",
#     "REFERENCE",
#     "SUBJECT",
#     "NOTIFICATION_TYPE",
#     "NOTIFICATION_BASIS",
#     "CLASSIFICATION",
#     "RISK_DECISION",
# )


def text_replace(j):
    a = j.replace("(n)", "")
    a = a.replace("(o)", "")
    a = a.replace("(d)", "")
    a = a.replace("(op)", "")
    a = a.replace("(ffup)", "")
    a = a.replace("(ffa)", "")

    return a


origin = "abc(n)(d)(op)", "def(ffa)(ffup)(d)"

origin_list = []
for j in origin:
    a = text_replace(j)
    origin_list.append(a)
origin_list = ", ".join(origin_list)


print(origin_list)
