from .forms import CategoryCreationForm, CategoryUpdateForm, UserMemocardCreationForm
from .models import CategoryMemoCard, MemoCard, Repeat, UserMemoCard
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from stats.models import Statistic
import datetime


@login_required
def cards(request):
    user = request.user
    today = datetime.date.today()
    stats = Statistic.objects.get(Q(day=today)&Q(user=user))
    try:
        word = Repeat.objects.filter(
        Q(user_for=user)&Q(repeat_on=today)
        )[0]
    except:
        word = []
    if request.method == 'POST':
        value = request.POST.get("save_answer")
        counter = word.counter
        if value == 'right':
            stats.right = stats.right + 1
            stats.save()
            word.counter = word.counter + 1
            if word.counter == 1:
                word.repeat_on = datetime.date.today() + datetime.timedelta(days=2)
                messages.success(request, f"Ta fiszka wróci do ciebie za 2 dni")
            elif word.counter == 2:
                word.repeat_on = datetime.date.today() + datetime.timedelta(days=7)
                messages.success(request, f"Ta fiszka wróci do ciebie za 7 dni")
            elif word.counter == 3:
                word.repeat_on = datetime.date.today() + datetime.timedelta(days=14)
                messages.success(request, f"Ta fiszka wróci do ciebie za 2 tygodnie")
            elif word.counter == 4:
                word.repeat_on = datetime.date.today() + datetime.timedelta(days=30)
                messages.success(request, f"Ta fiszka wróci do ciebie w przyszłym miesiącu")
            elif word.counter == 5:
                word.repeat_on = datetime.date.today() + datetime.timedelta(days=60)
                messages.success(request, f"Ta fiszka wróci do ciebie za 2 miesiące")
            elif word.counter == 5:
                word.repeat_on = datetime.date.today() + datetime.timedelta(days=183)
                messages.success(request, f"Ta fiszka wróci do ciebie za pół roku")
        elif value == 'wrong':
            stats.wrong = stats.wrong + 1
            stats.save()
            word.counter = 0
            word.repeat_on = datetime.date.today() + datetime.timedelta(days=1)
            messages.error(request, f"Ta fiszka wróci do ciebie jutro")
        else:
            stats.near = stats.near + 1
            stats.save()
            word.repeat_on = datetime.date.today() + datetime.timedelta(days=1)
            messages.warning(request, f"Ta fiszka wróci do ciebie jutro")
        word.save()
        return redirect('cards')
    return render(request, 'memo_card/cards.html', {'word':word})


@login_required
def category(request):
    user = request.user
    categories = CategoryMemoCard.objects.filter(author=user)
    return render(request, 'memo_card/category.html', {'categories': categories})


class CategoryDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = CategoryMemoCard

    def get_success_url(self):
        return reverse_lazy('category')

    def test_func(self):
        category = self.get_object()
        if self.request.user == category.author:
            return True
        else:
            return False


@login_required
def category_detail(request, pk):
    category = CategoryMemoCard.objects.get(id=pk)
    return render(request, 'memo_card/category_detail.html', {'category': category})


@login_required
def category_detail_all(request, pk):
    category = CategoryMemoCard.objects.get(id=pk)
    memocards = UserMemoCard.objects.filter(category=category)
    return render(request, 'memo_card/category_detail_all.html', {'category': category, 'memocards': memocards})


@login_required
def category_form(request):
    if request.method == 'POST':
        form = CategoryCreationForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.author = request.user
            category.save()
            title = form.cleaned_data.get('title')
            messages.success(request, f'Katygoria {title} została stworzona. Dodaj do niej fiszki')
            return redirect('category')
    else:
        form = CategoryCreationForm()
    return render(request, 'memo_card/category_form.html', {'form': form})


@login_required
def dictionary(request):
    user = request.user
    words = Repeat.objects.filter(user_for=user).order_by('card__esp_title')
    return render(request, 'memo_card/dictionary.html', {'words': words})


@login_required
def main(request):
    user = request.user
    last_card_generaterd = user.profile.last_card_generaterd
    today = datetime.date.today()
    if last_card_generaterd != today:
        MemoCard.objects.new_card(user)

    return render(request, 'memo_card/home.html', {})


@login_required
def memocard_creator(request, pk):
    category = CategoryMemoCard.objects.get(id=pk)
    if request.method == 'POST':
        form = UserMemocardCreationForm(request.POST)
        value = request.POST.get("save")
        if form.is_valid():
            memocard = form.save(commit=False)
            memocard.category = category
            memocard.save()
            messages.success(request, f'Fiszka została dodana')
            if value == 'save':
                return redirect('category_detail', pk=pk)
            else:
                return redirect('memocard_form', pk=pk)
    else:
        form = UserMemocardCreationForm()
    return render(request, 'memo_card/memocard-creator.html', {'category': category, 'form': form})


@login_required
def memocard_delete(request, pk):
    memocard = UserMemoCard.objects.get(id=pk)
    pk = memocard.category.id
    memocard.delete()
    messages.error(request, f"fiszka usunięta")
    return redirect('category_memocard', pk=pk)


@login_required
def category_edit(request, pk):
    category = CategoryMemoCard.objects.get(id=pk)
    if request.method == 'POST':
        form = CategoryUpdateForm(request.POST,
                                instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, f'Katygoria została poprawiona')
            return redirect('category_detail', pk=pk)
    else:
        form = CategoryUpdateForm(instance=category)
    return render(request, 'memo_card/category_edit.html',{'category': category, 'form':form})


@login_required
def memocard_repeat(request, pk):
    category = CategoryMemoCard.objects.get(id=pk)
    try:
        memocard = UserMemoCard.objects.filter(category=category).order_by('?')[0]
    except:
        memocard = []
    print(memocard)
    return render(request, 'memo_card/memocard-repeat.html',{'category': category, 'memocard': memocard})


@login_required
def memocard_detail(request, pk):
    memocard = UserMemoCard.objects.get(id=pk)
    return render(request, 'memo_card/memocard_detail.html', {'memocard':memocard})
