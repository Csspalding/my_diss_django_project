import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','my_diss_django_project.settings')

import django
django.setup()
from posts import Posts
from datetime import datetime
#populate Blog posts database 

def populate():

      p1 = Posts(
        title='Post One: My first Web Development Project',
        body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        created_at = datetime.now()
        #image='img/project2.png'
      )
      p1.save()

      p2 = Posts(
        title='Post Two:Five advantages of joining a Meet Up Group',
        body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        created_at = datetime.now()
        #image='img/project2.png'
      )
      p2.save()
      
      p3= Posts(
        title='Post Three: Free tools, which ones...?',
        body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        created_at = datetime.now()
        #image='img/project2.png'
      )
      p3.save()

      p4= Posts(
        title='Post Four:My top tips for basic coding equipment.',
        body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        created_at = datetime.now()
        #image='img/project2.png'
      )
      p4.save()

      p5= Posts(
        title='Post Five: Inspirational Women in Tech',
        body = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        created_at = datetime.now()
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