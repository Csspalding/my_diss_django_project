import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','my_diss_django_project.settings')

import django
django.setup()
from posts import Posts
from datetime import datetime

def populate():
# 
  p1 = Post(
    title='Post One: My first Web Development Project',
    body = "",
    created_at = datetime.now(),
    #image='img/project2.png'
  )
  p1.save()

  
  p3= Post(
    title='Post Three:',
    body = "",
    created_at = datetime.now(),
    #image='img/project2.png'
  )
  p3.save()

	p4  = Post(
    title='Post Four:',
    body = "",
    created_at = datetime.now(),
    #image='img/project2.png'
  )
  p4.save()



	
  


  




 # Start execution here!
if __name__ == '__main__': #keeps this  Python script as standalone, cannot be imported to other modules
	print("Starting posts population script...")
	populate()