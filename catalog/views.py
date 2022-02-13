from django.shortcuts import render
from .models import BookInstance, Book, Author, Genre, Language
from django.views import generic

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()
    num_fiction = Genre.objects.filter(name__icontains='fiction').count()
    num_books_with_all = Book.objects.filter(title__icontains='all').count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_fiction': num_fiction,
        'num_books_with_all': num_books_with_all,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by=10

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by=10

class AuthorDetailView(generic.DetailView):
    model = Author