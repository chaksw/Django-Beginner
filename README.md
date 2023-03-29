# Django Project

## Basic
### Start project
```bash
django-admin startproject project
django-admin startapp app
```

### Views Routing URLs
- View
View dictate what information is being shown to the client (html to render in function)
- URLs
URLs dictate where that information is shown on the website (function in view.py)

There work in concert so you can think of each View/URL pairing as a web page on the website.
In project level or app level, we need to define in urls.py the connection of routes in a list variable called urlpatterns using path() and include() Django functions

Likes:
 - html file define the content of page
 - view file define which html file will be sent to client (with certain logic) using 
  ```py
   - render()
   - HttpResponse()
   - HttpResponseNotFound()
   - HttpResponseRedirect()
  ```
 - urls file define where (urls path) a view should be displayed by using path() in urlpatterns[] list

## Template and Django template language
Refer [Layouts](/02-Django-and-Templates/my_site/templates/layouts.html) and  to [example](/02-Django-and-Templates/my_site/my_app/templates/my_app/variable.html) to view html example

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
- app
  - migrations
    - 0001_initial.py



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
 - Inserting new data into a SQL table by create a new instance of the class(models) and call `.save()` method to create an `INSERT` call to the SQL database <br>
 - Alternatively, usign the built-in `.objects.create()` method to both **create** and **save** the new data entry in a single line.
 - In instances where want to create multiple new data entries in bulk(庞大的), you can use the `.object.bulk_create()` methode to pass in a likst of newly created objects.

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
 - for more method aoubt database oprations, check <a href='https://docs.djangoproject.com/en/4.1/ref/models/querysets/'>QuerySet API</a>
 - for more keys of lookups, see <a href='https://docs.djangoproject.com/en/4.1/ref/models/querysets/#id4'>lookups list</a>

Operators are also available in Django (`& |`) by referring `Q()` object class

### Updating Models, Entries (add | delete)
- Entries updated can be done by overwriting attribute of existing data entry and call `.save()` to save the changes.
- Similarly, use `.delete()` to delete an object.


## Connecting Tempaltes and Database Models
- In **project urls**, add **app** as routing
- In **app urls**, create routing and connect to method in **views**
- In **views**, import models to use database models as variable and use as context of render() so that we built **connection of template and database models**
- In **html**, use django templates language to call context define in **views** 


# Django Admin
One of the MOST POWERFUL FEATURES of Django, able to automatically create an Admin interface, to have a graphical interface for interacting with data and users on the site.
<br>
Django has pre-built admin paths in site `urls.py` file(`'/admin'`) as well as indications of an existing Django Admin app (`"django.contrib.admin"`).
## Configuration of admin