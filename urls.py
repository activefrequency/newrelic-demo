from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^test-string/', 'newrelicdemo.views.test_string'),
    (r'^test-float/', 'newrelicdemo.views.test_float'),
    (r'^test-decimal/', 'newrelicdemo.views.test_decimal'),
)
