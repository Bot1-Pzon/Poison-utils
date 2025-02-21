'''
	Funzionalità per il calcolo con grandezze fisiche tenendo conto delle incertezze.
'''

from Poison_utils import Console

SUPPORTED_UTNITS: tuple[14] = ('km', 'hm', 'dam', 'm', 'dm', 'cm', 'mm', 'km²', 'hm²', 'dam²', 'm²', 'dm²', 'cm²', 'mm²')

class Measure:


	def __init__(self, measure: int | float, uncertainty: int | float, unit: str) -> None:

		if not isinstance(measure, (int, float)):
			Console.Logs.fatal_error(f"La misura \"{measure}\" non è un numero supportato")

		if not isinstance(uncertainty, (int, float)):
			Console.Logs.fatal_error(f"L'incertezza \"{uncertainty}\" non è un numero supportato")

		if not isinstance(unit, str):
			Console.Logs.fatal_error(f"L'unità \"{unit}\" non è una stringa supportata")

		if unit not in SUPPORTED_UTNITS:
			Console.Logs.fatal_error(f"L'unità \"{unit}\" non è supportata")

		self.measure = measure
		self.uncertainty = uncertainty
		self.unit = unit


	def __add__(self, other: 'Measure') -> 'Measure':

		if type(self) is not Measure or type(other) is not Measure:
			Console.Logs.fatal_error(f"Non sono supportate le operazioni tra \"{self}\" di tipo: \"{type(self)}\" e \"{other}\" di tipo \"{type(other)}\"")

		if self.unit != other.unit:
			Console.Logs.fatal_error(f"Non sono supportate le operazioni tra \"{self}\" di unità \"{self.unit}\" e \"{other}\" di unità \"{other.unit}\"")

		resulting_measure = self.measure + other.measure
		resulting_uncertainty = self.uncertainty + other.uncertainty

		return Measure(measure = resulting_measure, uncertainty = resulting_uncertainty, unit = self.unit)


	def __sub__(self, other: 'Measure') -> 'Measure':

		if type(self) is not Measure or type(other) is not Measure:
			Console.Logs.fatal_error(f"Non sono supportate le operazioni tra \"{self}\" di tipo: \"{type(self)}\" e \"{other}\" di tipo \"{type(other)}\"")

		if self.unit != other.unit:
			Console.Logs.fatal_error(f"Non sono supportate le operazioni tra \"{self}\" di unità \"{self.unit}\" e \"{other}\" di unità \"{other.unit}\"")

		resulting_measure = self.measure - other.measure
		resulting_uncertainty = self.uncertainty + other.uncertainty

		return Measure(measure = resulting_measure, uncertainty = resulting_uncertainty, unit = self.unit)


	def __mul__(self, other: 'Measure') -> 'Measure':

		if type(self) is not Measure or type(other) is not Measure:
			Console.Logs.fatal_error(f"Non sono supportate le operazioni tra \"{self}\" di tipo: \"{type(self)}\" e \"{other}\" di tipo \"{type(other)}\"")

		if self.unit != other.unit:
			Console.Logs.fatal_error(f"Non sono supportate la moltiplicazione tra tra \"{self}\" di unità \"{self.unit}\" e \"{other}\" di unità \"{other.unit}\"")

		resulting_measure = self.measure * other.measure

		relative_error = (self.uncertainty / self.measure) + (other.uncertainty / other.measure)
		resulting_uncertainty = self.uncertainty + other.uncertainty * relative_error

		resulting_unit = f"{self.unit}²"

		return Measure(measure = resulting_measure, uncertainty = resulting_uncertainty, unit = resulting_unit)


	def __truediv__(self, other: 'Measure') -> 'Measure':

		if type(self) is not Measure or type(other) is not Measure:
			Console.Logs.fatal_error(f"Non sono supportate le operazioni tra \"{self}\" di tipo: \"{type(self)}\" e \"{other}\" di tipo \"{type(other)}\"")

		if self.unit != other.unit:
			Console.Logs.fatal_error(f"Non sono supportate la moltiplicazione tra tra \"{self}\" di unità \"{self.unit}\" e \"{other}\" di unità \"{other.unit}\"")

		resulting_measure = self.measure / other.measure

		relative_error = (self.uncertainty / self.measure) + (other.uncertainty / other.measure)
		resulting_uncertainty = self.uncertainty + other.uncertainty * relative_error

		return Measure(measure = resulting_measure, uncertainty = resulting_uncertainty, unit = self.unit)


	def __str__(self) -> str:
		return f"({self.measure} ± {self.uncertainty}){self.unit}"
