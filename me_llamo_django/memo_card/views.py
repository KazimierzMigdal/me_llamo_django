from .forms import CategoryCreationForm, CategoryUpdateForm, UserMemocardCreationForm, MyForm
from .models import CategoryMemoCard, MemoCard, Repeat, UserMemoCard
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, TemplateView, ListView, DetailView, CreateView, UpdateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormMixin
from stats.models import Statistic
import datetime


class Cards(LoginRequiredMixin, ListView, FormMixin):
    model = Repeat
    context_object_name = 'word'
    template_name = "memo_card/cards.html"
    form_class = MyForm

    def get_queryset(self):
        user = self.request.user
        today = datetime.date.today()
        if user.profile.last_card_generaterd != datetime.date.today():
            MemoCard.objects.new_card(user)
        try:
            return Repeat.objects.filter(Q(user_for=user)&Q(repeat_on=today))[0]
        except:
            return []

    def post(self, request):
        word = self.get_queryset()
        answer = request.POST.get("save_answer")
        MemoCard.objects.leitner(request, word, answer)
        return redirect('cards')


class CategoryListView(LoginRequiredMixin, ListView):
    model = CategoryMemoCard
    context_object_name = 'categories'
    template_name = "memo_card/category.html"

    def get_queryset(self):
        user = self.request.user
        return CategoryMemoCard.objects.filter(author=user)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "memo_card/home.html"


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


class CategoryDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'category'
    template_name = "memo_card/category_detail.html"
    queryset = CategoryMemoCard.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        context['category'] = self.get_object()
        return context


class MemoCardListView(LoginRequiredMixin, ListView):
    model = UserMemoCard
    template_name = "memo_card/category_detail_all.html"
    context_object_name = 'memocards'

    def get_context_data(self, **kwargs):
        context = super(MemoCardListView, self).get_context_data(**kwargs)
        context['category'] = CategoryMemoCard.objects.get(id=self.kwargs.get('pk'))
        return context

    def get_queryset(self):
        category = CategoryMemoCard.objects.get(id=self.kwargs.get('pk'))
        return UserMemoCard.objects.filter(category=category)


class CategoryCreationView(LoginRequiredMixin, CreateView):
    model = CategoryMemoCard
    form_class = CategoryCreationForm
    template_name = 'memo_card/category_form.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(CategoryCreationView, self).get_form(form_class)
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, f'Storzono katygorię! Możesz dodać do niej fiszki.')
        return super().form_valid(form)


class Dictionary(LoginRequiredMixin, ListView):
    model = Repeat
    context_object_name = 'words'
    template_name = 'memo_card/dictionary.html'

    def get_queryset(self):
        user = self.request.user
        if user.profile.last_card_generaterd != datetime.date.today():
            MemoCard.objects.new_card(user)
        return Repeat.objects.filter(user_for=user).order_by('card__esp_title')


class MemoCardCreateView(LoginRequiredMixin, CreateView):
    model = UserMemoCard
    form_class = UserMemocardCreationForm
    template_name = 'memo_card/memocard-creator.html'

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = super(MemoCardCreateView, self).get_form(form_class)
        return form

    def form_valid(self, form):
        form.instance.category = CategoryMemoCard.objects.get(id=self.kwargs.get('pk'))
        return super().form_valid(form)

    def get_success_url(self):
        value = self.request.POST.get("save")
        if value == 'save':
            messages.success(self.request, f'Storzono fiszkę!')
            return reverse_lazy('category_detail', kwargs={'pk': self.kwargs.get('pk')})
        else:
            messages.success(self.request, f'Storzono fiszkę! Możesz dodać kolejną.')
            return reverse_lazy('memocard_form', kwargs={'pk': self.kwargs.get('pk')})


class MemoCardDeleteView(LoginRequiredMixin,DeleteView):
    model = UserMemoCard

    def get_success_url(self):
        category = self.object.category
        messages.error(self.request, f"fiszka usunięta")
        return reverse_lazy( 'category_memocard', kwargs={'pk': category.id})

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)


class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView, FormMixin):
    model = CategoryMemoCard
    context_object_name = 'category'
    template_name = 'memo_card/category_edit.html'
    form_class = CategoryUpdateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, f'Katygoria została poprawiona')
        return super().form_valid(form)

    def test_func(self):
        category = self.get_object()
        if self.request.user == category.author:
            return True
        else:
            return False


@login_required
def memocard_repeat(request, pk):
    category = CategoryMemoCard.objects.get(id=pk)
    try:
        memocard = UserMemoCard.objects.filter(category=category).order_by('?')[0]
    except:
        memocard = []
    return render(request, 'memo_card/memocard-repeat.html',{'category': category, 'memocard': memocard})


@login_required
def memocard_detail(request, pk):
    memocard = UserMemoCard.objects.get(id=pk)
    return render(request, 'memo_card/memocard_detail.html', {'memocard':memocard})
