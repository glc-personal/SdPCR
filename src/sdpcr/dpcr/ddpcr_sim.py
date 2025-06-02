from .dpcr_sim_base import DpcrSimBase
from typing import Dict, Any
import numpy as np

class DdpcrSim(DpcrSimBase):
	""" Simulates droplet-based dPCR """
	
	def __init__(self, parameters: Dict[str, Any]):
		super().__init__(parameters)
		self.num_droplets = parameters.get("num_droplets", 2000)
		self.target_copies = parameters.get("target_copies", 1000)
		self.volume = parameters.get("droplet_volume", 0.00085) # uL

	def run(self) -> Dict[str, Any]:
		""" Simulate Poisson-based distribution of target molecules """
		lambda_ = self.target_copies / self.num_droplets
		droplet_hits = np.random.poisson(lambda_, size=self.num_droplets)
		positive_droplets = (droplet_hits > 0).sum()

		return {
			"positive_droplets": int(positive_droplets),
			"total_droplets": self.num_droplets,
			"fraction_positive": positive_droplets / self.num_droplets,
		}
