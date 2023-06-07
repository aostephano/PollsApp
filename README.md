<!-- # Study Notes -->
# Main Title

## Topics Covered

- Topic 1
- Topic 2
- Topic 3

## Getting Started: Polls App

> ### Part 3: Write views that do something

Writing more views: You can write dynamic routes by using '<type: var_name>' inside your urlpatterns. For example:

```python

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

> ### Part 4: Write views that do something

Always return an HttpResponseRedirect after successfully dealing with POST data. This prevents data from being posted twice if a user hits the Back button.

> ### Keywords

**Endpoint:** /products /orders /users, /etc;

**view.py:** Event handler;

**migrate:** command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py;

**DRY:** Don't Repeat Yourself principle;

**Migrations:** are how Django stores changes to your models (and thus your database schema) - they’re files on disk. You can read the migration for your new model if you like; it’s the file polls/migrations/0001_initial.py;

```bash
python manage.py makemigrations polls
```

**Migrate:** command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your mysite/settings.py file and the database migrations shipped with the app;

```bash
python manage.py sqlmigrate polls 0001
```

**TEMPLATES:** Django’s template engine provides a powerful mini-language for defining the user-facing layer of your application, encouraging a clean separation of concerns in your code;

**DTO:** Data Transfer Object, is an object that carries data between processes;

**Race Condition:** A situation where two or more threads/processes are reading or writing some shared data, and the final result depends on the timing of how the threads are scheduled;

### Remember the three-step guide to making model changes

1. Change your models (in models.py).
2. Run python manage.py makemigrations to create migrations for those changes
3. Run python manage.py migrate to apply those changes to the database.

### Field lookups

Field lookups are how you specify the meat of an SQL WHERE clause. They’re specified as keyword arguments to the QuerySet methods filter(), exclude() and get().

Basic lookups keyword arguments take the form field__lookuptype=value. (That’s a double-underscore). For example:

```bash
Entry.objects.filter(pub_date__lte="2006-01-01")
```

### Questions

- [ ] Question 1
- [ ] Question 2
- [ ] Question 3

### Next Steps

[Note down what your next steps will be regarding the subject of the lecture.]

### Additional Resources

- [1 hour Django Introduction](https://www.youtube.com/watch?v=rHux0gMZ3Eg)
- [Python Django Tutorial for Beginners](https://www.youtube.com/watch?v=gcv5hXyTcIo)
- [Recommended book](Book Name)

### Additional Notes

[Include any other notes or observations you wish to make.]

### Image Sample

![Image Description](image.jpg){width=400px}

### Code Sample

```python
def saudacao(nome):
"""Esta função saúda a pessoa com o nome fornecido."""
print(f"Olá, {nome}!")
