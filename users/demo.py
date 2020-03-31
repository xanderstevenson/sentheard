import sendgrid
import os
from sendgrid.helpers.mail import Mail, Content, To, Email

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("DoNotReply@sentheard.com")
to_email = To("xanderstevenson2@gmail.com")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())


print(response.status_code)
print(response.body)
print(response.headers)