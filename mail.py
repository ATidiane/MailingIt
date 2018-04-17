""" This file contains all the necessary functions to send,
search or delete emails

@author: Ahmed Tidiane BALDE

"""


import imaplib
import smtplib

import imapclient

# To fix the size error
imaplib._MAXLINE = 10000000


class UnknownValueException(Exception):
    def __init__(self, value):
        """ Initialize the exception

        :param value: value that causes the exception

        """

        self.value = value

    def __str__(self):
        """ Print the value when the exception occurs """

        return repr("Unknown value : {}".format(self.value))


def getDomain(email, protocol="smtp"):
    """ Get the server domain name giving the protocol and an email

    :param protocol: smtp or imap
    :param email: login an e-mail
    :returns:
    :rtype:

    """

    protocol = protocol.lower()
    if protocol not in ("smtp", "imap"):
        raise UnknownValueException(protocol)

    domain = email.split('@')[1].split('.')[0]

    if domain == "gmail":
        return 587, protocol + '.' + domain + '.com'
    elif domain in ("outlook", "hotmail"):
        return 587, protocol + '-mail.' + domain + '.com'
    elif domain == "yahoo":
        return 587, protocol + '.mail.' + domain + '.com'
    elif domain == "att":
        return 465, protocol + '.mail.' + domain + '.net'
    elif domain == "comcast":
        return 587, protocol + '.' + domain + '.net'
    elif domain == "verizon":
        return 465, protocol + '.' + domain + '.net'
    else:
        raise UnknownValueException(domain)


def connectImap(email, mdp):
    """ Connect to an IMAP server

    :param email: login
    :param mdp: password
    :param domain: domain name of the imap server
    :returns: an imapclient that connects into the server
    :rtype: IMAPClient Object

    """

    port, domain = getDomain(email, "imap")
    print(domain)
    imapObj = imapclient.IMAPClient(domain, ssl=True)
    imapObj.login(email, mdp)

    return imapObj


def connectSMTP(email, mdp):
    """FIXME! briefly describe function

    :param email: login
    :param mdp: password
    :param port: 587 for TLS and 465 for SSL
    :param domain: domain name of the imap server
    :returns: the smtp object
    :rtype: SMTP Object

    """

    port, domain = getDomain(email)

    print(domain)
    smtpObj = None
    if port == 587:
        smtpObj = smtplib.SMTP(domain, port)
        smtpObj.ehlo()
        # Enable TLS encryption if you are using 587 port
        smtpObj.starttls()

    elif port == 465:
        # Encryption is automatically set up
        smtpObj = smtplib.SMTP_SSL(domain, port)
        smtpObj.ehlo()
    else:
        raise UnknownValueException(port)

    smtpObj.login(email, mdp)

    return smtpObj


def logout(obj, protocol='smtp'):
    protocol = protocol.lower()
    if protocol == 'smtp':
        obj.quit()
    elif protocol == 'imap':
        obj.logout()
    else:
        raise UnknownValueException(protocol)


def sendmail(smtpObj, phrom, to, subject=None, body=None):
    """ Send email from "phrom" to "to"

    :param smtpObj: Object that connects into the mail
    :param phrom: from
    :param to: to
    :param subject: Subject of the email
    :param body: body of the email
    :returns: send an email
    :rtype: void

    """

    smtpObj.sendmail(phrom, to, 'Subject: {}\n{}'.format(subject, body))


def listfolders(imapObj):
    """ List the folders of an account

    :param imapObj: Object that connects into the mail
    :returns: prints the list of folders of the account
    :rtype: void

    """

    return imapObj.list_folders()


def deletefolder(imapObj, folder):
    """ Delete a folder

    :param imapObj: Object that connects into the mail
    :param folder: the folder to delete
    :rtype: void
    :returns: delete emails

    """

    imapObj.delete_folder(folder)


def searchmails(imapObj, folder='INBOX', **kwargs):
    """ Search emails given infinite args

    :param imapObj: Object that connects into the mail
    :param folder: folder from which to search emails

    """

    imapObj.select_folder(folder)
    requete = []
    for key in kwargs:
        requete += ['{}'.format(key), '{}'.format(kwargs[key])]

    uids = imapObj.search(requete)

    return uids


def deletemails(imapObj, uids):
    """ Delete an email from phrom

    :param imapObj: Object that connects into the mail
    :param uids: list of uids from which to delete emails

    """

    imapObj.delete_messages(uids)
