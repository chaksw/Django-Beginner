**Table of Contents** _generated with [DocToc](https://github.com/thlorenz/doctoc)_

-   [1. Django Learnning](#1-django-learnning)
    -   [1.1. Basic](#11-basic)
        -   [1.1.1. Start project](#111-start-project)
        -   [1.1.2. Views Routing URLs](#112-views-routing-urls)
    -   [1.2. Template and Django template language](#12-template-and-django-template-language)
    -   [1.3. Migration](#13-migration)
        -   [1.3.1. Base commands](#131-base-commands)
        -   [1.3.2. Steps for migrations](#132-steps-for-migrations)
    -   [1.4. Data Interaction (CRUD)](#14-data-interaction-crud)
        -   [1.4.1. ADD/INSERT data](#141-addinsert-data)
            -   [1.4.1.1. Relative Function](#1411-relative-function)
        -   [1.4.2. READ data](#142-read-data)
            -   [1.4.2.1. Relative Function](#1421-relative-function)
        -   [1.4.3. Updating Models, Entries (add | delete)](#143-updating-models-entries-add--delete)
    -   [1.5. Connecting Tempaltes and Database Models](#15-connecting-tempaltes-and-database-models)
-   [2. Django Admin](#2-django-admin)
    -   [2.1. Model admin object class](#21-model-admin-object-class)
    -   [2.2. Resigter model in to admin](#22-resigter-model-in-to-admin)
    -   [2.3. ModelAdmin Class example](#23-modeladmin-class-example)
-   [3. Django Form](#3-django-form)
    -   [3.1. Reivew - Form](#31-reivew---form)
    -   [3.2. HTTP (Hyptertext Transfer Protocol)](#32-http-hyptertext-transfer-protocol)
    -   [3.3. GET, POST, and CSRD review](#33-get-post-and-csrd-review)
    -   [3.4. Django Form Class Bascis](#34-django-form-class-bascis)
    -   [3.5. Form widget and styling - widget attributes](#35-form-widget-and-styling---widget-attributes)
    -   [3.6. ModelForm](#36-modelform)
    -   [3.7. ModelForms Customizaton](#37-modelforms-customizaton)
-   [4. Class-Based Views(CBVs)](#4-class-based-viewscbvs)
    -   [4.1. TemplateView](#41-templateview)
    -   [4.2. FormView](#42-formview)
        -   [4.2.1. `cleaned_data()`](#421-cleaned_data)
    -   [4.3. Model based CBVs (Class Based Views)](#43-model-based-cbvs-class-based-views)
        -   [4.3.1. CreateView](#431-createview)
            -   [4.3.1.1. **Important Note**](#4311-important-note)
        -   [4.3.2. ListView](#432-listview)
        -   [4.3.3. DetailView](#433-detailview)
        -   [4.3.4. UpdateView](#434-updateview)
        -   [4.3.5. DeleteView](#435-deleteview)
        -   [4.3.6. HOME Page](#436-home-page)
-   [5. jQuery](#5-jquery)
    -   [5.1. Basics](#51-basics)
        -   [5.1.1. Styling element with object](#511-styling-element-with-object)
        -   [5.1.2. Styling element in list](#512-styling-element-in-list)
        -   [5.1.3. Grap content using jQuery](#513-grap-content-using-jquery)
        -   [5.1.4. Change attribute](#514-change-attribute)
        -   [5.1.5. Add `css` class into `html`](#515-add-css-class-into-html)
        -   [5.1.6. Events](#516-events)
    -   [5.2. Event animation (Effects)](#52-event-animation-effects)
-   [6. Appendix](#6-appendix)
    -   [6.1. Extensions](#61-extensions)
    -   [6.2. Git plugs](#62-git-plugs)
-   [Django Project -SCGA](#django-project--scga)
    -   [Data Structure](#data-structure)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 1. Django Learnning

## 1.1. Basic

### 1.1.1. Start project

```bash
django-admin startproject project
django-admin startapp app
```

### 1.1.2. Views Routing URLs

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

## 1.2. Template and Django template language

Refer [Layouts](/02-Django-and-Templates/my_site/templates/layouts.html) and to [example](/02-Django-and-Templates/my_site/my_app/templates/my_app/variable.html) to view html example

## 1.3. Migration

### 1.3.1. Base commands

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

Run any existing migrations (typically created through the `makemigrations` command). <br>
This is actually running the files under the migrations directory created by makemigrations

```bash
python manage.py sqlmigrate app 0001
```

After running migrate command, if wanna to see what the SQL code looked like, you could run the sqlmigrate command to view. <br>
PS: Typically we won't reviewthe files created under the migrations directory or run sqlmigrate

### 1.3.2. Steps for migrations

1. Inital project migrate command
2. Create app and create models (datebase)
3. Register app in INSTALLED_APP in setting.py
4. Run makemigrations for new app
5. Run migrate for new migrations

## 1.4. Data Interaction (CRUD)

Something like `MyModel.objects` is Django Model Manager. This Manager can do the CRUD of database and also provides other enhanced functions

### 1.4.1. ADD/INSERT data

#### 1.4.1.1. Relative Function

```python
MyModel.objects.save() # INSERT, to create we need to create an instance of object first
MyModel.objects.objects.create() # CREATE AND SAVE
MyModel.objects.bulk_create() # CREATE a bulk data
```

-   Inserting new data into a SQL table by create a new instance of the class(models) and call `.save()` method to create an `INSERT` call to the SQL database <br>
-   Alternatively, usign the built-in `.objects.create()` method to both **create** and **save** the new data entry in a single line.
-   In instances where want to create multiple new data entries in bulk(庞大的), you can use the `.object.bulk_create()` methode to pass in a likst of newly created objects.

### 1.4.2. READ data

#### 1.4.2.1. Relative Function

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

-   for more method aoubt database oprations, check <a href='https://docs.djangoproject.com/en/4.2/ref/models/querysets/'>QuerySet API</a>
-   for more keys of lookups, see <a href='https://docs.djangoproject.com/en/4.2/ref/models/querysets/#id4'>lookups list</a>

Operators are also available in Django (`& |`) by referring `Q()` object class

### 1.4.3. Updating Models, Entries (add | delete)

-   Entries updated can be done by overwriting attribute of existing data entry and call `.save()` to save the changes.
-   Similarly, use `.delete()` to delete an object.

## 1.5. Connecting Tempaltes and Database Models

-   In **project urls**, add **app** as routing
-   In **app urls**, create routing and connect to method in **views**
-   In **views**, import models to use database models as variable and use as context of render() so that we built **connection of template and database models**
-   In **html**, use django templates language to call context define in **views**

# 2. Django Admin

Take Project [car](./04-Django-Admin-Portal/my_car_site/) as an example, inside which apply all previous learning
One of the MOST POWERFUL FEATURES of Django, able to automatically create an Admin interface, to have a graphical interface for interacting with data and users on the site.
Django has pre-built admin paths in site `urls.py` file(`'/admin'`) as well as indications of an existing Django Admin app (`"django.contrib.admin"`).
Admin panel is meant for a manager of the website. so we need to **create a 'superuser'**

```bash
python manager.py createsuperuser
# enter username, email and password
```

## 2.1. Model admin object class

## 2.2. Resigter model in to admin

In `admin.py` of app, use `admin.site.register(model, modeladmin)` to add Model to administrator site. (ref <a href="https://docs.djangoproject.com/en/4.2/ref/contrib/admin/">Modeladmin</a>)

## 2.3. ModelAdmin Class example

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

# 3. Django Form

Django comes with a built-in Forms class which can be used with Django and python to create forms and send to the tempalte through `{{form}}`

## 3.1. Reivew - Form

1. GET, POST, and CSRD review
2. Django Form Class Bascis
3. Form Fields and Validation
4. Form Widgets and CSS Styling
5. ModelForms

## 3.2. HTTP (Hyptertext Transfer Protocol)

foundation for the method of **sending** and **receiving** data over the world wide web.

## 3.3. GET, POST, and CSRD review

`GET` and `POST` methods are the key methods for http interaction (sending and receiving data)

-   `GET`: request data from a specified resource (local | remote form, model, etc..). not used to update/create information (请求从网页服务器上接受数据)
-   `POST`: Request to send data to a server to create/update a resource, normaly raised by submit operation
-   CSRD can be called by `{% csrf_token %}` and it's used to make sure the information `POST` or `GET` are legitimate （请求向网页服务器上发送数据（更新/添加/删除））

## 3.4. Django Form Class Bascis

Django `form.py` used to create a form field (class) that ends up generating a Django widget which in turn renders the actual HTML form input/label tags
ref <a href="https://docs.djangoproject.com/en/4.2/topics/forms/">Working with Forms</a> for more.<br>
**Code example for Form Class**

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

To be able to passing form class to template(html), we need to import `Form` Class into `views.py`

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

When passing `{{form}}` to the template, we saw that the HTML tags rendered by the Django Form Widgets are all in the same line and don't look visually appealing.
Actually, there are more details around template rendering inside the .html files<br>
PS: Render 是渲染的意思， Django 创建的 from 用来渲染 HTML

**Example:**

```html
<div class="container">
    <form action="" method="POST">
        {% csrf_token %}
        <div>
            <h2>Dispaly as paragraph</h2>
            <!-- Display as paragraph-->
            {{form.as_p}}
        </div>
        <div>
            <h2>Dispaly as list</h2>
            <!-- Display as list -->
            {{form.as_ul}}
        </div>
        <div>
            <h2>Dispaly as table</h2>
            <!-- Display as table -->
            {{form.as_table}}
        </div>
        <div>
            <h2>Pass attribute</h2>
            <!-- passing only label-->
            {{ form.first_name.label_tag }}
            <!-- passing only field-->
            {{ form.first_name }}
            <p></p>
            <!-- passing only label-->
            {{ form.last_name.label_tag }}
            <!-- passing only field-->
            {{ form.last_name }}
        </div>

        <div>
            <h2>Loop the form</h2>
            {% for field in form %}
            <div class="mb-3">{{ field.label_tag }}</div>
            {{ field }} {% endfor %}
        </div>

        <input type="submit" />
    </form>
</div>
```

## 3.5. Form widget and styling - widget attributes

To have more control over styling and presentation, we can access <a href="https://docs.djangoproject.com/en/4.2/ref/forms/widgets/">widget</a> attributes.
Linking a **static files** directory to hold our custom css files:

-   Create app/static/app/custom.css file
-   Load static directory in .html

```django-html
{% load static %}
```

-   Link static CSS file connection

```html
<link rel="stylesheet" href="{% static 'appname/cssfile.css' %}" />
```

-   Run migrate to load new app in setting.py file

**Example:**

```python
from django import forms

class ReivewForm(forms.Form):
    # the variable create here will connect to TextInput widget of html
    # with maybe defined a label
    first_name = forms.CharField(label='First Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    # use widget in python and call css style using "attrs={'class':'myform'}"
    # all the attribute of certain HTML tag can be passed in as a dictionary in the "attrs" of widget
    review = forms.CharField(label='Please write your review here', widget=forms.Textarea(attrs={'class':'myform', 'rows': '2', 'cols': '2'}))
```

## 3.6. ModelForm

`ModelForm` class automatically creates a Form with fields connected to each model field.
自动创建 instance 来保存前端数据，并连接保存到 modelfield 中？

-   Create ModelForm in `models.py`

```python
from django.db import models

# Create your models here.
class Review(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    stars = models.IntegerField()
```

-   Register Model in `admin.py` <br>
    `admin.site.register(Review)`

-   Make migration to apply model <br>

```bash
python manage.py makemigrations
python manage.py migrate
```

-   <a href="https://docs.djangoproject.com/en/4.2/topics/forms/modelforms/">Creating form from models</a>
    See doc for more information about specify form style

```python
from django import forms
from .models import Review
from django.forms import ModelForm

# Creating form from models
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['first_name', 'last_name', 'stars']
```

-   In `view.py`, save data create POST from user

```python
if request.method == 'POST':
        # pass to review form
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect(reverse('cars:thank_you'))
# ELSE, RENDER FORM
else:
    # first time visite page, no submit operation
    # just create form
    form = ReviewForm
return render(request, 'cars/rental_review.html', context={'form': form})
```

## 3.7. ModelForms Customizaton

1. Customize Error Message of `Interge Field` refer Built-in Field classes in <a href="https://docs.djangoproject.com/en/4.2/ref/forms/fields/">Field Class</a><br>
   **Example:** in `forms.py`

```python
class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__" # pass all the model fields as form fields
        # fields = ['first_name', 'last_name', 'stars']
        # over write label
        labels = {
            'first_name': "YOUR FIRST NAME",
            'last_name' : "Last Name",
            'stars':'Rating'
        }
        error_message = {
            'stars':{
                'min_value': "YO! Min value is 1",
                'max_value': "YO! YO! Max value is 5",
            }
        }
```

# 4. <a href="https://docs.djangoproject.com/en/4.2/topics/class-based-views/">Class-Based Views(CBVs)</a>

Django privodes an entrie View class system that is very powerful for quickly rendering commonly used views.
Django CBVs come with many pre-build generic class views for common tasks, such as listing all the values for a particular model in a database (ListView) or creating a new instance of a model object (CreateView).

-   Templateview
-   Formview
-   Listview
-   UpdateView
-   DeleteView

## 4.1. TemplateView

```python
from django.views.generic import TemplateView
# Create your views here.
class HomeView(TemplateView):
    template_name = 'classroom/home.html'
```

in `urls.py`

```python
urlpatterns = [
    path('', HomeView.as_view(), name='home')  # path expects a function!
]
```

## 4.2. FormView

-   Create a form in `forms.py`
-   import form in `views.py`
-   Create a form view class in `views.py`

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
```

```python
from .forms import ContactForm
class ContactFormView(FormView):
    # connect form class to form view class
    form_class = ContactForm
    template_name = 'classroom/contact.html'

    # success URL ? where to go to after submit successfully
    # reverse() returns a string and reverse_lazy() returns an object
    # if using success_url, use reverse_lazy().
    success_url = reverse_lazy('classroom:thank_you')
    # What to do with form ?

    def form_valid(self, form):
        print(form.cleaned_data['name'])
        # ContactFormView(request.POST)
        return super().form_valid(form)
        # form.save()
    # cleaned_data is a dictionary
```

### 4.2.1. `cleaned_data()`

The clean() method on a Field subclass is responsible for running to_python(), validate(), and run_validators() in the correct order and propagating their errors. If, at any time, any of the methods raise ValidationError, the validation stops and that error is raised. This method returns the clean data, which is then inserted into the cleaned_data dictionary of the form.

## 4.3. Model based CBVs (Class Based Views)

There are a few operations with models

### 4.3.1. CreateView

Django provodes CBVs that automatically create the appropriate views, forms, and context objects for predefined template names by simply being connected to a model(database)<br>
These classes require just a few attributes and automatically do the work for you !<br>

-   model_form.html - teacher_form.html
    <br>

#### 4.3.1.1. **Important Note**

Because the classes are designed to be simple, these views require a template name to follow specific pattern. (`templatename`\_form.html)

```python

class TeacherCreateView(CreateView):
    model = Teacher # connect to a model(database)
    # fields = ['first_name', 'last_name'] # connect to data attribute
    fields = '__all__'
    # reverse to another template after submit, 'thank_you` is name of path defined in urls
    success_url = reverse_lazy('classroom:thank_you')

```

once defined `model = Teacher` to connect to model, django will create a `form` based on model look for the template named `modelname_form.html` just like the definition of `template_name = 'classroom/teacher_form.html`, then the created form will be used once you call `form.as_p` in html. Also when you hit the submit button, it's will automatically hit `save()` after all the field are validated.

```html
<h1>Teacher Form</h1>
<form action="" method="POST">
    {% csrf_token %} {{ form.as_p }}
    <input type="submit" value="Submit" />
</form>
```

### 4.3.2. ListView

`ListView` used to list all the instances for a particular model.
A `ListView` will do a query request for all the objects inside the model look for the template named `modelname_list.html`

```python
class TeacherListView(ListView):
    # model_list.html
    model = Teacher
    # Grab instances in model
    queryset = Teacher.objects.all()
    # define the list name used in html
    context_object_name = "teacher_list"
```

```html
<h1>List of Teachers (ListView)</h1>
<ul>
    {% for teacher in teacher_list %}
    <li>{{ teacher.first_name}} {{ teacher.last_name }}</li>
    {% endfor %}
</ul>
```

### 4.3.3. DetailView

The main purpose of the `DetailView` is to view a single instance of (PK) a particular entry inside a model.A `DetailView` will look fort he template named `modelname_detail.html`

```python
class TeacherDetailView(DetailView):
    # RETURN ONLY ONE MODEL ENTRY using primary key
    model = Teacher
    # PK --> {{ teacher }}
```

A `DetailView` will only grab a unique model entry by referring their primary key. by doing that the URL actually needs to be set up in a way to specifically refer to that primary key.

```python
path('teacher_detail/<int:pk>', TeacherDetailView.as_view(), name='detail_teacher')
```

Then we need to set up the link in a way on template side of things so that we can pass the primary key to the URL

```html
<h1>List of Teachers (ListView)</h1>
<ul>
    {% for teacher in teacher_list %}
    <li>
        <a href="/classroom/teacher_detail/{{teacher.id}}"
            >{{ teacher.first_name}} {{ teacher.last_name }}</a
        >
    </li>
    {% endfor %}
</ul>
```

### 4.3.4. UpdateView

`UpdateView` is kind of like a mix between a `CreateView` and a `DetailView`, it's kind of like a `CreateView` because you will be filling out a form to up the information. but it's also kind of like a `DetailView` because when you're talking about updating, you're talking aoubt a specific entry with a unique primary key.<br>
The intention of `UpdateView`, it's to SHARE the `model_form.html` from HTML template that `CreateView` also uses, and it looks a lot like create view as far as attributes concerned, but we can limit the field upon updating.<br>
In coding, kind of like using `CreateView` **views form** and using `UpdateView` **html form**

```python
class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = ['last_name', 'first_name']
    # fields = '__all__'
    success_url = reverse_lazy('classroom:list_teacher')
```

URL will be:

```python
path('update_teacher/<int:pk>', TeacherUpdateView.as_view(), name='update_teacher')</int:pk>
```

HTML will be (using `teacher_list.html`)

```html
<h1>List of Teachers (ListView)</h1>
<ul>
    {% for teacher in teacher_list %}
    <li>
        <a href="/classroom/teacher_detail/{{teacher.id}}"
            >{{ teacher.first_name}} {{ teacher.last_name }}</a
        >
        <ul>
            <li>
                <a href="/classroom/update_teacher/{{teacher.id}}"
                    >Update Information for {{ teacher.first_name }}</a
                >
            </li>
        </ul>
    </li>
    {% endfor %}
</ul>
```

### 4.3.5. DeleteView

Used to pointed to a primary key and delete a particular instance of the model<br>
`DeleteView` is technically a form, it sends back a form that just has a single confirmed deleted button.<br>
A `DeleteView` will look fort he template named `modelname_confirm_delete.html`<br>
In `ListView` we have link button links to the particular primary key.<br>

```html
<h1>List of Teachers (ListView)</h1>
<ul>
    {% for teacher in teacher_list %}
    <li>
        <a href="/classroom/teacher_detail/{{teacher.id}}"
            >{{ teacher.first_name}} {{ teacher.last_name }}</a
        >
        <ul>
            <li>
                <a href="/classroom/update_teacher/{{teacher.id}}"
                    >Update Information for {{ teacher.first_name }}</a
                >
            </li>
            <li>
                <a href="/classroom/delete_teacher/{{teacher.id}}"
                    >DELETE {{ teacher.first_name }}</a
                >
            </li>
        </ul>
    </li>
    {% endfor %}
</ul>
```

Once link is cliked, it's will go head and go to the `delete_theacher` url (refer to `urls.py`), and brings back to the `DeleteView`, which connects to the teacher model and renders(calls) the `teacher_confirm_delete.html`.<br>

-   **URLs**

```python
path('delete_teacher/<int:pk>', TeacherDeleteView.as_view(), name='delete_teacher')
```

-   `DeleteView`

```python
class TeacherDeleteView(DeleteView):
    model = Teacher
    # default template name:
    # model_confirm_delete.html
    success_url = reverse_lazy('classroom:list_teacher')
```

-   `teacher_confirm_delete.html`

```html
<h1>Are you sure you want to delete this teacher?</h1>
<h2>{{ teahcer }}</h2>
<form action="" method="post">
    {% csrf_token %}
    <input type="submit" name="" id="" value="Confirm Delete" />
</form>
```

After submit button is clicked, it's will go ahead and execute the deletion.

### 4.3.6. HOME Page

```html
<h1>Welcome to home.html</h1>
<ul>
    <li>
        <a href="{% url "classroom:thank_you" %}">THANK YOU PAGE LINK</a>
    </li>
    <li>
        <a href="{% url "classroom:contact" %}">CONTACT FORM PAGE LINK</a>
    </li>
    <li>
        <a href="{% url "classroom:create_teacher" %}">CREATE NEW TEACHER FORM PAGE LINK</a>
    </li>
    <li>
        <a href="{% url "classroom:list_teacher" %}">LIST TEACHER FORM PAGE LINK</a>
    </li>
</ul>
```

# 5. <a href="https://releases.jquery.com/">jQuery</a>

jQuery is a `javascript` library (a large single `.js` file) that has many pre-built methods and objects that simplify workflow, specifucally when you interacting with the DOM and making HTTP requests (AJAX)<br>
One of its main features is the use of `$`.

-   Grap attribute

```js
// jQuery
let divs = $('div');

// Vanilla
let divs = documents.querySelectorAll('div');
```

In situation we actullay want to edit the **styling** of a certain variable called `el`.

-   Styling

```js
// jQuery
$(el).css('border-width', '20px');

// Vanilla
el.style.borderWidth = '20px';

// Styling element with css style object
const newCss = {
    color: 'white',
    background: 'green',
    border: '20px solid red',
};

let list = $('h1');
list.css(newCss);
```

-   Function called

```js
// jQuery
$(document).ready(function () {});

// Vanilla
function ready(fn) {
    if (document.readyState != 'loading') {
        fn();
    } else {
        document.addEventListener('DOMConetentLoaded', fn);
    }
}
```

## 5.1. Basics

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>jQuery</title>
        <style>
            .turnBlue {
                color: white;
                background: blue;
            }
            .turnRed {
                color: white;
                background: red;
            }
        </style>
        <!-- Get Bootstrap -->
        <link
            href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css"
            rel="stylesheet"
            integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ"
            crossorigin="anonymous" />
        <!-- Get jQuery -->
        <script
            src="https://code.jquery.com/jquery-3.6.4.js"
            integrity="sha256-a9jBBRygX1Bh5lt8GZjXDzyOB+bWve9EiO7tROUtj/E="
            crossorigin="anonymous"></script>
    </head>
    <body>
        <h1>Selection with jQuery</h1>
        <p>
            You can use the $ to select elements from the DOM, it will fell a
            lot like selection using querySelectorAll()
        </p>
        <p>For example:</p>
        <ul>
            <li>
                Selecting all 'a' Tags:
                <ul>
                    <li>$('a')</li>
                </ul>
            </li>
            <li>
                Selecting all element from the class "container":
                <ul>
                    <li>$('.container')</li>
                </ul>
            </li>
            <li>
                Selecting all elements with id "special":
                <ul>
                    <li>$('#special')</li>
                </ul>
            </li>
        </ul>
    </body>
</html>
```

### 5.1.1. Styling element with object

```js
// Styling element with css style object
const newCss = {
    color: 'white',
    background: 'green',
    border: '20px solid red',
};

let list = $('h1');
list.css(newCss);
```

### 5.1.2. Styling element in list

```js
var listItems = $('li');
// use .eq to index element in list
listItems.eq(0).css('color', 'orange');

// negative index for last elemnt
listItems.eq(-1).css('color', 'orange');
```

### 5.1.3. Grap content using jQuery

The JQuery `html()` and `text()` methods are two methods that you can use to get or set the contents of an HTML element. The difference between them is stated below: <br>
`html()` is used to return or change the **html** and **text** content of an element. `text()` can only return or change the text content of an element.

```js
$('h1').text();
// Change text in page (temporatry)
$('h1').text('Brand New Text');
// Actullay change html
$('h1').html('<em>New</em>');
```

### 5.1.4. Change attribute

```js
// change attribute 'type' from 'submit' to 'checkbox'
$('input').eq(1).attr('type', 'checkbox');
// change attribute 'value'
$('input').eq(0).val('new value');
```

### 5.1.5. Add `css` class into `html`

We add add the pre-defined `css` class in to element using `addClass()`, and use `removeClass()` to remove the class. We can also toggle to class in elemnt using `toggleClass()`

```js
// add class
$('h1').addClass('turnRed');
// remove class
$('h1').removeClass('turnRed');
// toggle class
$('h1').toggleClass('turnBlue');
```

### 5.1.6. [Events](https://api.jquery.com/category/events/)

-   Event `click()`

```js
// Event 'Click'
$('h1').click(function (e) {
    console.log('There was a click!');
});

// Grap multiple event
$('li').click(function (e) {
    console.log('any li was clicked!');
});
```

-   `this` key word: `this` means any object we selected, here is 'h1'

```js
// use 'this' key word
$('h1').dblclick(function (e) {
    //
    $(this).text('Double click is triggered');
    console.log($(this).text());
});
```

-   Event `keypress()` : Each key has number code that stored in event.which()

```js
// Key press
$('input')
    .eq(0)
    .keypress(function (event) {
        // Each key has number code that stored in event.which()
        // 'enter' = 13
        if (event.which === 13) {
            console.log(event);
            $('h3').toggleClass('turnBlue');
        }
    });
```

-   `on()` : `on()` method essentially act like addEventListener

```js
// on()
$('h1').on('dblclick', function () {
    $(this).toggleClass('turnBlue');
});

// grap mouseEnter using on()
$('h1').on('mouseenter', function () {
    $(this).toggleClass('turnBlue');
});
```

## 5.2. Event animation ([Effects](https://api.jquery.com/category/effects/))

```js
// event animation
$('input')
    .eq(1)
    .on('click', function () {
        // grap every thing in the `.container` class
        // fadeOut(x), make selector disappear in x milleseconds
        // $(".container").fadeOut(1000);
        // slideUp()
        $('.container').slideUp(1000);
    });
```

# 6. Appendix

## 6.1. Extensions

1. <a href="">Git History (git log)</a>
2. <a href="https://marketplace.visualstudio.com/items?itemName=alefragnani.project-manager">project-manager</a>
3. <a href="https://marketplace.visualstudio.com/items?itemName=codezombiech.gitignore">gitignore</a>
4. <a href="https://marketplace.visualstudio.com/items?itemName=ziyasal.vscode-open-in-github">open in github</a>

## 6.2. Git plugs

1. <a href="https://github.com/git-ecosystem/git-credential-manager">git credential manager</a>

# Django Project -SCGA

## Data Structure

-   Project 1(F6)
    -   Function 1(GGF)
        -   Load 1 (Configuration ID <- Dilivery Letter)
            -   Process 1
                -   Module 1 (file.cpp)
                    -   Methode 1
                        -   Code Line Number 1
                        -   Code Line Number 2
                        -   ...
                    -   Methode 2
                    -   ...
                -   Module 2
                -   ...
            -   Process 2
            -   ...
        -   Load 2
        -   ...
    -   Function 2(MWF)
    -   ...
-   Project 2
-   ...
