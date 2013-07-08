from istore.apps.customer import abstract_models


class Email(abstract_models.AbstractEmail):
    pass


class CommunicationEventType(abstract_models.AbstractCommunicationEventType):
    pass


class Notification(abstract_models.AbstractNotification):
    pass


class ProductAlert(abstract_models.AbstractProductAlert):
    pass


from istore.apps.customer.history_helpers import *
from istore.apps.customer.alerts.receivers import *
