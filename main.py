from client import *
from settings import USER_TOKEN


c = Client()

with open('error.html', 'w') as f:
    f.write(c.messages())#body='hello, world', receiver=USER_TOKEN))

print "done"