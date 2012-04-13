from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^test-string/', 'views.test_string'),
    (r'^test-float/', 'views.test_float'),
    (r'^test-decimal/', 'views.test_decimal'),
)
