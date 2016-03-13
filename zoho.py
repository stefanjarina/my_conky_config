#!/usr/bin/env python
import os, imaplib
ZOHO_USER = ''
ZOHO_PASS = ''

with imaplib.IMAP4_SSL(host='imap.zoho.com', port=imaplib.IMAP4_SSL_PORT) as mail:
    mail.login(ZOHO_USER, ZOHO_PASS)
    mail.select('INBOX')

    status, response = mail.search('INBOX', '(UNSEEN)')
    unread_msg_nums = response[0].split()

    print(len(unread_msg_nums))
