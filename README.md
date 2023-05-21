# how to start this app

## 1. install dependencies
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## 2. setup database
```
python3 manage.py makemigrations
```

## 3. run server
```
python3 manage.py runserver
```