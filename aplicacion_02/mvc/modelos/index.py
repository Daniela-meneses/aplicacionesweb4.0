import  web
import json

class ModeloIndex:
    def _init_(self):
        self.contactos = [
            {"nombre": "Carlos", "edad": 25, "email": "amor@lizbeth.com"},
            {"nombre": "Juan", "edad": 30, "email": "juan@example.com"},
            {"nombre": "María", "edad": 28, "email": "maria@example.com"}
        ]

    def obtener_contactos_json(self):
        return json.dumps(self.contactos)