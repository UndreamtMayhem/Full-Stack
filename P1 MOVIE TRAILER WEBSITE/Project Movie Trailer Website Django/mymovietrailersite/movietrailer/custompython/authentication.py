class MyBackend(object):
    # these should be post['usernam'] and post['password']
    def authenticate(self, username=None, password=None):
        # Check the username/password and return a user.


        login_valid = (settings.ADMIN_LOGIN == username)
        pwd_valid = check_password(password, settings.ADMIN_PASSWORD)
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
                #create a session??
            except User.DoesNotExist:
           
            return user
        
if request.user.is_authenticated:
    # Do something for authenticated users.
    
else:
    # Do something for anonymous users.
    