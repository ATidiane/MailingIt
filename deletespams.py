""" This file contains the main function for delete spams given a search
request and the folder to search

@author: Ahmed Tidiane BALDE

"""

from mail import connectImap, deletemails, listfolders, logout, searchmails


def main():
    """ The possible folders are: (depending on your service provider)
    You can select one of those to search emails from or delete emails

    'INBOX'
    '[Gmail]'
    '[Gmail]/Brouillons'
    '[Gmail]/Corbeille'
    '[Gmail]/Important'
    '[Gmail]/Messages envoyés'
    '[Gmail]/Spam'
    '[Gmail]/Suivis'
    '[Gmail]/Tous les messages'

    """

    email = input("Enter you email: ")
    mdp = input("Enter your password: ")
    imapObj = connectImap(email, mdp)

    # print list of folders, might help if you do not have gmail like me
    print(listfolders(imapObj))

    # TODO, ask those filters on the terminal

    uids = searchmails(imapObj,
                       '[Gmail]/Messages envoyés',
                       ON='17-Apr-2018',
                       FROM='baldeahmedtidiane36@gmail.com')

    logout(imapObj, 'imap')


if __name__ == '__main__':

    main()
