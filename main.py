from pypresence import Presence
import time
import random

client_id = '853335508713341008'
RPC = Presence(client_id)
RPC.connect()


count = 1000
while True:
    RPC.update(details="Ded outside", state=f"{count} - 7 = {count - 7}", large_image="ads",large_text="Че",small_image="eblo", small_text="Dev by - VandenGG#3142")
    count-=7
    if count <= 7:
        count = 1000
    time.sleep(3)