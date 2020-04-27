# me_llamo_django
**Me llamo django** is an original project aimed at increasing the effectiveness of Spanish language learning. The project contains a set of Polish-Spanish memocards which are generated daily for each user in the number specified by them. The implemented method of Leitner's repetition makes that the memocard with the learned words are sent to the user again after some time depending on the level of memory of a given word

### Inicialization
**Me llamo django** uses Python programming language, its Django framework and RDBMS PostgreSQL. To run the project locally:
 
**1.** Install [Python](https://www.python.org/downloads/)

**2.** Install [PIP](https://bootstrap.pypa.io/get-pip.py)

**3.** Install [PostgreSQL](https://www.postgresql.org/download/)

**4.** Me llamo django is integrated into the me_llamo_django PostgreSQL database with user me_llamo_django with the password me_llamo_django. Create this database and user. For example, by typing the following commands in SQL Shell

```
 CREATE DATABASE me_llamo_django;
 CREATE USER me_llamo_django WITH ENCRYPTED PASSWORD 'me_llamo_django';
 GRANT ALL PRIVILEGES ON DATABASE me_llamo_django TO me_llamo_django;
 
```

**5.** Clone this repository: 
```
git clone https://github.com/KazimierzMigdal/me_llamo_django.git
```

**6.** Create virtual environment

**7.** Create virtual environment, activate it and install install packages from the requirements.txt:
```
pip install -r requirements.txt
```

**8.** Go to me_llamo_django directory and update the databases by typing into CMD/Command prompt 
```
python manage.py migrate
```
**9.** The repository contains the necessary memocards. Upload them to a previously created table in the database by typing into CMD/Command prompt 
```
python manage.py loaddata memocard.json
```
**10.** Run server by typing into CMD/Command prompt:
```
python manage.py runserver
```
The **Me llamo django** is available at the address http://127.0.0.1:8000

**11.** You can create administrator by typing into CMD/Command prompt:
```
python manage.py createsuperuser
```
