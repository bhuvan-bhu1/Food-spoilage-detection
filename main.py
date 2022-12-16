import pytesseract as pt
import re
import pandas as pd
from datetime import datetime
from dateutil import relativedelta
pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

text = pt.image_to_string("img1.jpg")
x = text.split("\n")
# print(text)

#find the months to get expire
for i in x:
    find = i.find("BEST")
    if find > -1:
        expire_date = i      
months_to_expire = 0
for i in expire_date:
    if i.isdigit():
        months_to_expire = i



match_str = re.search(r'\d{2}-\d{2}-\d{4}',text)
required_date = datetime.strptime(match_str.group(), '%d-%m-%Y').date()
print("The Date of manufactured: ",required_date)


today = datetime.today()
print("Today's Date: ",today)

#date difference between packed and today
delta = relativedelta.relativedelta(today,required_date)
result_months= str(delta.months)

#print the result
if result_months <= months_to_expire:
    print("Food is safe to eat")
else:
    print("Food is spoiled")
