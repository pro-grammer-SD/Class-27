class Parrot(object):
    """docstring for Parrot."""
    def __init__(self):
        super(Parrot, self).__init__()
        
        self.talks = True
        self.hits_on_my_damn_head = True

    def talk(self):
        return "Wee!"
    
    def hit_on_my_damn_head(self):
        return """I like hitting you Soumalya; 
                you didn't give me much to eat last week!"""
                