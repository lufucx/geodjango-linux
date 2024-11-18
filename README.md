# Basic Utilization Guide

## Prerequisites

Before getting started, make sure you have the following installed:

- **Python** 3.8+
- **PostgreSQL** with **PostGIS** enabled
- **GDAL** library

### Linux Dependencies

sudo apt-get install binutils libproj-dev gdal-bin

sudo apt install libgeos++-dev libgeos-3.8.0 libgeos-c1v5 libgeos-dev libgeos-doc

## Linux and Windows, Django, GeoDjango, PostgreSQL/PostGIS and Leaflet

This project is a Django-based web application that leverages GeoDjango to handle geospatial data, integrates Leaflet for map rendering, and utilizes Django Rest Framework for API development. It includes a custom admin interface with `django-ckeditor` for rich text editing.

## Installation

### Step 1: Clone the repository
Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/your-project.git
cd your-project
```

### Step 2: Set up the virtual environment

Create and activate a virtual environment:
```bash
python -m venv venv
```
Activate the virtual environment:

    On Windows:
```bash
venv\Scripts\activate
```
On macOS/Linux:
```bash
    source venv/bin/activate
```
### Step 3: Install dependencies

Install the required dependencies:
```venv
pip install -r requirements.txt
```
### Step 4: Set up the database

Run migrations to set up the database schema:
```venv
python manage.py makemigrations
python manage.py migrate
```
### Step 5: Create a superuser

Create a Django superuser (admin user) to access the Django admin interface:
```venv
python manage.py createsuperuser
```
Step 6: Run the development server

Start the development server:
```venv
python manage.py runserver
```
You can now access the application at http://127.0.0.1:8000/ and the admin panel at http://127.0.0.1:8000/admin/.
Features

    GeoDjango Integration: Provides support for geospatial queries and visualizing maps with Leaflet.
    Admin Interface: Customizable admin interface with django-ckeditor for rich text editing and django-crispy-forms for better form rendering.
    REST API: Uses djangorestframework and djangorestframework-gis to create API endpoints for geospatial data.
    PostGIS Support: Integrates with PostgreSQL/PostGIS for geospatial data storage and queries.
    Leaflet Maps: Maps are rendered using the Leaflet library.

## Development Notes

    GDAL: Ensure GDAL is installed and correctly configured, as it’s required for handling geospatial data.
    Windows: If you're running on Windows, ensure GDAL is properly installed using the wheel provided in the requirements.
    Database: This project uses PostgreSQL/PostGIS. Make sure you have a PostgreSQL instance with PostGIS enabled.

## Troubleshooting

    GDAL Installation: If you encounter issues with GDAL, ensure it is installed correctly. You may need to use pipwin to install it on Windows.

    Example for installing GDAL with pipwin on Windows:
``` venv
pip install pipwin
pipwin install gdal
pip install GDAL whl path
```
Missing Packages: If you receive errors related to missing packages, double-check that your virtual environment is activated and that the dependencies have been installed.

# Leaflet Installation: If the Leaflet module is missing or not found, try reinstalling the dependencies with:
```venv
    pip install django-leaflet
```
    Database Errors: Ensure that PostgreSQL is running and configured with PostGIS enabled. Also, verify that the database settings in settings.py are correct.
