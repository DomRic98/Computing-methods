import math


class Particle:
    """ Class representing a generic muon
    """

    def __init__(self, mass, charge, name, momentum=0., beta=0.):
        """
        :param mass: mass of muon in MeV/c^2
        :param charge: charge of muon in units of electron charge
        :param name: particle's name
        :param momentum: module of initial particle's momentum
        """
        self.mass = mass
        self.charge = charge
        self.name = name
        self.momentum = momentum
        self.beta = beta

    def info(self):
        """ Print some info about muon
        :return: a string with some information
        """
        msg = 'Particle "{name}" of mass {mass:.3f} MeV/c^2, charge: {charge}'
        return msg.format(name=self.name, mass=self.mass, charge=self.charge)

    @property
    def energy(self):
        """ Computing the particle's energy
        :return: the energy of the particle
        """
        return math.sqrt(self.mass ** 2 + self._momentum ** 2)

    @energy.setter
    def energy(self, energy):
        """ Set the particle's energy
        :param energy: this attribute doesn't exist but it's emulate by the @property
        """
        if energy < self.mass:
            print('Cannot set energy to a value lower than tha muon mass')
        else:
            self._momentum = math.sqrt(energy ** 2 - self.mass ** 2)

    @property
    def momentum(self):
        return self._momentum

    @momentum.setter
    def momentum(self, momentum):
        """ Set the particle's momentum
        """
        if momentum < 0.:
            print('Cannot set momentum to a negative value')
            print('Momentum will be set to 0')
            self._momentum = 0.
        else:
            self._momentum = momentum

    @property
    def beta(self):
        """ Computing the particle's beta
        :return: the beta of the particle
        """
        return self._momentum / self.energy

    @beta.setter
    def beta(self, beta):
        if beta < 0. or beta > 1.:
            print('Cannot set beta into unphysical region')
        else:
            self.momentum = beta * self.mass / math.sqrt(1 - beta ** 2)


class Proton(Particle):
    """ Class describing a proton that inheritance attributes and methods from Superclass Particle
    """
    NAME = 'Proton'
    MASS = 938.272  # MeV/c^2
    CHARGE = +1  # unity of electron charge

    def __init__(self, momentum=0., beta=0.):
        Particle.__init__(self, self.MASS, self.CHARGE, self.NAME, momentum, beta)


class Alpha(Particle):
    """ Class describing an Alpha nucleus """

    NAME = 'Alpha'
    MASS = 3727.3  # MeV/c^2
    CHARGE = +2  # unity of electron charge

    def __init__(self, momentum=0., beta=0.):
        Particle.__init__(self, self.MASS, self.CHARGE, self.NAME, momentum, beta)


proton = Proton(momentum=200.)
print(proton.info())
proton.beta = 0.8
print(proton.beta)
alpha = Alpha(momentum=20.)
alpha.energy = 10000.
print(alpha.info())
