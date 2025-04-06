from apns2.client import APNsClient
from apns2.payload import Payload
from apns2.credentials import TokenCredentials

auth_key_path = 'xxx'
auth_key_id = 'xxx'
team_id = 'xxx'
topic = 'xxx'

token_credentials = TokenCredentials(auth_key_path=auth_key_path, auth_key_id=auth_key_id, team_id=team_id)
client = APNsClient(credentials=token_credentials, use_sandbox=True)

# Include a badge value along with alert and sound if desired.
payload = Payload(alert="Hello World!", sound="default", badge=1)
test_device_token = 'xxx'

print("Sent notification to device:", test_device_token)

client.send_notification(test_device_token, payload, topic)
print("Sent notification with badge")
