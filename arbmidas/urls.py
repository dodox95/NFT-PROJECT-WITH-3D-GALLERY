from django.contrib import admin
from django.urls import path
from abmidas_nft.views import home, index, vip_page, contact, connect_wallet, check_wallet_connection, nft, fetch_nft_data
from django.conf.urls.static import static
from django.conf import settings
from django.urls import re_path
from django.contrib.staticfiles.views import serve as serve_static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    re_path(r'^staticfiles/(?P<path>.*)$', serve_static, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^gallery/$', index, name='image-gallery'),
    path('pages/vip.html', vip_page, name='vip-page'),
    path('contact/', contact, name='contact'),
    path('connect-wallet/', connect_wallet, name='connect-wallet'),
    path('check-wallet-connection/', check_wallet_connection, name='check-wallet-connection'),
    path('staking/', nft, name='staking'),
    path('api/fetch-nft-data/', fetch_nft_data, name='fetch-nft-data'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.PUBLIC_IMAGES_URL, document_root=settings.PUBLIC_IMAGES_ROOT)

handler404 = 'abmidas_nft.views.handler404'
