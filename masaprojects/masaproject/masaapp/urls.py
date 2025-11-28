from django.urls import path
from . import views

# アプリ内のURLルーティング設定
urlpatterns = [
    # トップページ（ようこそ画面）
    path('', views.index, name='index'),

    # 在庫一覧ページ（ログインユーザーの在庫を表示）
    path('inventory/', views.inventory_list, name='inventory'),

    # 在庫の新規登録ページ
    path('inventory/add/', views.inventory_add, name='inventory_add'),

    # 在庫の編集ページ（pkは在庫ID）
    path('inventory/edit/<int:pk>/', views.inventory_edit, name='inventory_edit'),

    # 在庫の削除処理（pkは在庫ID）
    path('inventory/delete/<int:pk>/', views.inventory_delete, name='inventory_delete'),

    # お問い合わせフォームページ
    path('contact/', views.contact_view, name='contact'),

    # ユーザーの新規登録ページ
    path('signup/', views.signup_view, name='signup'),

    # 在庫操作履歴ページ（ログインユーザーの履歴を表示）
    path('inventory/history/', views.inventory_history, name='inventory_history'),

    
    path('login/success/', views.login_success_view, name='login_success'),

    
    path('logout/success/', views.logout_success_view, name='logout_success'),
    
]


