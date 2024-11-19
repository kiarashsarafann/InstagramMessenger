import time
from instagrapi import Client

cl = Client()
cl.login("Username", "password")

usernames = ['InstagramUsers']
message = "this is test message!"

for username in usernames:
    try:
        user_id = cl.user_id_from_username(username)
        cl.direct_send(message, [user_id])
        print(f"message is delivered to {username}")
    except Exception as e:
        print(f"error in send message to{username}: {e}")

    time.sleep(60)