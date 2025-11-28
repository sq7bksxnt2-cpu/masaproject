from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 管理サイト（/admin/）
    path('admin/', admin.site.urls),

    # アプリ「masaapp」のURL設定を読み込む（トップページなど）
    path('', include('masaapp.urls')),

    # Django標準の認証URL（ログイン・ログアウト・パスワード変更など）
    path('accounts/', include('django.contrib.auth.urls')),
]