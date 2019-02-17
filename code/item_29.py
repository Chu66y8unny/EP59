#!/usr/bin/env python3

import logging

class OldResistor(object):
    def __init__(self, ohms):
        self._ohms = ohms

    def get_ohms(self):
        return self._ohms

    def set_ohms(self, ohms):
        self._ohms = ohms


r0 = OldResistor(50e3)
print('Before: %5r' % r0.get_ohms())
r0.set_ohms(10e3)
print('After:  %5r' % r0.get_ohms())


# clumsy
r0.set_ohms(r0.get_ohms() + 5e3)


# Instead, you should start with simple public attributes.
class Resistor(object):
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0


r1 = Resistor(50e3)
r1.ohms = 10e3
print('%r ohms, %r volts, %r amps' %
      (r1.ohms, r1.voltage, r1.current))

r1.ohms += 5e3


# the @property decorator and its corresponding setter attribute
class VoltageResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def voltage(self):
        return self._voltage

    @voltage.setter
    def voltage(self, voltage):
        self._voltage = voltage
        self.current = self._voltage / self.ohms


r2 = VoltageResistance(1e3)
print('Before: %5r amps' % r2.current)
r2.voltage = 10
print('After:  %5r amps' % r2.current)


# Specifying a setter on a property also lets you perform type checking and
# validation on values passed to your class.
class BoundedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if ohms <= 0:
            raise ValueError('%f ohms must be > 0' % ohms)
        self._ohms = ohms


# assigning an invalid resistance to the attribute raises an exception
try:
    r3 = BoundedResistance(1e3)
    r3.ohms = 0
except:
    logging.exception('Expected')
else:
    assert False


# An exception will also be raised if you pass an invalid value to the
# constructor
try:
    BoundedResistance(-5)
except:
    logging.exception('Expected')
else:
    assert False


# You can use @property to make attributes from parent classes immutable
class FixedResistance(Resistor):
    def __init__(self, ohms):
        super().__init__(ohms)

    @property
    def ohms(self):
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        if hasattr(self, '_ohms'):
            raise AttributeError("Can't set attribute")
        self._ohms = ohms
        # trying to assign to the property after construction raises an
        # exception


try:
    r4 = FixedResistance(1e3)
    r4.ohms = 2e3
except:
    logging.exception('Expected')
else:
    assert False


# Please follow the rule of least surprise
# For example, avoid inappropriate side effects
class MysteriousResistor(Resistor):
    @property
    def ohms(self):
        self.voltage = self._ohms * self.current
        return self._ohms

    @ohms.setter
    def ohms(self, ohms):
        self._ohms = ohms


r7 = MysteriousResistor(10)
r7.current = 0.01
print('Before: %5r' % r7.voltage)
r7.ohms
print('After:  %5r' % r7.voltage)
