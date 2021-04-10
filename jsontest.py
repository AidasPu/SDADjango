import json


class testing():
    def __init__(self, something, something_else):
        self.something = something
        self.something_else = something_else


t = testing("text", "other_text").__dict__
a = testing("another_text", "other_another_text").__dict__
list1 = [t, a]
for record in list1:
    objects = {"title": record.get("something"), "address": record.get("something_else")}

print(json.dumps(objects))
