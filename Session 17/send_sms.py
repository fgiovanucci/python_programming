# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "ACc99bfe131a7f26a1cf6c510f88a92a56"
auth_token = "3ecb1def3ec181eb1c720f67fddfc9b4"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+15082088537", from_="+15082324694",
                                     body="Hello there!")