from abc import ABC, abstractmethod
from typing import Any, Dict

class DpcrSimBase(ABC):
	""" Abstract base class for all dPCR simulation models """

	def __init__(self, parameters: Dict[str, Any]):
		self.parameters = parameters

	@abstractmethod
	def run(self) -> Dict[str, Any]:
		""" Run the sim and return results """
		pass
