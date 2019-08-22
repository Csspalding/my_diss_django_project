import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','my_diss_django_project.settings')

import django
django.setup()
from cupcake_site.models import Category, Page

#WARNING DO NO REPOPULATE DATABASE WITHOUT REMOVING THE SLUG.MODEL.SLUGFIELD UNIQUE=TRUE ATTRIBUTE IN MODEL.PY
#AND REMOVING ADMIN.PY REGISTER SLUG
#CHECK TANGO BOOK PG 77 FIRST!!

def populate():
  	
  	
# 3 lists of dictionaries containing pages to add to each category 
		book_pages = [
				{"title":"Invent Your own Computer Games with Python",
				"description":"If your interested in basic games as a way to start try this, available to read free on line from the link", 
				"url":"https://inventwithpython.com/", 
				"views":9 },

				{"title":"Automate the Boring Stuff with Python",
				"description":"Another classic great starter book available to read free on line at this link", 
				"url":"https://inventwithpython.com/",
				"views":9} ,

				{"title":"Head First Python", 
				"description":"A modern book available from most Local Libraries. Head First cover lots of coding languages, this one is Python, great for beginers with a very visual and fun, learn by doing. This link requires you register with O'Reilly.", 
				"url":"http://shop.oreilly.com/product/0636920036777.do",
				"views":9},

				{"title":"Python Cookbook", 
				"description":"Available free from this link, this book is daunting for beginers but a great comprehensive guide to Python version 3. Learn Python the Hard Way is a better way to get started", 
				"url":"https://github.com/sjyuan-cc/programming-books/blob/master/Language/Python/Python%20Cookbook%2C%203rd%20Edition.pdf",
				"views":9},

				{"title":"Packt", 
				"description":"This site offers discounts and features different Free eBook every day you can save to your account and read on line if you register. Wide ranging e-books for various stages of learning. ", 
				"url":"https://www.packtpub.com/gb/",
				"views":9},
				
				{"title":"Learn Python the Hard Way",
				"description":"A starter book that drums in the basics for total beginers, who like learning by reading and writing, widely available to read for free on line, the link here requires you register with O'Reilly.", 
				"url":"https://www.oreilly.com/library/view/learn-python-the/9780133124316/",
				"views":9} ]

		web_pages = [
				{"title":"22 Ways to Learn to Code for Free in 2019",
				"description":"A comprehensive list of 22 different ways to learn code explained in detail by Jamie Spencer in a blog post for Make A Website Hub",
				"url":"https://makeawebsitehub.com/learn-to-code-for-free/", 
				"views":64},

				{"title":"Top 10 ways to teach yourself to code",
				"description":"Advice on how to start learning to code by Melanie Pinola and Gloria Sin and which learning tools to try out, including a guide to deciding which programing language to learn.", 
				"url":"https://lifehacker.com/top-10-ways-to-teach-yourself-to-code-1684250889",
				"views":77 },

				{"title":"Complete Beginers Guide to Interaction Design",
				"description":"If your interested in User Experience (UX)also referred to as UI for user interaction this link is a great guide written by the UXBooth editorial team", 
				"url":"https://www.uxbooth.com/articles/complete-beginners-guide-to-interaction-design/",
				"views":2},

				{"title":"Official Python Documentation",
				"description":"This isn't the most friendly page for total beginers, but it is the essential documentation of Python language, includes set up instructions, and all the code syntax a bit like a language dictionary with grammar, as you become more advanced this documentation becomes more readable and useful as a reference", 
				"url":"https://docs.python.org/3/",
				"views":10} ]

		video_pages = [
				{"title":"Coding Blond",
				"description":"Great video tutorials on everything to do with tech by a female presenter, topic are far and wide ranging include women in tech, programming, lifestyle, computor science concepts, brilliant!", 
				"url":"https://www.youtube.com/channel/UCjdRbKZ494DfZ4zeX19rICw",
				"views":10},

				{"title":"Derek Banas You Tube Channel ",
				"description":"Excellent teacher fast pace up beat video tutorials for beginers in a wide range of programming languages, in-depth courses as well as intensive 'Everything you need to know in one hour' videos", 
				"url":"https://www.youtube.com/user/derekbanas",
				"views":10},

				{"title":"Travis Media You Tube Channel ",
				"description":"Great video tutorials on coding, web development and freelancing", 
				"url":"https://www.youtube.com/channel/UCGPGirOab9EGy7VH4IwmWVQ",
				"views":10},

				{"title":"Free Code Camp You Tube Channel",
				"description":"Tutorials on a range of Programming languages, Web development and Computer Science concepts", 
				"url":"https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ",
				"views":10},

				{"title":"Codecademy",
				"description":"Tips for beginers learning to code, short videos on technical terms and Computer Science concepts", 
				"url":"https://www.youtube.com/channel/UC5CMtpogD_P3mOoeiDHD5eQ/featured",
				"views":10},

				{"title":"Khan Academy",
				"description":"Global student resource on many subjects areas, excellent videos by teachers and lecturers explaining programming, technical terms, Maths, Data Science, Computer Science concepts", 
				"url":"https://www.youtube.com/user/khanacademy",
				"views":10}	]
			
		meetup_pages=[
				{"title":"Ladies Of Code",
				"description":"Supporting and encouraging group who network with cake, informal, regular talks from experts, beginers welcome,always at professional venues, recommended",
				"url":"https://www.meetup.com/Ladies-of-Code-Glasgow/",
				"views":0},

				{"title":"Women in Tech uk",
				"description":"If you are serious about a career in tech at some point you may want to join this group of female digital technology professionals who network, discuss tech topics and host presentation",
				"url":"https://www.meetup.com/Women-in-Tech-Scotland-Meetup/",
				"views":0},

				{"title":"Codebar",
				"description":"Non profit organisation faciliating diversity in tech by running free  on-site programming workshops with expert coaches, beginers welcome, highly recommended, held at professional venues",
				"url":"https://codebar.io/glasgow",
				"views":0},	
				
				{"title":"Code Craft",
				"description":"Aimed at increasing diversity, Glasgow based, this group debate how to write code well, Guided Conversations, Lean Coffee and Workshops as well as an annual Code Craft Conference in September, be warned some topics are quite advanced, held at professional venues",
				"url":"https://www.codecraftuk.org/",
				"views":0},

				{"title":"Glasgow Coding Meet Up",
				"description":"Informal group sharing the experience of learning to code, and learning web development offering presentations on beginers topics - beginers welcome, pub venue",
				"url":"https://www.meetup.com/Glasgow-Coding-Meetup/",
				"views":0}]


		course_pages = [ 
				{"title": "Code First: Girls",
				"description":"Their 20:20 campaign aims to teach 20,000 women to code by 2020. They offer free certified on-site in person courses for students, and female professionals. They work along side companies to offer corperate education and community partnerships.", 
				"url":"https://www.codefirstgirls.org.uk/courses-we-offer.html", 
				"views":87},

				{"title": "Codecademy",
				"description":"Free interactive courses with short bite size lessons progressing to develop technical coding skills", 
				"url":"https://www.codecademy.com/", 
				"views":87},

				{"title": "Khan Academy",
				"description":"Introducing the basics for all kinds of coding activities", 
				"url":"https://www.khanacademy.org/computing/computer-programming", 
				"views":87},

				{"title":"Free Code Camp",
				"description":"Free interactive coding courses, and open source projects", 
				"url": "https://www.freecodecamp.org/", 
				"views":16},

				{"title":"Coursera Python for Everyone",
				"description":"A great introduction to coding for beginers. Corsera are a hugh on line library of courses on every topic, taught by professionals. Learning videos are free. If you want to be certified or to access course materials or support from a tutor there is a small course fee",
				"url": "https://www.coursera.org/specializations/python", 
				"views":16},

				{"title":"Udemy",
				"description":"Another e-learning platform offering thousands of wide ranging video tutorials. Many coding and web development courses available for free, some courses cost a fee", 
				"url": "https://www.udemy.com/", 
				"views":16},

				{"title":"Learnpython.org",
				"description":"Excellent beginers tutorial on Python", 
				"url": "https://www.learnpython.org/", 
				"views":16},

				{"title":"DataCamp",
				"description":"Learn data science and much more.",
				"url": "https://www.datacamp.com/?utm_source=learnpython_com&utm_campaign=learnpython_tutorials", "views":16},

				{"title":"W3schools",
				"description":"Interactive coding for beginers web development", 
				"url": "https://www.w3schools.com/", 
				"views":16},

				{"title": "Code.org",
				"description":"Fun and wide ranging One Hour Tutorials & Videos on Coding Activities for beginers, kids and a teacher resource site", 
				"url":"https://code.org/learn", 
				"views":67},

				{"title": "Techmums",
				"description":"Aims to take the mystery out of technology. Register for guides to Social Media, Staying Safe Online, and The Cloud & Google Drive, also run on-site technology workshops at schools", 
				"url":"https://techmums.co", 
				"views":67},

				{"title": "Mit",
				"description": "If you are academic and enjoy university lectures, Massachusetts Institute of Technology offer free education for all by providing video recordings of university lectures by professers. For a whole list of introductory courses in Computor Science with comprehensive materials type 'Python' in the search bar",
				"url":"https://web.mit.edu/", 
				"views":8},]

  #games = []
	#chat groups- many of the groups also have twitter feeds or facebook pages to follow put on about page, how about meet up groups?
	#pod casts []
	#events

		women_pages= [
				{"title":"Girls In Tech",
				"description":"Global non profit aimed at engaging young girls and women into Tech Industry, career development, help with Start Ups aims to empower and educate",
				"url":"https://girlsintech.org/",
				"views":3},

				{"title":"Girls Who Code",
				"description":"On site free classes, schools clubs and summer programmes to encourage girls and women into computor science.",
				"url":"https://uk.girlswhocode.com/",
				"views":3},

				{"title":"Girl Develop It",
				"description":"Aims to create opportunities for women learning to code with on-site classes and support, USA based",
				"url":"https://www.girldevelopit.com/",
				"views":3},

				{"title":"Women in Tech UK", 
				"description":"Encouraging website with links to information and conferences, returnships and mentoring",
				"url":"https://www.womenintech.co.uk/",
				"views":0},

				{"title":"Women Who Code",
				"description":"Global not for profit aimed at encouraging women in Tech careers",
				"url": "https://www.womenwhocode.com/",
				"views":1}]

