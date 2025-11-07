from app import app
from models import db
from flask_security.datastore import SQLAlchemyUserDatastore

with app.app_context():
  db.drop_all() # delete all data
  db.create_all() # create fresh tables
  datastore : SQLAlchemyUserDatastore = app.datastore

  admin_role = datastore.find_or_create_role('admin', description = 'super user')
  manager_role = datastore.find_or_create_role('manager', description = 'handles and manges store')
  customer_role = datastore.find_or_create_role('customer', description = 'buys items from store')
  
  try:
    db.session.commit()
    print('✅ Initial roles created successfully.')
  except:
    db.session.rollback()
    print('❌ Error occurred while creating initial roles.')