import os
import json
from prompt_toolkit import prompt
from datetime import datetime

flpath = "output.json"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("Type in your text, then press Esc + Enter to continue: ")
usrtxt = prompt(multiline=True)

class Entry:
    def __init__(self, id, content, tstamp):
        self.id = id
        self.content = content
        self.tstamp = tstamp

    def to_dict(self):
        return {
            "id": self.id,
            "content": self.content,
            "tstamp": self.tstamp
        }

if os.path.exists(flpath):
    with open('output.json', 'r') as file:
        nwlist = json.load(file)
    nxtid = len(nwlist) + 1
else:
    nwlist = []
    nxtid = 1

usrnote = Entry(nxtid, usrtxt, timestamp)
dictver = usrnote.to_dict()

nwlist.append(dictver)
print(dictver)

with open('output.json', 'w') as file:
    json.dump(nwlist, file, indent=4)