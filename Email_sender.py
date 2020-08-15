import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Manvika Jaiswal'
email['to'] = 'manvikajaiswal1995@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content('I am a pythom master!')

with smtplib.SMTP(host='smtp.gmail.com', port= 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('manvikajaiswal1995@gmail.com','Jaisman@678#')
    smtp.send_message(email)
    print('all good boss!')