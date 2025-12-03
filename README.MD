### Media HUB

Media sharing platform that has role based access

- Teacher role - manage assigned student content, media uploads
- Student role - share media uploads
- Admin role - overseeing all content and managing the platform

### Tools ofuse

- Django
- Python libraries (ready made snippets for a specific job)
  - Pillow : media transactions in python frameworks (absolute media url)
  - Claudinary : media storage and also url access generation (url -> save to database for an upload)
  - Python-decouple : media tasks

### Apps in projects

- Accounts : authentication and authorization (signups, login, forgot password)
- Media_assets : uploads tasks, displays, updates

### Steps

- Install the libraries :
  pip install libraryname
  pip install -r requirements.txt
- Create our apps
- Configure our project settings
  - register our apps
  - register cloudinary
  - register a custom authentication process
  - emails registry

### Authentication and Authorization (accounts app)

Authentication = identify identification, who are you?
Authorization = access privileges - role based authorization, token based authorization

1. Create our custom user model - models.py
2. Extend the integrate form captures - forms.py
3. Create the views action for registration and login, logout and profile view,
   custompasswordresetview, custompasswordresetconfirmview - views.py
4. Register the views actions as URL route - urls.py
5. Register the models for admin to use and manage content on -admin.py
6. Register the apps url to the projects urls - project/urls.py
7. Create the templates
   - create a templates folder - within the app
   - create a global templates folder - register it's configuration in the settings.py file
8. Make databases migrations and then populate the templates
   python manage.py makemigrations
   python manage.py migrate

### Template creation

1. Configuration level file : base.html

   - Defining your blocks : title, extra_css, content (most important),footer, extra_js
   - Linking to global stylesheet / style lib. (bootstrap)
   - Link to global js files

2. Create the other pages by simply extending(extends) the configs done on 1.
   Populate what is dynamic using block - the content is changing.
