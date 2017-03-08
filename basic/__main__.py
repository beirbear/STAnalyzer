from basic.localDB import LocalDB
from basic.services import Services
import smtplib
from email.mime.text import MIMEText
import datetime
from basic.analysis import Analysis

if __name__ == '__main__':
    """
    Entry point
    """
    print("Basic Analysis")

    # Load configuration from file
    localDB = LocalDB()
    output = localDB.get_output()
    output += localDB.process(Analysis.volume_surge)

    # Just report stock in focus

    title = 'Stock Info : ' + datetime.datetime.now().strftime('%Y-%m-%d')
    msg_content = output.format(title=title)
    msg_content += "<h3>Available Resource</h3>" + Services.get_available_resource()
    message = MIMEText(msg_content, 'html')

    message['From'] = 'STAnalysis Auto Delivery <dcp.prto@gmail.com>'
    message['To'] = 'Beir Bear <beir.bear@gmail.com>'
    message['Cc'] = 'Pook <puku_9@hotmail.com>'
    message['Subject'] = title

    msg_full = message.as_string()

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login('dcp.prto@gmail.com', 'xxxx')
    server.sendmail('dcp.prto@gmail.com',
                    ['beir.bear@gmail.com', ],
                    msg_full)
    server.quit()
