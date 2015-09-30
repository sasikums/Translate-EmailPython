#Script to take a phrase in English and emails a version of the phrase in a different language each time.I used it to send a daily message to my wife every day 
#I when I was out of the country. Use Windows task scheduler or a cron job to run
# script on a periodic basis. 

import goslate 
import random
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

# instaniate goslate object to access translation module
gs = goslate.Goslate()
#get list of supported languages
lang_dict=gs.get_languages()
languages = lang_dict.keys()
lcount=len(languages)


email_msg=""
#Specify english message to send
message="I love you to the moon and back!!"

#function to translate english message to randomly selected language
def trans():
	global email_msg
	#pick random integer from 0 to number of supported languages
	lchoice=random.randint(0,lcount-1)
	translate=gs.translate(message, languages[lchoice])
	language=lang_dict[languages[lchoice]]
	#if the characters are printable, update email_msg
	#if error on print run translate again until acceptable message is found
	try:
		print translate, "(",language,")"
		email_msg="".join([translate, "\n","(",language,")"])
	except:
		trans()

#call translation function
trans()

# Send an email with translated message
fromaddr = #insert email in quotes
toaddr = [#insert email in quotes]
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = ", ".join(toaddr)
msg['Subject'] = #insert Subject
body = email_msg
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.mailgun.org:587')
server.ehlo()
server.starttls()
server.ehlo()
server.login(#insert log-in info )
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)