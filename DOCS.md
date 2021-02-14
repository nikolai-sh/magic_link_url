##Test assignment

Problem: 
We want to create an authentication solution that doesn’t require our users to input an email/password.  We want to be able to generate a magic link that works for a specific user’s email until we remove access.

Example:
We want to allow test@email.com have access to the site.  So we generate a magic link to test@email.com and an email gets sent to them with the magic link url.  Every time we hit the url with the magic link token, the counter for that user should increase by 1 (So we know how many times they checked out the link).

Important:
The route that requires the magic link token should not be accessible without the magic link.
We are not going to force any technology for this exercise, but we require that the solution is built in-house (no use of external magic link generators like auth0)
The project should be pushed to github or another repository of your choice.

Bonus points if:
You create a simple view where we can see the counts (visits) going up.
Use one of python web frameworks of your choice (Flask, Django, FastAPI, ...) for the backend.
Deploy the app in Heroku (Free account).

##Solution explanation 

I used the Django framework for this task. 

* Created a modified User with fields email, password, visits. For this I used the AbstractUser django class. Since was modified User, it is necessary to create the modified UserManager using the BaseUserManager class. 

* To register users, a UserRegisterForm was created based on UserCreationForm. 

* To send the magic link url, the send_magic_link function accepts email from EmailForm and checks it and determines the corresponding user object, also takes scheme, host variables from the request and passes it to get_magic_link(user, scheme, host) a function that generates a magic link url and sends it to the user.

* The get_magic_link function from the user object takes the user_id and encodes it, then generates a token using default_token_generator.make_token() from the PasswordResetTokenGenerator class. At the end, collects the scheme, host, user_id, token into the magic link url string. 

* When the user clicks on the received magic link url, the login_with_magic_link function from the url takes the values uidb64=user_id and token=token. uidb64 decodes and uses it to find the user. Token and user are checked using the default_token_generator.check_token() method of the PasswordResetTokenGenerator class, if return true:
user finish login with login() function from django.contrib.auth module and increase user visits value by 1.