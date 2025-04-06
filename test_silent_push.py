from apns2.client import APNsClient
from apns2.payload import Payload
from apns2.credentials import TokenCredentials

auth_key_path = '/Users/marconi/Downloads/AuthKey_xxx.p8'
auth_key_id = 'xxx'
team_id = 'xxx'
topic = 'com.kenmaro.microsoftAuthentication'

token_credentials = TokenCredentials(auth_key_path=auth_key_path, auth_key_id=auth_key_id, team_id=team_id)

client = APNsClient(credentials=token_credentials, use_sandbox=True)

payload = Payload(content_available=True)

test_device_token = 'xxx'

client.send_notification(test_device_token, payload, topic)
print("sent silent push")

