# RIT Computer Science Community Website

### Contributing

##### Getting a copy

    git clone https://github.com/rit-csc/CSCWebsite

##### Dependencies & Frameworks

* [Python 3.3 or higher](https://www.python.org/download/releases/3.3.0/)
* [Django](https://www.djangoproject.com/) -- backend

    ```pip3 install Django```

* [icalendar](http://icalendar.readthedocs.org/en/latest/) -- for calendar stuff

    ```pip3 install icalendar```

* [dateutil](https://labix.org/python-dateutil) -- for more calendar stuff, specifically repeat events

    ```pip3 install python-dateutil```

##### Meat & Potatoes (Creating Pages)

Making a page is as easy as creating a html file in `csc_new/pages/templates/pages/`.

For backend-intensive pages, you will have to put a new url in `csc_new/csc_new/urls.py`
and a new view/context in `csc_new/pages/views.py`.

Static files (images, CSS, JavaScript, etc.) go in `staticfiles/PATH_TO_YOUR_FILE`.
To refer to a static file in a template, do the following (*__outside__ of a `{% verbatim %}` block*):
```
{% load static %}

<!-- other stuff -->

{% static PATH_TO_YOUR_FILE %}
```

Django will do the rest for you!

A [base template](csc_new/pages/templates/csc_new/base.html) exists for all pages.
All content that goes on every page should end up here.
To extend this template, put `{% extends 'csc_new/base.html' %}` at the top of your file
and include your content in blocks that use the template correctly.

**Note**:
All contributions from outside contributors will be code-reviewed by the projects committee chair
and/or the Systems Administrator before being pushed to the live website.

### Tests

To run tests, navigate to the `csc_new/` directory and run the following:

    python manage.py test

### License

Our website is open-sourced using the [MIT License](LICENSE).

