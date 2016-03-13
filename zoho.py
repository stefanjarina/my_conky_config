#!/usr/bin/env python
import os, imaplib
IMAP_USER = ''
IMAP_PASS = ''
IMAP_HOST = 'imap.zoho.com'

with imaplib.IMAP4_SSL(host=IMAP_HOST, port=imaplib.IMAP4_SSL_PORT) as mail:
    mail.login(IMAP_USER, IMAP_PASS)
    mail.select('INBOX')

    status, response = mail.search('INBOX', '(UNSEEN)')
    unread_msg_nums = response[0].split()

    print(len(unread_msg_nums))
