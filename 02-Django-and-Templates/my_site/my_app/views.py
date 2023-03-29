from django.shortcuts import render

# Create your views here.


def exmaple_view(request):
    # refer to templates floder: my_app/templates/my_app/example.html
    return render(request, 'my_app/example.html')


def variable_view(request):
    my_var = {"first_name": 'rosaLind', 'last_name': 'franklin', 'some_list': [1, 2, 3], 'some_dict': {'inside_key': 'inside_value'},
              'user_logged_in': True}
    # recive request and send to template with context
    return render(request, 'my_app/variable.html', context=my_var)
