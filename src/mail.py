from win32com.client import Dispatch
import getpass
import datetime 



########################################
## Connect to Outlook inbox
#########################################
outlook = Dispatch("Outlook.Application").GetNamespace("MAPI")
# "6" refers to the index of a folder. 6 is the inbox
inbox = outlook.GetDefaultFolder("6")



### all inbox for today after 7am
all_inbox = inbox.Items.restrict("[ReceivedTime] > '"+ datetime.datetime.today().strftime('%d/%m/%Y')+" 05:00 AM'")

#mydate = datetime.datetime.today().strftime('%d/%m/%Y')

# startdate = datetime.date(2019, 9, 1).strftime('%d/%m/%Y')
# rightnow  = datetime.datetime.today().strftime('%d/%m/%Y')

# all_inbox = inbox.Items.restrict(   "[ReceivedTime] > '" \
                                    # + startdate \
                                    # + " 07:00 AM' and [ReceivedTime] < '" \
                                    # + rightnow\
                                    # + " 07:00 AM'")
##################
## Loop through e-mails and attachments 
##################

for msg in all_inbox:
    ## prints subject
    #print( msg.Subject, msg.SenderEmailAddress )
    print( msg.SenderEmailAddress )
    print( msg.body )
    
