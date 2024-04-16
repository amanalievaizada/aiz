class Bank:
    def __init__(self,name,age,money,key):
        self._name=name
        self._age=age
        self.__money=money
        self.__key=key

    def set_name(self,name):...

    def get_name(self):...

class RoyalBank(Bank):
    def __init__(self,name,age,money,key):
        super().__init__(name,age,money,key)

class PropertyBank(Bank):
    def __init__(self,name,age,money,key):
        super() .__init__(name,age,money,key)
        @property
        def money(self):
            return self.__money

        @money.setter
        def money(self,value):
            self.__money = value

    @property
    def key(self):
            return self.__key
    @key.setter
    def key(self,value):
            self.__key = value


