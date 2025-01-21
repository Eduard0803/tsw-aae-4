class Decode:

    __VOGAIS = ['a', 'e', 'i', 'o', 'u']
    __ALFABETO = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    __NUMERO = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    __SIMBOLOS = {
        '*': '@',
        '|': '!',
        '$': '?',
        '_': ' ',
    }

    def decode_numero(self, n):
        if n in Decode.__NUMERO:
            idx = Decode.__NUMERO.index(str(n))-1
            return Decode.__NUMERO[idx]
        return n
    
    def decode_consoante(self, n):
        # a b c d e f g h i j k l m n o p q r s t u v w x y z
        # z y x w v u t s r q p o n m l k j i h g f e d c b a
        if n in Decode.__ALFABETO and n not in Decode.__VOGAIS :
            idx = len(Decode.__ALFABETO)-Decode.__ALFABETO.index(str(n))-1
            return Decode.__ALFABETO[idx]
        return n

    def decode_simbolo(self, n):
        if n in Decode.__SIMBOLOS:
            return Decode.__SIMBOLOS[n]
        if n in ['#', '^']:
            return ''
        return n

    def remove_vogal_dupla(self, a, b):
        pass

    def decode(self, message: str) -> str:
        message = message.lower()
        out = ''
        for i in range(len(message)):
            buffer = ''
            if i > 0:
                buffer = self.remove_vogal_dupla(message[i], message[i-1])
            if message[i].isalpha():
                buffer = self.decode_consoante(message[i])
            elif message[i].isdigit():
                buffer = self.decode_numero(message[i])
            else:
                buffer = self.decode_simbolo(message[i])
            out += buffer
        return out
