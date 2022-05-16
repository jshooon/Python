class ChatMsg:
    def __init__(self, contents, To=None, From=None, attach=None):
        self.contents = contents
        self.To = To
        self.From = From
        self.attach = attach
    def __str__(self):
        return "contents={}, To={}, From={}, attach={}".format(self.contents, self.To, self.From, True if self.attach else False)