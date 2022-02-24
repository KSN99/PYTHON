#(920) 557-3390
#+19205573390
#AC887561da2c95cf8334769b2d19fa9900
#94981b418d56775bba6de2e266acc7af

# Download the helper library from https://www.twilio.com/docs/python/install

from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid ='AC887561da2c95cf8334769b2d19fa9900'
auth_token ='94981b418d56775bba6de2e266acc7af'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+19205573390',
                     to='+8201082649808'
                 )

print(message.sid)
