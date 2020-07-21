This tutorial is based upon the tutorial made by CodingEntrepreneurs on Youtube: https://www.youtube.com/watch?v=f1R_bykXHGE&list=WL&index=2&t=6s

One error that did occur was that I missed making the migrations
    
    $ python3 manage.py makemigrations

    and than:
    $ python3 manage.py migrate

Another error that did occur was that in my template configuration didn't recognize the path "tweets/templates/pages/home.html", but it accepts the path "tweets/templates/tweets/home.html" as it said in the documentation on the site https://docs.djangoproject.com/en/3.0/
