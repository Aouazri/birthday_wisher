# Extra Hard Starting Project #
import datetime as dt
import pandas as pd
import smtplib
from random import randint

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
date = dt.datetime.now()
birthday_month = date.month
birthday_day = date.day
df = pd.read_csv("birthdays.csv")
df_dict = df.to_dict(orient="records")
birthday_wishes = False
for entry in df_dict:
    if birthday_month == entry['month'] and birthday_day == entry['day']:
        name = entry['name']
        birthday_wishes = True
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
    # name from birthdays.csv
if birthday_wishes:
    random_letter = randint(1, 3)
    with open(f"letter_templates/letter_{random_letter}.txt", mode='r') as file:
        letter = file.readlines()
        birthday_text = "".join(letter)
        with open(f"letter_templates/letter_{random_letter}.txt", mode='a') as f:
            birthday_text = birthday_text.replace("[NAME]", name)
    # 4. Send the letter generated in step 3 to that person's email address.
    # add your email and password here
    my_email = "youremail@gmail.com"
    password = "yourPassword"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Happy Birthday!\n\n{birthday_text}"
        )
    print("email sent successfully")
else:
    print("the current date doesn't match any birthdays")
# I scheduled this task to run daily using pythonanywhere.com cloud service.
# It automatically checks whether it's someone's birthday and sends them a happy birthday message!
