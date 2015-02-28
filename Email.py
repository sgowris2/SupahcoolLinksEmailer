__author__ = 'sudeep'

def send_email(recipient, text):
        if text is not '':
            import smtplib

            gmail_user = "supahcoollinks@gmail.com"
            FROM = 'supahcoollinks@gmail.com'
            TO = [recipient]
            SUBJECT = "You have new links to check out!"
            TEXT = text

            # Prepare actual message
            message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
            """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
            try:
                #server = smtplib.SMTP(SERVER)
                server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
                server.ehlo()
                server.starttls()
                server.login(gmail_user, get_password())
                server.debuglevel = 1
                server.sendmail(FROM, TO, message)
                #server.quit()
                server.close()
                print 'successfully sent the mail'
            except:
                print "failed to send mail"


def compose_email(participant, participants):
    index = 0
    text = 'The following links were added recently: \n\n'
    others = [i for i in participants if i.name is not participant.name]
    for x in others:
        for y in x.diff_links:
            index += 1
            text += index.__str__() + '. ' + y.url + ' - ' + y.comment + '\n'
    if(index == 0):
        text = ''
    return text

def get_password():
    with open('../gmailKey.key', 'r') as key_file:
        return key_file.read().replace('\n', '')