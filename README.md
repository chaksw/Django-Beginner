# Django Project

## Basic

### Start project

```bash
django-admin startproject project
django-admin startapp app
```

### Views Routing URLs

-   View
    View dictate what information is being shown to the client (html to render in function)
-   URLs
    URLs dictate where that information is shown on the website (function in view.py)

There work in concert so you can think of each View/URL pairing as a web page on the website.
In project level or app level, we need to define in urls.py the connection of routes in a list variable called urlpatterns using path() and include() Django functions

Likes:

-   html file define the content of page
-   view file define which html file will be sent to client (with certain logic) using

```python
 - render()
 - HttpResponse()
 - HttpResponseNotFound()
 - HttpResponseRedirect()
```

refer [view.py](/01_Django-Views-Routing-URLs/my_site/first_app/views.py) to see the example

-   urls file define where (urls path) a view should be displayed by using path() in urlpatterns[] list

## Template and Django template language

Refer [Layouts](/02-Django-and-Templates/my_site/templates/layouts.html) and to [example](/02-Django-and-Templates/my_site/my_app/templates/my_app/variable.html) to view html example

## Migration

### Base commands

```bash
- makemigrations
- migrate
- sqlmigrae
```

```bash
python manage.py makemigrations app
```

Create the set of instructions(code) that will **apply changes to the database**, the migration files will be created under:

-   app
    -   migrations
        -   0001_initial.py

```bash
python manage.py migrate
```

Run any existing migrations (typically created through the makemigrations command). <br>
This is actually running the files under the migrations directory created by makemigrations

```bash
python manage.py sqlmigrate app 0001
```

After running migrate command, if wanna to see what the SQL code looked like, you could run the sqlmigrate command to view. <br>
PS: Typically we won't reviewthe files created under the migrations directory or run sqlmigrate

### Steps for migrations

1. Inital project migrate command
2. Create app and create models (datebase)
3. Register app in INSTALLED_APP in setting.py
4. Run makemigrations for new app
5. Run migrate for new migrations

## Data Interaction (CRUD)

Something like `MyModel.objects` is Django Model Manager. This Manager can do the CRUD of database and also provides other enhanced functions

### ADD/INSERT data

#### Relative Function

```python
MyModel.objects.save() # INSERT, to create we need to create an instance of object first
MyModel.objects.objects.create() # CREATE AND SAVE
MyModel.objects.bulk_create() # CREATE a bulk data
```

-   Inserting new data into a SQL table by create a new instance of the class(models) and call `.save()` method to create an `INSERT` call to the SQL database <br>
-   Alternatively, usign the built-in `.objects.create()` method to both **create** and **save** the new data entry in a single line.
-   In instances where want to create multiple new data entries in bulk(庞大的), you can use the `.object.bulk_create()` methode to pass in a likst of newly created objects.

### READ data

#### Relative Function

```python
MyModel.objects.all() # grap all the entries in a database table
MyModel.objects.all()[index] # grap a entries in a database table in location 'index'
MyModel.objects.objects.get(pk=N) # grap a single item from the model table, pk: primary key
MyModel.objects.filter(attribute=value) # filter data, can be chained together
MyModel.objects.exclude(conditions) # exclude data
MyModel.objects.filter(name__startswith = 's') # filter lookups
keys:
1. __startswith
2. __in
3. __gte (greater and equal)
4. __contains
5. ...
```

-   for more method aoubt database oprations, check <a href='https://docs.djangoproject.com/en/4.1/ref/models/querysets/'>QuerySet API</a>
-   for more keys of lookups, see <a href='https://docs.djangoproject.com/en/4.1/ref/models/querysets/#id4'>lookups list</a>

Operators are also available in Django (`& |`) by referring `Q()` object class

### Updating Models, Entries (add | delete)

-   Entries updated can be done by overwriting attribute of existing data entry and call `.save()` to save the changes.
-   Similarly, use `.delete()` to delete an object.

## Connecting Tempaltes and Database Models

-   In **project urls**, add **app** as routing
-   In **app urls**, create routing and connect to method in **views**
-   In **views**, import models to use database models as variable and use as context of render() so that we built **connection of template and database models**
-   In **html**, use django templates language to call context define in **views**

# Django Admin
Take Project [car](./04-Django-Admin-Portal/my_car_site/) as an example, inside which apply all previous learning
One of the MOST POWERFUL FEATURES of Django, able to automatically create an Admin interface, to have a graphical interface for interacting with data and users on the site.
Django has pre-built admin paths in site `urls.py` file(`'/admin'`) as well as indications of an existing Django Admin app (`"django.contrib.admin"`).
Admin panel is meant for a manager of the website. so we need to **create a 'superuser'**
```bash
python manager.py createsuperuser
# enter username, email and password
```
## Model admin object class
### Resigter model in to admin
In `admin.py` of app, use `admin.site.register(model, modeladmin)` to add Model to administrator site. (ref <a href="https://docs.djangoproject.com/en/4.1/ref/contrib/admin/">Modeladmin</a>)
### ModelAdmin Class example
```python
class CarAdmin(admin.ModelAdmin):
    # change order of fields in admin site
    # fields = ['year', 'brand']
    # split up field into different section
    fieldsets = (
        ("TIME INFORMATION", {
            "fields": (
                ['year']
            ),
        }),
        ("CAR INFORMATION", {
            "fields": (
                ['brand']
            ),
        }),
    )
```

# Django Form
Django comes with a built-in Forms class which can be used with Django and python to create forms and send to the tempalte through `{{form}}`
## Reivew - Form
1. GET, POST, and CSRD review
2. Django Form Class Bascis
3. Form Fields and Validation
4. Form Widgets and CSS Styling
5. ModelForms

## GET, POST, and CSRD review
`GET` and `POST` methods are the key methods for http interaction (sending and receiving data)
- `GET`: request data from a specified resource(local | remote form, model, etc..). no used to update/create information
- `POST`: Request to send data to a server to create/update a resource, normaly raised by submit operation
- CSRD can be called by `{% csrf_token %}` and it's used to make sure the information `POST` or `GET` are legitimate

## Django Form Class Bascis
ref <a href="https://docs.djangoproject.com/en/4.1/topics/forms/">Working with Forms</a> for more.
Code example for Form Class
```python
from django import forms

class ReivewForm(forms.Form):
    # the variable create here will connect to TextInput widget of html 
    # with maybe defined a label
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    review = forms.CharField(label='Please write your review here')
```

To be able to use form class in html, we need to import `Form` Class into `views.py`
```python
def rental_review(request):
    # POST REQUEST --> FORM CONTENTS --> THANK YOU\
    # if actually post sth (through submit)
    if request.method == 'POST':
        # pass to review form
        form = ReivewForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect(reverse('cars:thank_you'))
    # ELSE, RENDER FORM
    else:
        # first time visite page, no submit operation
        # just create form
        form = ReivewForm
    return render(request, 'cars/rental_review.html', context={'form': form})
```

# Appendix

## Extensions

1. <a href="">Git History (git log)</a>
2. <a href="https://marketplace.visualstudio.com/items?itemName=alefragnani.project-manager">project-manager</a>
3. <a href="https://marketplace.visualstudio.com/items?itemName=codezombiech.gitignore">gitignore</a>
4. <a href="https://marketplace.visualstudio.com/items?itemName=ziyasal.vscode-open-in-github">open in github</a>

## Git plugs

1. <a href="https://github.com/git-ecosystem/git-credential-manager">git credential manager</a>
