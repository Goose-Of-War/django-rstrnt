# django-rstrnt
 A restaurant project made using django

##
Honk once again. I know, it's been a while since I worked on a proper project (I mean, I _was_ working on the MASK website, but it's not on my own profile, so you can go visit it if you want by clicking [here]("https://github.com/mask-tech/MASK").) This one is another project done in an effort to learn something new.

##
### What's new?
Glad you asked (I mean, it's a monologue, but still, go with it.) After working for months with nodeJS, express, nunjucks, mongoDB, I am learning... Python? Yes. This project is a Django project in Python. Django (from what I gather) is a framework. Essentially, all I do is the same as what I did with node, express, nunjucks, etc., but all of them are already in one place rather than me installing everything all as per their requirements. I guess it is worth defecting back to Python (_sigh_ I was just getting the hang of JS.)

##
### Why `py` when you're already doing `js`?
To answer the question, it's pretty simple. This one is more of a project to learn the basics of django and things related to it, before we start working on the website of the hall. 

##
### What's done till now?
Well, the exercise required me to do the following:
- Implement CRUD elements (using Django and SQL)
- Use static web pages (using HTML and CSS)
- Be creative

And what have I done?
- CRU... hey? Where's the D?
- Welp, static web pages, but using templates (I mean... that's kinda why we even have it lol. DRY FTW.)
- Creativity... Nope, doesn't ring a bell. (At least I got some styling in my stuff)

(I'm doomed, aren't I?)

##
### Running the app:
- Clone the repository (preferably in a `venv`)
- Make sure django is present (if you're in a `venv`, all the more reason, since pip scripts need to be reinstalled)
- Type the following in the Terminal: `py manage.py runserver` (Note: Depending on your OS and other parameters, `py` should be replaced with the appropriate equivalent)
- The app can be found in the link [localhost:8000/rstrnt](localhost:8000/rstrnt)

### Model used:
```py 
class FoodItem(models.Model):
	name = models.CharField(max_length=40, primary_key=True)
	price = models.IntegerField()
	img = models.CharField(max_length=200, null=True)
```

##
> _I will be working on this repository only for a few days. So excuse me if it feels a bit sloppy ;-;_

Until later

Honk
##
_This repository is being updated. Details will be added along with time._
