from django.db import models
from django.contrib.auth.models import User

# 在庫アイテムモデル：ユーザーごとの在庫情報を管理
class InventoryItem(models.Model):
    name = models.CharField(max_length=100)  # 在庫名
    quantity = models.PositiveIntegerField()  # 数量（0以上）
    updated_at = models.DateTimeField(auto_now=True)  # 最終更新日時（自動更新）
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 所有ユーザー

    def __str__(self):
        return self.name  # 管理画面などで表示される文字列

# 在庫操作履歴モデル：登録・編集・削除などの履歴を記録
class InventoryLog(models.Model):
    ACTION_CHOICES = [
        ('create', '登録'),
        ('update', '更新'),
        ('delete', '削除'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # 操作したユーザー
    inventory = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)  # 対象の在庫
    action = models.CharField(max_length=10, choices=ACTION_CHOICES)  # 操作種別
    timestamp = models.DateTimeField(auto_now_add=True)  # 操作日時（自動記録）
    note = models.TextField(blank=True)  # 任意のメモ

    def __str__(self):
        return f"{self.user}が{self.inventory}を{self.get_action_display()}（{self.timestamp}）"

# お問い合わせモデル：ユーザーからの問い合わせ内容を保存
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)  # 名前
    email = models.EmailField()  # メールアドレス
    subject = models.CharField(max_length=200)  # 件名
    message = models.TextField()  # メッセージ本文
    sent_at = models.DateTimeField(auto_now_add=True)  # 送信日時（自動記録）