#cats is a dictionary list of tools, each  contain dictionary of pages 
		cats = {
					"Book Link": {"pages": book_pages, 'views':77, 'likes':9}, 
					"Web Learning Link": {"pages": web_pages,'views':104, 'likes':25 }, 
					"Video Tutorial Link": {"pages": course_pages,'views':21, 'likes':14},
					"Women Specific Web Link":{"pages": women_pages, 'views':0, 'likes':0},
					"Meet Up Group":{"pages": meetup_pages, 'views':0, 'likes':0}
					}
      
#loop through cats dictionary add each category then add all the associated pages for that category

		for cat, cat_data in cats.items():
			c = add_cat(cat, cat_data ["views"], cat_data ["likes"] )
			for p in cat_data["pages"]:
				add_page(c, p["title"], p["description"], p["url"],p["views"])

 # Print out the categories added.
		for c in Category.objects.all():
			for p in Page.objects.filter(category=c):#filters page by category
				print("- {0} - {1}".format(str(c), str(p)) )#uses string method to print category name and page title as defined in model

def add_page(cat, title, description, url, views=0):
	p = Page.objects.get_or_create(category=cat, title=title, description=description)[0]
	p.description=description
	p.url=url
	p.views=views
	p.save()
	return p

def add_cat(name,  views=0,likes=0):#title
	c = Category.objects.get_or_create(name=name)[0]
#	c.page=Page.objects.get_or_create(title =title)
#	c.title=title
	c.views=views
	c.likes=likes
	c.save()
	return c

 # Start execution here!
if __name__ == '__main__': #keeps this  Python script as standalone, cannot be imported to other modules
	print("Starting cupcake_site population script...")
	populate()