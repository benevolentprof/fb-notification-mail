#!/usr/bin/env python3

""" get_messages.py
    Parse out the message body from an mbox file containing Facebook notifications
    from the Send up the Count group
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2016 Susan Sim"
__license__ = "MIT License"


import mailbox
import re
import csv

def getbody(message): #getting plain text 'email body'
    body = None
    if message.is_multipart():
        for part in message.walk():
            if part.is_multipart():
                for subpart in part.walk():
                    if subpart.get_content_type() == 'text/plain':
                        body = subpart.get_payload(decode=True)
            elif part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True)
    elif message.get_content_type() == 'text/plain':
        body = message.get_payload(decode=True)
    return body


mbox = mailbox.mbox('sutc.mbox')
quoted = re.compile("\"(.*)\"")
new_photo = re.compile("New photo")
new_link = re.compile("New link")

msgOutput = open("vacPost.txt", "w")

for message in mbox:
    payload = ""

    # Check the subject for "New photo" and "New link" posts
    # No need to examine the message body in these cases
    if new_photo.search(message['subject']):
        payload = "New photo"
    elif new_link.search(message['subject']):
        payload = "New link"
    else:
        # Check the body for a quoted string
        body = getbody(message)

        match = quoted.search(body)
        # No match means that notification is for a comment
        if match is not None:
            payload = match.group()

    # We have some output
    if payload != "":
        # Pull out the name of the poster
        name = quoted.search(message['from'])
        if name is None:
            sender = ""
        else:
            sender = name.group()

        # print the output
        # print sender
        # print message['date']
        # print payload

        output = sender + ",\"" + message["date"] + "\"," + payload + "\n"
        #print output,
        msgOutput.write(output)  #Create a csv output file

msgOutput.close()


