from sqlalchemy import Column, String, Integer
class Material_Lens:
    id = Column(Integer, primary_key=True)
    name = Column(String)
    def __init__(self, id, name):
        self.id = id
        self.name = name