from django import forms
from .models import ContactMessage, InventoryItem
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# お問い合わせフォーム：ContactMessageモデルに基づく
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage  # 対象モデル
        fields = ['name', 'email', 'subject', 'message']  # 使用するフィールド

# 在庫登録・編集フォーム：InventoryItemモデルに基づく
class InventoryForm(forms.ModelForm):
    class Meta:
        model = InventoryItem  # 対象モデル
        fields = ['name', 'quantity']  # ユーザーはnameとquantityのみ入力

# ユーザー登録フォーム：Django標準のUserCreationFormを拡張
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User  # Djangoのユーザーモデル
        fields = ['username', 'email', 'password1', 'password2']  # メールアドレスも追加