from django.conf.urls.defaults import *
from bookmarks.views import *
from bookmarks.models import Bookmark

urlpatterns = patterns('basic.bookmarks.views',

    # (r'^$', main_page),

    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/(?P<object_id>\d+)/$',
        view='bookmark_detail',
        name='bookmark_detail',
    ),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\w{1,2})/$',
        view='bookmark_archive_day',
        name='bookmark_archive_day',
    ),
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$',
        view='bookmark_archive_month',
        name='bookmark_archive_month',
    ),
    url(r'^(?P<year>\d{4})/$',
        view='bookmark_archive_year',
        name='bookmark_archive_year',
    ),
    url(r'^$',
        view='bookmark_list',
        name='bookmark_index',
    ),
)