__author__ = 'sudeep'

def send_email(recipient, sender, text):
        if text is not '':
            import smtplib
            import email.mime.multipart
            import email.mime.text

            gmail_user = "supahcoollinks@gmail.com"
            FROM = 'SupahCool Links'
            TO = recipient
            SUBJECT = "You have new links to check out!"
            TEXT = text
            REPLY_TO_ADDRESS = sender

            # Prepare actual message

            msg = email.mime.multipart.MIMEMultipart()
            msg['to'] = TO
            msg['from'] = FROM
            msg['subject'] = SUBJECT
            msg.add_header('reply-to', REPLY_TO_ADDRESS)
            msg.attach(email.mime.text.MIMEText(TEXT))

            message = """From: %s\nTo: %s\nSubject: %s\nReply-To: %s\n\n%s
            """ % (FROM, ", ".join(TO), SUBJECT, REPLY_TO_ADDRESS, TEXT)
            try:
                #server = smtplib.SMTP(SERVER)
                server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
                server.ehlo()
                server.starttls()
                server.login(gmail_user, get_password())
                server.debuglevel = 1
                server.sendmail(FROM, TO, msg.as_string())
                #server.quit()
                server.close()
                print 'successfully sent the mail'
            except Exception, e:
                print "failed to send mail: %s" % str(e)


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
