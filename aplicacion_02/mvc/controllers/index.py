 import web
import json  
from mvc.models.index import ModeloIndex

render = web.template.render('mvc/views/',  base='layout')
m_index = ModeloIndex()

class Index:
    def GET(self):
        try:
            contactos_json = m_index.obtener_contactos_json()
            contactos = json.loads(contactos_json)
            return render.index(contactos=contactos)
        except Exception as e:
            print(f"Error: {e}")
            return "Lo siento, algo salió mal."