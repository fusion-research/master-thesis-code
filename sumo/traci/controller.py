import traci, pprint

from tracker import Tracker
from listener import StepListener


class SimController:
    def __init__(self, config):
        self.config = config
        self.tracker = Tracker()
        self.stepListener = StepListener(self.tracker)

    def init(self):
        # Add step listener
        traci.addStepListener(self.stepListener)

        # Load data about existing polygons in the simulation
        self.tracker.updatePolygons()

    def start(self):
        # Connect
        traci.start(self.config["sumoCmd"])

        # Initialize call listeners, subscriptions, etc.
        self.init()

        # Run the simulation
        nStep = 0
        while nStep < self.config["steps"]:
            print("step", nStep)
            traci.simulationStep()
            nStep += 1

        # Finish and clean up
        self.finish()

    def finish(self):
        traci.close()
