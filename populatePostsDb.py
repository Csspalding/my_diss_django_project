import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','my_diss_django_project.settings')

import django
django.setup()

from django.contrib.auth.models import User
from posts.models import Posts

from datetime import datetime
#populate Blog posts database 

#Requires a user to have been created, set a default user instance to pk 1 

def get_user_details():
      try:
          user = User.objects.get(pk=1)
      except User.DoesNotExist:#no users yet in the database 
          return None

#user with pk=1 should be the superuser created when the database is migrated
def user_or_default():
    pk=1
    users_list_pk ={}
    users_list_pk = get_user_details()
    for user in users_list_pk:
        return user.pk==1
    return pk
        
def populate():

      p1 = Posts(
        title='Post One: My first Web Development Project',
        body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        #slug=
        user=user_or_default(),
        created_at = datetime.now(),
        last_modified = datetime.now(),
        #status =1,
        #post_image=''
      )
      p1.save()

     

      # Print out the posts added.
      for p in Posts.objects.all():
         print("- {0} - {1}".format(str(p)) )
          #uses string method to print category name and page title as defined in model
      

    # Start execution here!
if __name__ == '__main__': #keeps this  Python script as standalone, cannot be imported to other modules
      print("Starting blog posts population script...")
      populate()