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
    output1 = localDB.get_output()
    output2 = localDB.process(Analysis.volume_surge)

    # Just report stock in focus

    output = """<!DOCTYPE html>
<html>
<head>
<style>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap-theme.min.css" integrity="sha384-rHyoN1iRsVXV4nD0JutlnGaslCJuC7uwjduW9SVrLvRYooPp2bWYgmgJQIXwl/Sp" crossorigin="anonymous">
</style>
</head>
<body>
{0}
{1}
{2}
{3}
</body>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>

</html>
"""


    title = 'Stock Info : ' + datetime.datetime.now().strftime('%Y-%m-%d')
    h_title = "<h1>" + title + "</h1>"
    msg_content = output.format(h_title, Services.get_available_resource(), output1, output2)
    # msg_content = output.format(title=title)
    message = MIMEText(msg_content, 'html')

    message['From'] = 'STAnalysis Auto Delivery <dcp.prto@gmail.com>'
    message['To'] = 'Beir Bear <beir.bear@gmail.com>'
    message['Cc'] = 'Pook <puku_9@hotmail.com>'
    message['Subject'] = title

    msg_full = message.as_string()

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login('dcp.prto@gmail.com', 'xxx')
    server.sendmail('dcp.prto@gmail.com',
                    ['beir.bear@gmail.com', ],
                    msg_full)
    server.quit()
