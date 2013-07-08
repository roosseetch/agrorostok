'''
from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _

from istore.apps.shipping.methods import (
    Free, NoShippingRequired, OfferDiscount)

# from istore.apps.shipping.repository import Repository as CoreRepository

from . import methods

METHODS = (
    methods.Standard(),
    methods.Express(),
)


class Repository(object):
    """
    Repository class responsible for returning ShippingMethod
    objects for a given user, basket etc
    """
    methods = (Free(),)

    def get_shipping_methods(self, user, basket, shipping_addr=None, **kwargs):
        """
        Return a list of all applicable shipping method objects
        for a given basket.

        We default to returning the Method models that have been defined but
        this behaviour can easily be overridden by subclassing this class
        and overriding this method.
        """
        # methods = [Free()]
        # return self.prime_methods(basket, methods)
        return self.prime_methods(basket, METHODS)

    def get_default_shipping_method(self, user, basket, shipping_addr=None,
                                    **kwargs):
        """
        Return a 'default' shipping method to show on the basket page to give
        the customer an indication of what their order will cost.
        """
        methods = self.get_shipping_methods(
            user, basket, shipping_addr, **kwargs)
        if len(methods) == 0:
            raise ImproperlyConfigured(
                _("You need to define some shipping methods"))
        return min(methods, key=lambda method: method.basket_charge_incl_tax())

    def prime_methods(self, basket, methods):
        """
        Prime a list of shipping method instances

        This involves injecting the basket instance into each and adding any
        discount wrappers.
        """
        return [self.prime_method(basket, method) for
                method in methods]

    def prime_method(self, basket, method):
        """
        Prime an individual method instance
        """
        method.set_basket(basket)
        # If the basket has a shipping offer, wrap the shipping method with a
        # decorating class that applies the offer discount to the shipping
        # charge.
        if basket.offer_applications.shipping_discounts:
            # We assume there is only one shipping discount available
            discount = basket.offer_applications.shipping_discounts[0]
            return OfferDiscount(method, discount['offer'])
        return method

    def find_by_code(self, code, basket):
        """
        Return the appropriate Method object for the given code
        """
        # known_methods = [Free, NoShippingRequired]
        # for klass in known_methods:
        #     if code == getattr(klass, 'code'):
        #         return self.prime_method(basket, klass())
        # return None
        if code == NoShippingRequired.code:
            method = NoShippingRequired()
        else:
            method = None
            for method_ in METHODS:
                if method_.code == code:
                    method = method_
            if method is None:
                raise ValueError(
                    "No shipping method found with code '%s'" % code)
        return self.prime_method(basket, method)
'''

from django.core.exceptions import ImproperlyConfigured
from django.utils.translation import ugettext_lazy as _

from istore.apps.shipping.methods import (
    Free, NoShippingRequired, OfferDiscount)


class Repository(object):
    """
    Repository class responsible for returning ShippingMethod
    objects for a given user, basket etc
    """
    methods = (Free(),)

    def get_shipping_methods(self, user, basket, shipping_addr=None, **kwargs):
        """
        Return a list of all applicable shipping method objects
        for a given basket.

        We default to returning the Method models that have been defined but
        this behaviour can easily be overridden by subclassing this class
        and overriding this method.
        """
        return self.prime_methods(basket, self.methods)

    def get_default_shipping_method(self, user, basket, shipping_addr=None,
                                    **kwargs):
        """
        Return a 'default' shipping method to show on the basket page to give
        the customer an indication of what their order will cost.
        """
        methods = self.get_shipping_methods(
            user, basket, shipping_addr, **kwargs)
        if len(methods) == 0:
            raise ImproperlyConfigured(
                _("You need to define some shipping methods"))

        # Choose the cheapest method by default
        return min(methods, key=lambda method: method.basket_charge_incl_tax())

    def prime_methods(self, basket, methods):
        """
        Prime a list of shipping method instances

        This involves injecting the basket instance into each and adding any
        discount wrappers.
        """
        return [self.prime_method(basket, method) for
                method in methods]

    def prime_method(self, basket, method):
        """
        Prime an individual method instance
        """
        method.set_basket(basket)
        # If the basket has a shipping offer, wrap the shipping method with a
        # decorating class that applies the offer discount to the shipping
        # charge.
        if basket.offer_applications.shipping_discounts:
            # We assume there is only one shipping discount available
            discount = basket.offer_applications.shipping_discounts[0]
            return OfferDiscount(method, discount['offer'])
        return method

    def find_by_code(self, code, basket):
        """
        Return the appropriate Method object for the given code
        """
        for method in self.methods:
            if method.code == code:
                return self.prime_method(basket, method)

        # Check for NoShippingRequired as that is a special case
        if code == NoShippingRequired.code:
            return self.prime_method(basket, NoShippingRequired())
