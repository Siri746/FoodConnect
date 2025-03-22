# Food Delivery App
A Django-based web app to connect customers, delivery boys, and sellers for food sharing and selling.

## Setup
1. Clone the repo: `git clone <repo-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py makemigrations && python manage.py migrate`
4. Create superuser: `python manage.py createsuperuser`
5. Start server: `python manage.py runserver`

## Features
- Role-based sign-up (customer, delivery boy, seller).
- Customers can share food.
- Delivery boys can accept food delivery requests.
- Sellers can list items for sale.
