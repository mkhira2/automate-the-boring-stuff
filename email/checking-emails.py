import imapclient, pyzmail

# see imap cheat sheet for other available methods

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)

# setup
conn.login('testemailforatbswp@gmail.com', 'swordfish')

conn.select_folder('INBOX', readonly=True)

UIDs = conn.search(['SINCE 20-Aug-2018']) # date format [BEFORE, ON, SINCE] XX-XXX-XXXX
print(UIDs) # returns list like [47416, 47417, 47418, 47419, 47420, 47421...]

rawMessage = conn.fetch([47420], ['BODY', 'FLAGS'])
message = pyzmail.PyzMessage.factory(rawMessage[47420][b'BODY[]'])

# the payoff
print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))

print(message.text_part) # discover if email is text...
print(message.html_part) # ...or html

print(message.text_part.get_payload().decode('UTF-8')) # 99% of the time encoding is UTF-8; may be different charset

# danger zone - deleting emails
# conn.select_folder('INBOX', readonly=False)
# UIDs = conn.search(['ON 23-Aug-2018'])
# conn.delete_messages([47420]) # delete single email
# conn.delete_messages(UIDs) # delete all passed-in emails