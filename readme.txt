    *** PLease .env file save in main project directory otherwise
         cloudinary and Stripe will not be working.
         There was secreat key on this .env file ***

         #Note : .env file attached on your mail. PLease check it.


* Install dependencies using this command
    pip install -r requirements.txt

* Apply migrations using this command
    python manage.py makemigrations
    python manage.py migrate

* Create superuser
    python manage.py createsuperuser
    # Allready have a supersuser :
            email: admin@gmail.com
            password: admin

* Run server
    python manage.py runserver


----------Running the Project---------

    The server will run on http://127.0.0.1:8000/

    Visit: http://127.0.0.1:8000/admin to access the admin panel.

    API base url: /api/
--------------------------------------
API Endpoints
--------------
Endpoint	            Method	               Description	                   Auth Required
/api/products/	        GET	                List all products (paginated)	        No
/api/profile/	        GET	                Get logged in user profile	            Yes
/api/token/	            POST	            Get JWT access & refresh tokens	        No
/api/token/refresh/	    POST	            Refresh JWT access token	            No
/api/checkout-session/	POST	    Create Stripe checkout session	                Yes

----------------------------------------------------------------------------------------------------------
* For Access Token
    Use postman to send Post request : : "http://127.0.0.1:8000/api/token/"
Method : POST
Body: JSON

{
  "email": "admin@gmail.com",
  "password": "admin"
}

you will get a refresh and access token.

------------------------------------------------
* For Cetegory
Use postman to send Post request : "http://127.0.0.1:8000/api/products/"
and also add in Postman Header section key: "category" and Value: "Bag"


* For profile
Use postman to send Post request : "http://127.0.0.1:8000/api/profile/"
and also add in Postman Header section key: "Authorization" and Value: "Bearer <Access key>"


*Testing Stripe Payments

Use Postman to send a POST request to: "http://127.0.0.1:8000/api/checkout-session/" with JSON body:
and also add in Postman Header section key: "Authorization" and Value: "Bearer <Access key>"

{
  "product_id": 1
}

    The response will contain a full url with sessionId.

    Copy this link and past any browser url section then it will be go to payment option.

    Use Stripe test cards (4242 4242 4242 4242) to complete payment.

    Success and cancel URLs redirect.