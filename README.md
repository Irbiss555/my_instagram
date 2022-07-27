# my_instagram
## How to run the project
1. Install Python and project dependencies

Download and install Python 3.8 from official site https://www.python.org/

Create and activate virtual environment
``` 
python3.8 -m venv env

source env/bin/activate
```
    
Install packages from requirements.txt
    
```
pip install -r requirements.txt
```

2. Apply migrations
```
python manage.py migrate
```
3. Load fixtures for users

```
python manage.py loaddata instagram/fixtures/auth.json 
```
4. Load fixtures for other data
    
```
python manage.py loaddata instagram/fixtures/dump.json
```
5. Extract archive with images
```
unzip uploads.zip
```
6. Run the project
```
python manage.py runserver
```
