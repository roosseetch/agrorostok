from django.contrib.auth.models import User
from django.contrib.auth.backends import ModelBackend
from django.core.mail import mail_admins
from django.core.exceptions import ImproperlyConfiguredfrom istore.core.compat import get_user_modelUser = get_user_model()if hasattr(User, 'REQUIRED_FIELDS'):    if not (User.USERNAME_FIELD == 'email' or 'email' in User.REQUIRED_FIELDS):        raise ImproperlyConfigured(            "Emailbackend: Your User model must have an email"            " field with blank=False")

class Emailbackend(ModelBackend):
    """    Custom auth backend that users an email address    For this to work, the User model must have an 'email' field    """
    def authenticate(self, email=None, password=None, *args, **kwargs):
        if email is None:
            if not 'username' in kwargs or kwargs['username'] is None:
                return None
            email = kwargs['username']

        # Check if we're dealing with an email address
        if '@' not in email:
            return None

        # We lowercase the host part as this is what Django does when saving a
        # user
        local, host = email.split('@')
        clean_email = local + '@' + host.lower()

        # Since Django doesn't enforce emails to be unique, we look for all
        # matching users and try to authenticate them all.  If we get more than
        # one success, then we mail admins as this is a problem.
        authenticated_users = []
        for user in User.objects.filter(email=clean_email):
            if user.check_password(password):
                authenticated_users.append(user)
        if len(authenticated_users) == 1:
            # Happy path
            return authenticated_users[0]
        elif len(authenticated_users) > 1:
            # This is the problem scenario where we have multiple users with
            # the same email address AND password.  We can't safely authentiate
            # either.  This situation requires intervention by an admin and so
            # we mail them to let them know!
            mail_admins(
                "There are multiple users with email address: %s" % clean_email,
                ("There are %s users with email %s and the same password "
                 "which means none of them are able to authenticate") % (len(authenticated_users),
                                                clean_email))
        return None
