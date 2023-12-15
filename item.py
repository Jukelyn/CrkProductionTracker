class Item:

    def __init__(self, name: str, prodTime: int):
        self.name = name
        self.prodTime = prodTime

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def prodTime(self):
        return self._prodTime
    
    @prodTime.setter
    def prodTime(self, prodTime: int):
        self._prodTime = prodTime


    def __str__(self) -> str:
        return f"{self.name}: {self.prodTime} seconds"
