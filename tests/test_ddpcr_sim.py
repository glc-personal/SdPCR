from sdpcr.dpcr.ddpcr_sim import DdpcrSim

def test_ddpcr_sim_run():
	params = {
		"num_droplets": 20000,
		"target_copies": 1000,
		"droplet_volume": 0.00085
	}
	
	sim = DdpcrSim(params)
	result = sim.run()

	# Basic checks
	assert isinstance(result, dict)
	assert "positive_droplets" in result
	print("Positive Droplets: ", result["positive_droplets"])
	assert 0 < result["fraction_positive"] < 1
