PYTHON=../env/bin/python

initialinsert:
	$(MYSQL) --defaults-file=$(CNF) -v < $(SQLFILES)/inserts.sql
	$(PYTHON)

geonamemigrate:
	$(MYSQL) --defaults-file=$(HOME)/.inig/mysql/db.cnf -v < $(SQLFILES)/geonamemigration.sql

cleanmigrate:
	rm rkiprojects/migrations/*.py

# before you run this you have to manually drop tables
resetdatabase:
	make cleanmigrate
	make prepmigrate
	make migrate
	make initialinsert
	make geonamemigrate

droptables:
	$(PYTHON) manage.py migrate rkiprojects zero

prepmigrate:
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py makemigrations rkiprojects

migrate:
	$(PYTHON) manage.py migrate

superuser:
	$(PYTHON) manage.py createsuperuser

geomodels:
	$(PYTHON) manage.py inspectdb --database=geonames > geomodels.py

runserver:
	$(PYTHON) manage.py runserver

