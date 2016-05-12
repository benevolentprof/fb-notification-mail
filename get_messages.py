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

for message in mbox:
    print message['from']
    print message['subject']
    text = getbody(message)
    print text
