from sqlalchemy import Column, String, Integer
class Material_Front:
    id = Column(Integer, primary_key=True)
    name = Column(String)
    def __init__(self, id, value):
        self.id = id
        self.name = value