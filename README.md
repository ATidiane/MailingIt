# MailingIt

## Send emails(or spams) and text messages using python ##

To send spams do: ```python or python3 sendspams.py```

To delete mails or (spams): ```python or python3 deletespams.py```

But before, you should **configure a request** withing the file deletespams.py for seearching the emails you want to delete.

This is **really __dangerous__**, make sure, there isn't any mistake in your request.

You can add the date and the person's email you want to delete emails from. For instance :
 ```
 uids = searchmails(imapObj,
                    '[Gmail]/Messages envoyés',
                     ON='17-Apr-2018',
                     FROM='mail.gmail.com')
                     
 deletemails(imapObj, uids)
 ```
 Of course, you will not forget to change the value of parameters (FROM, ON, etc...)
 
 You can **select** the folder where to search for emails, for those who have **gmail**, you might have the choices below:
     
    'INBOX'
    '[Gmail]'
    '[Gmail]/Brouillons'
    '[Gmail]/Corbeille'
    '[Gmail]/Important'
    '[Gmail]/Messages envoyés'
    '[Gmail]/Spam'
    '[Gmail]/Suivis'
    '[Gmail]/Tous les messages'
   
And you can add many many filters in the parameters, in this exemple i added only ON and FROM but you can use the link below
in the chapter *Sending emails and Text messages*, section *Performing the search*, to add more parameters:

https://automatetheboringstuff.com/chapter16/

In the next versions, I'll try to automate the process of deleting mails within the command line.

Have **fun** and great **spamming** !


## References ##
[Automate the Boring Stuff with Python](https://automatetheboringstuff.com)
