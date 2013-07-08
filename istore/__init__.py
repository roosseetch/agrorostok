import os

# Use 'final' as the 4th element to indicate
# a full release

VERSION = (0, 5, 0, 'final')


def get_short_version():
    return '%s.%s' % (VERSION[0], VERSION[1])


def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        # Append 3rd digit if > 0
        version = '%s.%s' % (version, VERSION[2])
    if VERSION[3:] == ('alpha', 0):
        version = '%s pre-alpha' % version
    elif VERSION[3] != 'final':
        version = '%s %s %s' % (version, VERSION[3], VERSION[4])
    return version


# Cheeky setting that allows each template to be accessible by two paths.
# Eg: the template 'oscar/templates/oscar/base.html' can be accessed via both
# 'base.html' and 'oscar/base.html'.  This allows Oscar's templates to be
# extended by templates with the same filename
ISTORE_MAIN_TEMPLATE_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'templates/oscar')

ISTORE_CORE_APPS = [
    'istore',
    'istore.apps.analytics',
    'istore.apps.order',
    'istore.apps.checkout',
    'istore.apps.shipping',
    'istore.apps.catalogue',
    'istore.apps.catalogue.reviews',
    'istore.apps.basket',
    'istore.apps.payment',
    'istore.apps.offer',
    'istore.apps.address',
    'istore.apps.partner',
    'istore.apps.customer',
    'istore.apps.promotions',
    'istore.apps.search',
    'istore.apps.voucher',
    'istore.apps.dashboard',
    'istore.apps.dashboard.reports',
    'istore.apps.dashboard.users',
    'istore.apps.dashboard.orders',
    'istore.apps.dashboard.promotions',
    'istore.apps.dashboard.catalogue',
    'istore.apps.dashboard.offers',
    'istore.apps.dashboard.ranges',
    'istore.apps.dashboard.vouchers',
    'istore.apps.dashboard.communications',
    # 3rd-party apps that oscar depends on
    'haystack',
    'treebeard',
    'sorl.thumbnail',
]


def get_core_apps(overrides=None):
    """
    Return a list of oscar's apps amended with any passed overrides
    """
    if not overrides:
        return ISTORE_CORE_APPS

    def get_app_label(app_label, overrides):
        pattern = app_label.replace('istore.apps.', '')
        for override in overrides:
            if override.endswith(pattern):
                if 'dashboard' in override and 'dashboard' not in pattern:
                    continue
                return override
        return app_label

    apps = []
    for app_label in ISTORE_CORE_APPS:
        apps.append(get_app_label(app_label, overrides))
    return apps
