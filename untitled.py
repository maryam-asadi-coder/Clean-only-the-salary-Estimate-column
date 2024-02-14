# -*- coding: utf-8 -*-
""".ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17053sIeV9Q3oPxfOS_PO1y7egb1S60En
"""

from google.colab import files

uploaded = files.upload()

import pandas as pd

df = pd.read_csv('df.csv')
df

def dollors_remover( a):   #اول یه تابع تعریف کن . این تابع سیو میمونه تو حافظه بعد هر جا خواستی فراخوانیش کن یعنی بگو این ستون یا این سلول رو با این تابعی که ساختم روی اون پیاده کن
  a = a.replace('$', ' ')
  return a

dollors_remover('$111K-$181K (Glassdoor est.)')   #اینجا تابع رو که قبلا ساخته بودیم رو فراخوانی میکنیم

df['Salary Estimate'].apply(dollors_remover)  #حالا کل دلار ریموور رو در کل ستون اپلای یا به اصطلاح اجراش کن

df  # فایل رو فراخوانی کن و میبینی که باز علامت دلار هست در ستون چرا؟؟؟ چون تو تغییرات رو سیو نکردی

df['Salary Estimate'] = df['Salary Estimate'].apply(dollors_remover) #داده های قبلی رو برابر داده های جدید میکنم و

df #حالا خروجی بگیر

def k_remover(a):   #حالا ک رو از ستون مربوطه حذف میکینم و نوبت به ک رسید پس دوباره یه تابع خوشگل تعریف میکنم
  a = a.replace('K' , ' ')
  return a

df['Salary Estimate'][0]   # من برای نمونه که مثل قبلی نباشه از مدل ایندکس استفاده میکنم و سلول اولم رو فراخوانی میکنم که مثلا یادآوری کنم و ضرورتی نداره

k_remover('111K- 181K (Glassdoor est.)')  #دیدی که ک هم ریمو شد

df['Salary Estimate'] = df['Salary Estimate'].apply(k_remover)  #میای میگی این قانون رو روی کل ستون اعمال کن

df  # حالا میگی نشونش بده ببینم؟

df['Salary Estimate']  # میتونی فقط بگی که ستون مربوطه رو نشون بده که از این روش میتونی فراخوانیش کنی

df[df['Salary Estimate'] != '-1']  #عدد -۱ هم خنزن پنزل است یعنی یا حقوق نامشخص یاحقوق صفر یا عدم وجود داده یاخطا در داده است که باید حذف شود

df = df[df['Salary Estimate'] != '-1'] #من برابر دی اف هم میگیرم اما با توجه به حجم داده نمیتونم ببینم که -۱ حذف شده پس یه اینفورمشن هم میگیرم

df.info()  #با اطلاعات قبلی مقایسه کنی میبینی این ۵۵۲۶ سطر داره و قبلی ۵۸۹۲ تا سطر داره پس حذف کرده

df['Salary Estimate'].str.contains('Per Hour') #ما تصمیم گرفتیم که اون حقوق هایی که بر اساس ساعت گفته شده رو توی دیتاست در نظر نگیریم من میخوام اونایی که این عبارت توشه رو نشون بده میبینید جایی که زده فالس یعنی این عبارت داخلش نیست میبینی اخری تورو هست یعنی شماره ۵۸۹۱ داخلش این عبارت موجوده

df[df['Salary Estimate'].str.contains('Per Hour')]  #باز اینجا سلولهایی که این عبارت رو نشون میده رو به من نشون داد

df[~df['Salary Estimate'].str.contains('Per Hour')]  # توجه کن اینجا ابتدای همان دستور قبلی یه عبارت نقضضض میزارم یعنی اونایی که این عبارت رو ندارن نشون بده

df = df[~df['Salary Estimate'].str.contains('Per Hour')] #برابر دی اف قرار بده تا در کل دیتا اعمال بشه
df

df.info() #خروجی بگیر میبینی که داری کلین میکنی از تعداد سطر ها

df.to_csv('my_dataframe.csv')