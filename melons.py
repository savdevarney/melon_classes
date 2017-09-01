"""Classes for melon orders."""

from random import randint
import datetime


class AbstractMelonOrder(object):

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_base_price(self):
        base_price = randint(5, 9)
        #add $4 charge if day is mon-fri and 8am-11am
        current_datetime = datetime.datetime.now()
        day = current_datetime.weekday()
        time = current_datetime.hour
        #time = 10 <-- to test
        if day in range(5) and time in range(8, 12):
            base_price += 4.00
        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()

        if self.species == "Christmas":
            base_price = 1.5 * base_price

        total = (1 + self.tax) * self.qty * base_price
        if self.order_type == "international" and self.qty < 10:
            total = total + 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Domestic melon order attributes."""
        super(DomesticMelonOrder, self).__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.08



class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super(InternationalMelonOrder, self).__init__(species, qty)
        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order."""


    def __init__(self, species, qty):
        """Initialize melon order attributes"""
        super(GovernmentMelonOrder, self).__init__(species, qty)
        self.order_type = "domestic"
        self.tax = 0.00
        self.passed_inspection = False


    def mark_inspection(self, passed):

        self.passed_inspection = passed
