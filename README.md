#Example-CRUD for django\_select2

This is a minimal example to display how to use select2 with generic update/create views.

## Prerequisites

Install dependencies

In the repository folder, do

```bash
python -m venv env
source env/bin/activate
pip install -r requirements.txt 
```

## Run Server

```bash
make runserver
```

## Usage

locate to

* http://localhost:8000/institution/create
* http://localhost:8000/institution/update/1 # This will currently produce the erroneous behavior
* http://localhost:8000/geoname/create
* http://localhost:8000/geoname/update/2 # This will show that the ModelSelect2Widget works on a Model with less entries.


