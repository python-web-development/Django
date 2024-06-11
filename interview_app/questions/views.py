from django.shortcuts import render, get_object_or_404
from .models import Language, Question
from django.core.paginator import Paginator

def home(request):
    languages = Language.objects.all()
    return render(request, 'questions/home.html', {'languages': languages})

def detail(request, language_id):
    language = get_object_or_404(Language, pk=language_id)
    questions = Question.objects.filter(language=language)
    paginator = Paginator(questions, 10)  # Show 10 questions per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'questions/detail.html', {'language': language, 'page_obj': page_obj})
