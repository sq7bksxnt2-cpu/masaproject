from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import InventoryItem, InventoryLog
from .forms import ContactForm, InventoryForm, CustomUserCreationForm

# トップページ
def index(request):
    return render(request, 'index.html')

# お問い合わせフォーム
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # 必要ならメール送信処理をここに追加
            return render(request, 'contact/thanks.html')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})

# 在庫一覧（ログイン必須・全ユーザー共有）
@login_required
def inventory_list(request):
    items = InventoryItem.objects.all()
    return render(request, 'inventory.html', {'inventory': items})

# 在庫新規登録（管理者のみ）
@login_required
def inventory_add(request):
    if not request.user.is_staff:  # 管理者以外は拒否
        return HttpResponseForbidden("在庫の追加は管理者のみ可能です。")

    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            item = form.save()
            InventoryLog.objects.create(
                user=request.user,
                inventory=item,
                action='create',
                note='新規登録'
            )
            return redirect('inventory')
    else:
        form = InventoryForm()
    return render(request, 'inventory_form.html', {'form': form, 'title': '新規登録'})

# 在庫編集（管理者のみ）
@login_required
def inventory_edit(request, pk):
    if not request.user.is_staff:
        return HttpResponseForbidden("在庫の編集は管理者のみ可能です。")

    item = get_object_or_404(InventoryItem, pk=pk)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            InventoryLog.objects.create(
                user=request.user,
                inventory=item,
                action='update',
                note='編集'
            )
            return redirect('inventory')
    else:
        form = InventoryForm(instance=item)
    return render(request, 'inventory_form.html', {'form': form, 'title': '編集'})

# 在庫削除（管理者のみ）
@login_required
def inventory_add(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("在庫の追加は管理者のみ可能です。")

    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)   # ← commit=False にする
            item.user = request.user         # ← ログインユーザーをセット
            item.save()
            InventoryLog.objects.create(
                user=request.user,
                inventory=item,
                action='create',
                note='新規登録'
            )
            return redirect('inventory')
    else:
        form = InventoryForm()
    return render(request, 'inventory_form.html', {'form': form, 'title': '新規登録'})

# 在庫操作履歴（全ユーザー共有）
@login_required
def inventory_history(request):
    logs = InventoryLog.objects.all().order_by('-timestamp')
    return render(request, 'inventory/history.html', {'logs': logs})

# ユーザー登録
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

# ログイン成功画面
@login_required
def login_success_view(request):
    return render(request, 'registration/login_success.html')

# ログアウト成功画面
def logout_success_view(request):
    return render(request, 'registration/logout_success.html')

from django.http import HttpResponseForbidden

@login_required
def inventory_delete(request, pk):
    if not request.user.is_staff:  # 管理者以外は拒否
        return HttpResponseForbidden("在庫の削除は管理者のみ可能です。")

    item = get_object_or_404(InventoryItem, pk=pk)
    InventoryLog.objects.create(
        user=request.user,
        inventory=item,
        action='delete',
        note='削除'
    )
    item.delete()
    return redirect('inventory')