import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','my_diss_django_project.settings')

import django
django.setup()

from django.contrib.auth.models import User
from posts.models import Posts

from datetime import datetime
#populate Blog posts database 

#Requires a user to have been 
#set a default user instance to id 1 
#both these methods may be fuzz, also look at admin.py for PostAdmin class with def helper method, not yet migrated - check ER diagram first, as this is too complex and running in circles. 
def get_user_details():
      try:
          user = User.objects.get(id=id)
      except User.DoesNotExist:#no users yet in the database 
          return None

def user_or_default():
    id=1
    users_list_id ={}
    users_list_id = get_user_details()
    for user in users_list_id:
        return user.id==1
    return id
        
def populate():

      p1 = Posts(
        created_by_user=user_or_default(),
        title='Post One: My first Web Development Project',
        body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        created_at = datetime.now(),
        #image='img/project2.png'
        status =1
      )
      p1.save()

      p2 = Posts(
        created_by_user=1,
        title='Post Two:Five advantages of joining a Meet Up Group',
        body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        created_at = datetime.now(),
        #image='img/project2.png'
        status =1
      )
      p2.save()
      
      p3= Posts(
        created_by_user=1,
        title='Post Three: Free tools, which ones...?',
        body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        created_at = datetime.now(),
        #status =1
        #image='img/project2.png'
      )
      p3.save()

      p4= Posts(
        created_by_user=1,
        title='Post Four:My top tips for basic coding equipment.',
        body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        created_at = datetime.now(),
        status =1
        #image='img/project2.png'
      )
      p4.save()

      p5= Posts(
        created_by_user=1,
        title='Post Five: Inspirational Women in Tech',
        body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        created_at = datetime.now(),
        status=1
        #image='img/project2.png'
      )
      p5.save()


      # Print out the posts added.
      #for p in Posts.objects.all():
         # print("- {0} - {1}".format(str(p)) )
          #uses string method to print category name and page title as defined in model
      

    # Start execution here!
if __name__ == '__main__': #keeps this  Python script as standalone, cannot be imported to other modules
      print("Starting blog posts population script...")
      populate()