class Person:

  def __init__(self, infectionStatus, turnsRemaining):
    # 0 = uninfected, 1 = infected, 2 = immune
    self.infectionStatus = infectionStatus
    self.turnsRemaining = turnsRemaining
