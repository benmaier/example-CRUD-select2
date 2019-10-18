PYTHON=env/bin/python
db=db.sqlite3

initialinsert:
	$(PYTHON) manage.py shell << initial_fill.py

cleanmigrate:
	rm crud/migrations/*.py
	touch crud/migrations/__init__.py

resetdatabase:
	make droptables
	make cleanmigrate
	make prepmigrate
	make migrate
	make initialinsert

droptables:
	rm $(db)
	touch $(db)

prepmigrate:
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py makemigrations crud

migrate:
	$(PYTHON) manage.py migrate

superuser:
	$(PYTHON) manage.py createsuperuser

runserver:
	$(PYTHON) manage.py runserver

