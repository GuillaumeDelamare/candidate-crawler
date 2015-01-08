# -*- coding: utf-8 -*-

###############################################
# Job Crawler - E-mail program                #
# Created by RIVES Yann                       #
# Crawl some website to find interesting jobs #
###############################################

### External modules importation ###

import smtplib
#import email.mime
from email.mime.text import MIMEText

### End of external modules importation ###

### Custom modules importation ###

### End of custom modules importation ###

### Classes ###
class JobCrawlerEmail(object):

    def _values_initializer(self, profile_name, receiver):
        """Method to initialize variables"""
        self.sender = "consept.toulouse@gmail.com"
        self.receiver = receiver
        self.subject = profile_name

        self.mail_host = "smtp.gmail.com"
        self.mail_port = 587

        self.username = "consept.toulouse"
        self.password = "consept31"

    def _message_setup(self):
        """Method to set message content"""
        message_body = "Bonjour\n\n"

        if self.links:
            message_body = message_body + "Voici les nouvelles annonces trouvées:\n"
            for link in self.links:
                message_body = message_body + link + "\n"
        else:
            message_body = message_body + "Pas de nouvelles annonces\n"

        message_body = message_body + "\nBonne journée"

        self.message = MIMEText(message_body)
        self.message['From'] = self.sender
        self.message['To'] = self.people

        self.message['Subject'] = "Job crawling - {}".format(self.subject)

    def _send_email(self):
        """Method to send e-mail"""
        server = smtplib.SMTP(self.mail_host, self.mail_port)
        server.starttls()
        server.login(self.username, self.password)
        smtplib.SMTP.ehlo(server)
        server.sendmail(self.sender, self.people, self.message.as_string())
        server.quit()

    def run_program(self, profile_name, receiver, links):
        """Method to run program"""
        print("Sending E-mail ...")

        self.links = links

        self._values_initializer(profile_name, receiver)

        for self.people in self.receiver:
            self._message_setup()
            self._send_email()

        print("E-mail sent")

### End of Classes ###

### Main program ###

if __name__=='__main__':
    print("This program is a module, it has to be piloted")

### End of Main program ###
