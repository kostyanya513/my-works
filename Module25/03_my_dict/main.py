class Dict:
    __slovar = {1: 'first', 2: 'second', 3: 'therd'}

    def get_slovar(self):
        return self.__slovar

    def get(self, key):
        if key in self.__slovar:
            return self.__slovar[key]
        else:
            return None


class MyDict(Dict):
    def get(self, key):
        if key in self.get_slovar():
            return self.get_slovar()[key]
        else:
            return 0


mydict = MyDict()
print(mydict.get(4))
