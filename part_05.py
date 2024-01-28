class Parser:
    def __init__(self, seperator, sentence):
        self.separtor = seperator
        self.sentencce = sentence

    def parse(self):
        # séparer les différens sesctions de la phrase grâce au séparateur
        words = self.sentencce.split(self.separtor)
        res = ""
        for word in words:
            if word.strip().isdigit(): # enlever les espaces au début et  la fin du mot et tester si'i ne contient que des chiffres
                res += word.strip()+" "
        return res


phrase = '8790: bonjour le monde:8987:7777:Hello World:    9007' 

p = Parser(':', phrase)
print( p.parse() )