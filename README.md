<h1 align="center">This is all Becuase of `Shins` !</h1>


i try to make a stateless web or REST API! in which i use JSON-WEBTOKEN(Jwt) authentication via ```simple-jwt``` Pip package!


user after Successfully registraion and login can perform CRUD operations!<div align="center"><img align="center"> 
![Hnet-image](https://user-images.githubusercontent.com/47344024/132098227-bb526966-1300-4d4f-90e2-321ad3e4df92.gif) 
</img> 
</div>
for documenting Api i have used `Swagger-ui` and `redoc` also!

### Set this project locally :computer:

1. Fork this Repository (or Download the Zip file directly and start from the step 3).

2. Open terminal / command prompt and Clone the project using 
    ```bash
    git clone https://github.com/ritiksoni00/Techdome_task.git
    ```
  
3. Create a python3 virtual environment:

    ```bash
    $ python3 -m venv venv
    ```

    Or, use [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html):

    ```bash
    $ virtualenv venv
    ```

4. Activate the virtual environment:

    On Linux or Mac or any Unix based system-
    
    ```bash
    $ source venv/bin/activate
    ```
    
    On Windows-
    ```
    > venv\Scripts\activate
    ```

5. Now Install the dependecies:

    ```bash
    $ pip install -r requirements.txt
    ```


    
6. Creating `.env` file:
Create a `.env` file in the same directory where your `manage.py` resides.

    Copy this text in your `.env` file -
    ```
    SECRET_KEY = 'secretkey'
    ```

7. Run the `migrate` command:

    ```bash
    $ python manage.py migrate
    ```

8. Now you are ready to go:

    #### Run the application

    ```bash
    $ python manage.py runserver
    ```
thanks to Guarav bhai!
