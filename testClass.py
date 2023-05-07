class person:
    def __init__(self,saxeli, gvari):
        self.saxeli = saxeli
        self.gvari = gvari
    
    def gamotana(self):
        print (self.saxeli, self.gvari)

vakaki = person("Zura", "Chavchavadze")
vakaki.gamotana()