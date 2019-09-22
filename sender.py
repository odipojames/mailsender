import csv
import smtplib
from settings import SENDER_EMAIL, SENDER_PASSWORD

# Email template for students on track
OnTrack_MSG = """
Hello {},
We are glad to let you know that you are on good track,
please keep it up

Thank you,
Moringa School
"""
# template for  students doing bad
Not_OnTrack_MSG = """
Hello {},
We are sorry to inform you that you are doing poor,
reason {},


Thank you,
Moringa School
"""


# read students data from csv document
csv_file = open('students.csv')
student_data_reader = csv.reader(csv_file,delimiter=',')
next(student_data_reader)

# connection to mail server
conn = smtplib.SMTP('imap.gmail.com',587)
conn.ehlo()
conn.starttls()
conn.login(SENDER_EMAIL,SENDER_PASSWORD)
for row in student_data_reader:

    Student,Email,IP1 ,IP2 , IP3, IP4,Attendance,First,reason,Final,reason = row

     # checks perfomance and recommendations for each student and send email to each accodingly
    if  First =='Yes' and Final == 'Yes':
        msg = OnTrack_MSG.format(Student)
    else :
        msg = Not_OnTrack_MSG.format(Student,reason)

    conn.sendmail(SENDER_EMAIL,Email,msg)

conn.quit()  #mail logout

csv_file.close()
