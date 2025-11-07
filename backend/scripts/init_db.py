from app import app
from models import db
from flask_security.datastore import SQLAlchemyUserDatastore
from flask_security.utils import hash_password

# run like this from backend folder
# python3 -m scripts.init_db

with app.app_context():
  db.drop_all() # delete all data
  db.create_all() # create fresh tables
  datastore : SQLAlchemyUserDatastore = app.datastore

  admin_role = datastore.find_or_create_role('admin', description = 'super user')
  manager_role = datastore.find_or_create_role('manager', description = 'handles and manges store')
  customer_role = datastore.find_or_create_role('customer', description = 'buys items from store')
  
  if not datastore.find_user(email = 'admin@study'):
    datastore.create_user(
      email = 'admin@study',
      password = hash_password('Admin@123'),
      name = 'admin_01'
    )

  if not datastore.find_user(email = 'manager@study'):
    datastore.create_user(
      email = 'manager@study',
      password = hash_password('manager@123'),
      name = 'manager_01'
    )

  if not datastore.find_user(email = 'customer@study'):
    datastore.create_user(
      email = 'customer@study',
      password = hash_password('customer@123'),
      name = 'customer_01'
    )

  try:
    db.session.commit()
    print('✅ Initial roles created successfully.')
  except:
    db.session.rollback()
    print('❌ Error occurred while creating initial roles.')


  admin01 = datastore.find_user(email = 'admin@study')
  manager01 = datastore.find_user(email = 'manager@study')
  cust = datastore.find_user(email = 'customer@study')

  admin_role = datastore.find_role('admin')
  manager_role = datastore.find_role('manager')
  customer_role = datastore.find_role('customer')

  datastore.add_role_to_user(admin01, admin_role)
  datastore.add_role_to_user(manager01, manager_role)
  datastore.add_role_to_user(cust, customer_role)

  try:
    db.session.commit()
    print('✅ Initial users assigned to roles.')
  except:
    db.session.rollback()
    print('❌ Error occurred while assigning roles to initial users.')