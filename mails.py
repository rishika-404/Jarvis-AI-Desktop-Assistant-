import smtplib
import config
def SendEmail(to,content):
    try:
        server=smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD) #from which acc you send mails
        # message='to:{}\n\n{}'.format(to,content)
        server.sendmail(config.EMAIL_ADDRESS,to,content)
        server.quit()
    except:
        print("Cant establish a connection")

