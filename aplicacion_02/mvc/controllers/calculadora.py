import web
from mvc.models.calculadora import Calculadora

render = web.template.render('mvc/views/', base='layout')

class Calculadoracontrolador:
    def GET(self, operacion=None):
        if not operacion:
            return render.calculadora(operacion=None, resultado=None)
        return render.calculadora(operacion=operacion, resultado=None)

    def POST(self):
        try:
            data = web.input(operacion=None, numero1=None, numero2=None)
            operacion = data.operacion
            numero1 = float(data.numero1)
            numero2 = float(data.numero2)

            calculadora = Calculadora(numero1, numero2)

            if operacion in ['suma', 'resta', 'multiplicacion', 'division']:
                resultado = getattr(calculadora, operacion)()
            else:
                return "Operación no válida"

            return render.calculadora(operacion=operacion, resultado=str(resultado))
        except ValueError as e:
            print(f"Error: {e}")
            return f"Error: {e}"
