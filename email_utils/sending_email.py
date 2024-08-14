import yagmail
def send_email(to_email,attachment_file_path):
    yag = yagmail.SMTP('email@gmail.com', 'password code from google')
    subject = ' Results '
    body = '''Hello, 
    This is the advanced sentiment analysis results.
    Let me know if there is any problem with it.
    Enjoy
    '''
    attachments=[attachment_file_path]
    yag.send(to=to_email, subject=subject, contents=body, attachments=attachments)
    print("Email sent successfully!")
