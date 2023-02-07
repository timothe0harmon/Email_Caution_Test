from tkinter import *
import smtplib
import time

gui = Tk()

#Creds
gmail_email = ""
gmail_pass_gmail = ""
recipient_email = ""


title_body = {"Safe Test Grey":"Test123",
  "Caution Test Yellow":"https://google.com/amp/example.com/bad.exe",
  "Unsafe Test Red" :"https://bit.ly/380AXa4"}

def Send_Banner(color):
   with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
       smtp.ehlo()
       smtp.starttls()
       smtp.ehlo()
       smtp.login(gmail_email, gmail_pass_gmail)
       for subject in title_body:
           if color == "Send All":
               print("Sending All Emails")
               time.sleep(3)
               msg = f'Subject:{subject}\n\n{title_body[subject]}'
               smtp.sendmail(gmail_email, recipient_email, msg)

           if color == "red":
               if "Red" in subject:
                   print("Sending Unsafe E-mail")
                   msg = f'Subject:{subject}\n\n{title_body[subject]}'
                   smtp.sendmail(gmail_email, recipient_email, msg)

           if color == "yellow":
               if "Yellow" in subject:
                   print("Sending Potentinally Unsafe E-mail")
                   msg = f'Subject:{subject}\n\n{title_body[subject]}'
                   smtp.sendmail(gmail_email, recipient_email, msg)

           if color == "Grey":
               if "Grey" in subject:
                   print("Sending Safe E-mail")
                   msg = f'Subject:{subject}\n\n{title_body[subject]}'
                   smtp.sendmail(gmail_email, recipient_email, msg)

red_banner=Button(text="Red Test",command=lambda: Send_Banner("red")).grid(row=0)
yellow_banner=Button(text="Yellow Test",command=lambda: Send_Banner("yellow")).grid(row=0,column=1)
grey_banner=Button(text="Grey Test",command=lambda: Send_Banner("Grey")).grid(row=0,column=2)
all_banner=Button(text="Send All",command=lambda: Send_Banner("Send All")).grid(row=1,column=1)

mainloop()
Send_Banner()

