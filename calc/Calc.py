# -*-coding: utf8 -*-

from sympy import *
class calc():
	def parse_latex(self,fun):
		dif = latex(S(fun,evaluate=False))
		print dif
		solc = str(dif)
		return solc

	def limites(self,fun):
		"""El primer argumento es la funcion, el segundo es el
		simbolo x, y el tercero es hacia donde tiende acercarse x.
		Si se dieron cuenta, en el segundo ejemplo, que x tiende al
	    infinito, esto lo hice con el atributo oo de SymPy que
        equivale a  ∞.   limx→x0f(x)"""
		x, y = symbols('x y')
		dif = limit(fun,x,oo)
		dif = latex(dif)
		solc = str(dif)
		return solc
		
	def derivadas(self,fun):
		x, y = symbols('x y')
		dif = diff(fun,x)
		dif = latex(dif)
		solc = str(dif)
		return solc
	
	def integrales(self,fun):
	    """Al momento de calcular una integral
	    definida debemos pasarle a parte de la
	    expresion matematica, (variable_integracion,
	    limite_inferior, limite_superior), como se
	    muestra en el primer ejemplo. En el primer
	    ejemplo como pueden ver, se hace uso de exp()
	    el cual es la función exponencial, también vemos sympy.oo,
	    esto es equivalente al símbolo de infinito."""
	    x, y = symbols('x y')
	    dif = integrate(fun)
	    dif = latex(dif)
	    solc = str(dif)
	    return solc
	
	
	def  ecu_dif(self,fun):
		y = symbols('y', cls=Function)
		x = symbols('x')
		diffeq = Eq(fun)
		sol = dsolve(diffeq, y(x))
		sol = latex(sol)
		solc=str(sol)
		pprint(diffeq)
		pprint(sol)
		return solc
		
	def control(self, cad ,tipo):
		fun = sympify(cad)
		if tipo=='l':
			return self.limites(fun)
		elif tipo == 'd':
			return self.derivadas(fun)
		elif tipo == 'i':
			return self.integrales(fun)
		elif tipo == 'ed':
			return  self.ecu_dif(fun)