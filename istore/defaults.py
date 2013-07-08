from django.utils.translation import ugettext_lazy as _

ISTORE_SHOP_NAME = 'Agrorostok'
ISTORE_SHOP_TAGLINE = 'Domain-driven e-Commerce for Django'

# Basket settings
ISTORE_BASKET_COOKIE_LIFETIME = 7 * 24 * 60 * 60
ISTORE_BASKET_COOKIE_OPEN = 'istore_open_basket'
ISTORE_BASKET_COOKIE_SAVED = 'istore_saved_basket'
ISTORE_MAX_BASKET_QUANTITY_THRESHOLD = 10000

# Currency
ISTORE_DEFAULT_CURRENCY = 'GBP'

# Max number of products to keep on the user's history
ISTORE_RECENTLY_VIEWED_PRODUCTS = 20

# Paths
ISTORE_IMAGE_FOLDER = 'images/products/%Y/%m/'
ISTORE_PROMOTION_FOLDER = 'images/promotions/'

# Copy this image from oscar/static/img to your MEDIA_ROOT folder.
# It needs to be there so Sorl can resize it.
ISTORE_MISSING_IMAGE_URL = 'image_not_found.jpg'
ISTORE_UPLOAD_ROOT = '/tmp'

# Address settings
ISTORE_REQUIRED_ADDRESS_FIELDS = ('first_name', 'last_name', 'line1',
                                 'line4', 'postcode', 'country')

# Search settings
ISTORE_SEARCH_SUGGEST_LIMIT = 10

# Product list settings
ISTORE_PRODUCTS_PER_PAGE = 20

# Checkout
ISTORE_ALLOW_ANON_CHECKOUT = False

# Partners
ISTORE_PARTNER_WRAPPERS = {}

# Promotions
COUNTDOWN, LIST, SINGLE_PRODUCT, TABBED_BLOCK = (
    'Countdown', 'List', 'SingleProduct', 'TabbedBlock')
ISTORE_PROMOTION_MERCHANDISING_BLOCK_TYPES = (
    (COUNTDOWN, "Vertical list"),
    (LIST, "Horizontal list"),
    (TABBED_BLOCK, "Tabbed block"),
    (SINGLE_PRODUCT, "Single product"),
)
ISTORE_PROMOTION_POSITIONS = (('page', 'Page'),
                             ('right', 'Right-hand sidebar'),
                             ('left', 'Left-hand sidebar'))

# Reviews
ISTORE_ALLOW_ANON_REVIEWS = True
ISTORE_MODERATE_REVIEWS = False

# This enables sending alert notifications/emails
# instantly when products get back in stock
# by listening to stock record update signals
# this might impact performace for large numbers
# stock record updates.
# Alternatively, the management command
# ``oscar_send_alerts`` can be used to
# run periodically, e.g. as a cronjob. In this case
# instant alerts should be disabled.
ISTORE_EAGER_ALERTS = False

# Registration
ISTORE_SEND_REGISTRATION_EMAIL = True
ISTORE_FROM_EMAIL = 'agrorostok@gmail.com'

# Offers
ISTORE_OFFER_BLACKLIST_PRODUCT = None

# Cookies
ISTORE_COOKIES_DELETE_ON_LOGOUT = ['istore_recently_viewed_products', ]

# Hidden Oscar features, e.g. wishlists or reviews
ISTORE_HIDDEN_FEATURES = []

# Menu structure of the dashboard navigation
ISTORE_DASHBOARD_NAVIGATION = [
    {
        'label': _('Dashboard'),
        'icon': 'icon-th-list',
        'url_name': 'dashboard:index',
    },
    {
        'label': _('Catalogue'),
        'icon': 'icon-sitemap',
        'children': [
            {
                'label': _('Products'),
                'url_name': 'dashboard:catalogue-product-list',
            },
            {
                'label': _('Categories'),
                'url_name': 'dashboard:catalogue-category-list',
            },
            {
                'label': _('Ranges'),
                'url_name': 'dashboard:range-list',
            },
            {
                'label': _('Low stock alerts'),
                'url_name': 'dashboard:stock-alert-list',
            },
        ]
    },
    {
        'label': _('Fulfilment'),
        'icon': 'icon-shopping-cart',
        'children': [
            {
                'label': _('Order management'),
                'url_name': 'dashboard:order-list',
            },
            {
                'label': _('Statistics'),
                'url_name': 'dashboard:order-stats',
            },
            {
                'label': _('Partners'),
                'url_name': 'dashboard:partner-list',
            },
        ]
    },
    {
        'label': _('Customers'),
        'icon': 'icon-group',
        'children': [
            {
                'label': _('Customer management'),
                'url_name': 'dashboard:users-index',
            },
            {
                'label': _('Stock alert requests'),
                'url_name': 'dashboard:user-alert-list',
            },
        ]
    },
    {
        'label': _('Offers'),
        'icon': 'icon-bullhorn',
        'children': [
            {
                'label': _('Offer management'),
                'url_name': 'dashboard:offer-list',
            },
            {
                'label': _('Vouchers'),
                'url_name': 'dashboard:voucher-list',
            },
        ],
    },
    {
        'label': _('Content'),
        'icon': 'icon-folder-close',
        'children': [
            {
                'label': _('Content blocks'),
                'url_name': 'dashboard:promotion-list',
            },
            {
                'label': _('Content blocks by page'),
                'url_name': 'dashboard:promotion-list-by-page',
            },
            {
                'label': _('Pages'),
                'url_name': 'dashboard:page-list',
            },
            {
                'label': _('Email templates'),
                'url_name': 'dashboard:comms-list',
            },
            {
                'label': _('Reviews'),
                'url_name': 'dashboard:reviews-list',
            },
        ]
    },
    {
        'label': _('Reports'),
        'icon': 'icon-bar-chart',
        'url_name': 'dashboard:reports-index',
    },
]

# Search facets
ISTORE_SEARCH_FACETS = {
    'fields': {
        # The key for these dicts will be used when passing facet data
        # to the template. Same for the 'queries' dict below.
        'category': {
            'name': _('Category'),
            'field': 'category'
        }
    },
    'queries': {
        'price_range': {
            'name': _('Price range'),
            'field': 'price',
            'queries': [
                # This is a list of (name, query) tuples where the name will
                # be displayed on the front-end.
                (_('0 to 40'), '[0 TO 20]'),
                (_('20 to 40'), '[20 TO 40]'),
                (_('40 to 60'), '[40 TO 60]'),
                (_('60+'), '[60 TO *]'),
            ]
        }
    }
}

ISTORE_SETTINGS = dict(
    [(k, v) for k, v in locals().items() if k.startswith('ISTORE_')])
