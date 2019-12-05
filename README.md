my_diss_django_project author Cassie Spalding 2140148s dissertation project 2019
 
VERSION
Django 2.1.5
Python 3.6.7 :: Anaconda, Inc.
Pillow 5.1.4
Django-crispy-forms-1.7.2
Django-registration-redux==2.2

requirements.txt has the software requirements 
install by running the command
pip install -r requirements.txt

Warning** 
To avoid integrity error, before populating the database remove the Unique=True from cupcake_site.models.py the slug attribute of the Category model and from posts.models.py the slug attribute of the Post model, replace once the database has been populated

To populate the database run the following scripts
python populateCupcakeDb.py
python populatePostsDb.py 