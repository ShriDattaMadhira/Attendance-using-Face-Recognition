from twilio.rest import Client
account_sid = "<account_sid>"
auth_token = "<auth_token>"
client =Client(account_sid,auth_token)
message= client.messages.create(to="+91",from_="",body="hello")
print(message.sid)