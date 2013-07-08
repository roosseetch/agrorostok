from django.conf import settings

def checkout(request):
    return {'anon_checkout_allowed': getattr(settings, 'ISTORE_ALLOW_ANON_CHECKOUT', False)}
