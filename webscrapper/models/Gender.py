from sqlalchemy import Column, String, Integer
class Gender:
    id = Column(Integer, primary_key=True)
    name = Column(String)
    def __init__(self, id, name):
        self.id = id
        self.name = name