from django.conf.urls import patterns, url

from istore.views.decorators import staff_member_required
from istore.core.application import Application
from istore.apps.dashboard.reports import views


class ReportsApplication(Application):
    name = None
    index_view = views.IndexView

    def get_urls(self):
        urlpatterns = patterns('',
            url(r'^$', self.index_view.as_view(), name='reports-index'),
        )
        return self.post_process_urls(urlpatterns)

    def get_url_decorator(self, url_name):
        return staff_member_required


application = ReportsApplication()
