import random as Divran

import yagmail


Divotp = Divran.randint(100,999)

Divuser = "Div@gmail.com"
Divpwd = "Div"
Divrecipient = input("Enter your email to get the OTP: ")

Divsub = "DivOTP"
Divcont = ["The OTP for your account recovery is %s, Please don't share this with anyone"%(Divotp)]

with yagmail.SMTP(Divuser, Divpwd) as Divyag:
    Divyag.send(Divrecipient, Divsub, Divcont)
    print("The email transfer has been initiated, Check your email client service for the OTP")


Divotpver = int(input("Enter your OTP here for compliance verification: "))

Divinstance = isinstance(Divotpver, int)

if Divinstance==True:
    if Divotpver==Divotp:
        print("The OTP has been successfully verified, Your account compliance hold will be released soon")

    else:
        print("Negative for OTP verification, No release on account compliance hold")

else:
    print("Enter the OTP in right format")










