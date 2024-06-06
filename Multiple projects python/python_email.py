import smtplib as s

ob = s.SMTP('smtp.gmail.com',587)  # port number for gmail 587
ob.ehlo()
ob.starttls()

ob.login('your_email_id','your_password')

subject = "test python"
body = "I Love Python"
massage = "subject: {}n\n{}".format(subject, body)
listadd = ['abc@gmail.com', 'abc1@gmail.com','abc1@gmail.com']

ob.sendmail('senders mail addrese',listadd,massage)

print("send mail")

ob.quit()
