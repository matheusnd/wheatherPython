from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACc899cc53a439016c8f4407faf9d86d3b'
auth_token = '6a6e0e3ad267dd660130ae9e98a2051b'

def sendSms(Text):
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body='Eu sei o que voce fez',
            from_='+5524933007029',
            to='++5511959959245'
        )

    return (message.sid)