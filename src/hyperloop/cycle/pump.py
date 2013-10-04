from openmdao.main.api import Component

from openmdao.lib.datatypes.api import Float


class Pump(Component): 
    """Calculate the power requirement for a liquid pump given flow conditions""" 

    delta_P