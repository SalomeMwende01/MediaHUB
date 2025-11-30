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

### Authentication and Authorization
Authentication = identify identification, who are you?
Authorization = access privileges - role based authorization, token based authorization

1. Create our custom user model - models.py
2. Extend the integrate form captures - forms.py
3. Create the views action for registration and login - views.py