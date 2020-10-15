#EMAIL Sender
import smtplib
from email.message import EmailMessage
import os
import time
import imghdr

def AskForInput():
	while True:
		response = input('\nStart A New Message (Y/N): ').strip()
		if response == 'Y' or response == 'y':
			return True
		elif response == 'N' or response == 'n':
			return False
		else:
			print("Invalid Input")



#___________________________________________________________________________________________________________________________

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
	#create and encrypt connection to gmail servers
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()	

	#login
	successful = False
	while not successful:
		SENDER_ADDRESS = input("Your Email: ")
		APP_PASSCODE = input("Your App Passcode: ")
		try:
			smtp.login(SENDER_ADDRESS, APP_PASSCODE)
			successful = True
		except:
			successful = False

	#Start Sequence
	print(""" -------------------------------
/|Welcome To Reda's Mail Sender|
|-------------------------------
-------------------------------/""")
	time.sleep(1)

	#User loop
	while AskForInput():
		#Start new message loop
		print("\n>>>>>>>>>>>>>> New Message >>>>>>>>>>>>>>")
		msg = EmailMessage()

		#Set message sender
		msg['From'] = SENDER_ADDRESS

		#Set message recipient
		RECIEVER_ADDRESS = input('Recipient Email Address (use ", " to seperate multiple email addresses):\n')
		if RECIEVER_ADDRESS == "Test":
			RECIEVER_ADDRESS = SENDER_ADDRESS
		msg['To'] = RECIEVER_ADDRESS

		#Set message subject
		msg['Subject'] = input('\nSubject:\n')

		#Set message body
		body = input('\nBody (type "html" to add html instead):\n')
		if body == 'html':
			try:
				with open(input("\nInsert File Path:\n"), 'r') as html:
					msg.add_alternative(html.read(), subtype='html')
			except:
				print("Invalid File")
		else:
			msg.set_content(body)
			attachments = input('\nExtra Attachments (to add files, seperate file paths with a ", "):\n').split(", ")
			for filePath in attachments:				
				if filePath:
					try:
						with open(filePath, 'rb') as f:
							file_data = f.read()
							file_type = imghdr.what(f.name)
							file_name = f.name
							msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
					except:
						print("Invalid Path Inputted")

		#Send message
		try:
			smtp.send_message(msg)
		except:
			print("Invalid Info Inputted")

		print("<<<<<<<<<<<< End of Message <<<<<<<<<<<<")

	smtp.quit()
	print('\nBye!')
	time.sleep(1)
