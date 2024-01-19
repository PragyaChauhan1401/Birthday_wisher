import datetime as dt
import pandas as py
import random
import smtplib

today = (dt.datetime.now().month, dt.datetime.now().day)

data = py.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]):data_row for(index, data_row) in data.iterrows()}
MY_EMAIL = "pragyachauhan3004@gmail.com"
MY_PASSWORD = "mdjrvtleaggdqvst"

if today in birthdays_dict:
    birthdays_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthdays_person["name"])
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthdays_person["email"],
                            msg=f"Subject: HAPPY BIRTHDAY!\n\n{contents}")


