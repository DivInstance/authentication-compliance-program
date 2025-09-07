import random
import yagmail

otp = random.randint(100, 999)

sender_email = "your_email@gmail.com"
sender_password = "your_password"

recipient_email = input("Enter your email to receive the OTP: ")

subject = "OTP Verification"
content = [f"The OTP for your account recovery is {otp}. Please do not share this with anyone."]

try:
    with yagmail.SMTP(sender_email, sender_password) as yag:
        yag.send(recipient_email, subject, content)
        print("Email sent successfully! Check your inbox for the OTP.")
except Exception as e:
    print(f"Failed to send email. Error: {e}")
    exit()

try:
    entered_otp = int(input("Enter the OTP here for verification: "))
except ValueError:
    print("Invalid input! Please enter the OTP as a number.")
    exit()

if entered_otp == otp:
    print("OTP verified successfully. Your account compliance hold will be released soon.")
else:
    print("OTP verification failed. No release on account compliance hold.")
