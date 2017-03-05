from basic.localDB import LocalDB
import smtplib
from email.mime.text import MIMEText
import datetime

if __name__ == '__main__':
    """
    Entry point
    """
    print("Basic Analysis")

    # Load configuration from file
    localDB = LocalDB()

    # Just report stock in focus


    title = 'Stock Info : ' + datetime.datetime.now().strftime('%Y-%m-%d')
    msg_content = '<p>' + localDB.get_output() + '</p>'.format(title=title)
    message = MIMEText(msg_content, 'html')

    message['From'] = 'Sender Name <beir.bear@gmail.com>'
    message['To'] = 'Receiver Name <beir.bear@gmail.com>'
    message['Cc'] = 'Receiver2 Name <beir.bear@gmail.com>'
    message['Subject'] = 'Any subject'

    msg_full = message.as_string()

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login('beir.bear@gmail.com', '')
    server.sendmail('beir.bear@gmail.com',
                    ['beir.bear@gmail.com', ],
                    msg_full)
    server.quit()