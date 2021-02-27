import smtplib
from string import Template
import os


dbuser = os.environ.get("USER")
dbpass = os.environ.get("DB_PASS")

print(dbuser,dbpass)

def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names,emails


def send_email(sub,msg,host):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        print(server)
        server.login(dbuser, dbpass)
        message = 'Subject: {}\n{}'.format(sub,msg)
        server.sendmail(dbuser, host, message)
        server.quit()
        print("Successful send\n")
    except:
        print("Email failed to send\n")


names, emails = get_contacts('email.txt')
message_template = read_template('msg.txt')


for name, emails in zip(names, emails):
    message = message_template.substitute(PERSON_NAME=name.title())
    host_email = emails
    print("progress for ", name)
    sub = "Email Automation System Free to use"
    send_email(sub,message, host_email)
