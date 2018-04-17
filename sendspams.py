""" This file contains only the main function for sending a lot of spams.

@author: Ahmed Tidiane BALDE

"""

from mail import connectSMTP, logout
from spams import spam


def main():
    email = input("Enter your email: ")
    mdp = input("Enter your password: ")
    victime_name = input("Enter the victime's name: ")
    victime_mail = input("Enter the victime's mail: ")
    nbspams = int(input("Enter the number of spams to send: "))
    subject = input("Finally enter a subject: ")

    smtpObj = connectSMTP(email, mdp)

    spam(smtpObj,
         email,
         victime_name,
         victime_mail,
         subject,
         nbspams)

    logout(smtpObj)


if __name__ == '__main__':

    main()
