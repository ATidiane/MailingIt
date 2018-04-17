""" File contains the spam function, you can modify it to replace the body
of your spams emails when sending for instance.

@author: Ahmed Tidiane BALDE

 """

from mail import sendmail


def spam(smtpObj, phrom, name, to, subject, nbspams=None):
    count = 0
    while True and nbspams is None:
        sendmail(smtpObj,
                 phrom,
                 to,
                 subject,
                 "< I can proudly say that I am {} >\n"
                 " ----------\n"
                 "    \               ,-----._\n"
                 "  .  \         .  ,'        `-.__,------._\n"
                 " //   \      __\\'                        `-.\n"
                 "((    _____-'___))                           |\n"
                 " `:='/     (alf_/                            |\n"
                 " `.=|      |='                               |\n"
                 "    |)   O |                                  \\\n"
                 "    |      |                               /\  \\\n"
                 "    |     /                          .    /  \  \\\n"
                 "    |    .-..__            ___   .--' \  |\   \  |\n"
                 "   |o o  |     ``--.___.  /   `-'      \  \\   \ |\n"
                 "    `--''        '  .' / /             |  | |   | \\\n"
                 "                 |  | / /              |  | |   mmm\n"
                 "                 |  ||  |              | /| |\n"
                 "                 ( .' \ \              || | |\n"
                 "                 | |   \ \            // / /\n"
                 "                 | |    \ \          || |_|\n"
                 "                /  |    |_/         /_|\n"
                 "               /__/".format(name))
        count += 1
        print(count)
    else:
        for i in range(nbspams):
            sendmail(smtpObj,
                     phrom,
                     to,
                     subject,
                     "< I can proudly say that I am {} >\n"
                     " ----------\n"
                     "    \               ,-----._\n"
                     "  .  \         .  ,'        `-.__,------._\n"
                     " //   \      __\\'                        `-.\n"
                     "((    _____-'___))                           |\n"
                     " `:='/     (alf_/                            |\n"
                     " `.=|      |='                               |\n"
                     "    |)   O |                                  \\\n"
                     "    |      |                               /\  \\\n"
                     "    |     /                          .    /  \  \\\n"
                     "    |    .-..__            ___   .--' \  |\   \  |\n"
                     "   |o o  |     ``--.___.  /   `-'      \  \\   \ |\n"
                     "    `--''        '  .' / /             |  | |   | \\\n"
                     "                 |  | / /              |  | |   mmm\n"
                     "                 |  ||  |              | /| |\n"
                     "                 ( .' \ \              || | |\n"
                     "                 | |   \ \            // / /\n"
                     "                 | |    \ \          || |_|\n"
                     "                /  |    |_/         /_|\n"
                     "               /__/".format(name))
            count += 1
            print(count)
