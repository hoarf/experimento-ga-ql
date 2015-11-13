import pytest
from ExperimentConfig import ExperimentConfig

def test_all_experiments_run():
    e1 = ExperimentConfig(experimentType=1)
    e1.run()
    e2 = ExperimentConfig(experimentType=2)
    e2.run()
    e3 = ExperimentConfig(experimentType=3)
    e3.run()
    e4 = ExperimentConfig(experimentType=4)
    e4.run()

def test_all_experiment_config():
    e = ExperimentConfig(generations=1000, population=100,
                         mutations=[0.001], crossovers=[0.2],
                         group_sizes=[1], ks=[8])
    e.run()

