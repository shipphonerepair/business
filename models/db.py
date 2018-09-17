#import csv
#import os
db = DAL("sqlite://storage.sqlite")


phone_models = ['iPhone 4', 'iPhone 4S', 'iPhone 5', 'iPhone 5C', 'iPhone 5S', 'iPhone 6', 'iPhone 6 Plus', 'iPhone 6S', 'iPhone 6S Plus', 'iPhone SE', 'iPhone 7', 'iPhone 7 Plus', 'iPhone 8', 'iPhone 8 Plus']
phone_screen_colors = ['Black', 'White']
spare_phone_options = ['Yes', 'No']
#dates = []
#with open(os.path.join(request.folder, 'static', 'files', 'dates.csv')) as csvfile:
#    reader = csv.reader(csvfile)
#    for row in reader:
#        for item in row:
#            dates.append(item)
db.define_table('post',
    Field('first_name'),
    Field('last_name'),
    Field('email'),
    Field('phone_number'),
    Field('phone_model'),
    Field('phone_screen_color'),
    Field('spare_phone'),
    Field('price'),
    #Field('date'),
    Field('notes', 'text'))

db.post.first_name.requires = IS_NOT_EMPTY(error_message="Enter first name")
db.post.last_name.requires = IS_NOT_EMPTY(error_message="Enter last name")
db.post.email.requires = IS_EMAIL(error_message="Invalid email")
db.post.phone_number.requires = IS_MATCH('^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$', error_message="Invalid Number")
db.post.phone_model.requires = IS_IN_SET(phone_models, zero='Select Model', error_message="Select model")
db.post.spare_phone.requires = IS_IN_SET(spare_phone_options, zero='Select Option', error_message="Select option")
db.post.phone_screen_color.requires = IS_IN_SET(phone_screen_colors, zero='Select Color', error_message="Select screen color")
#db.post.date.requires = IS_IN_SET(dates, zero='Select Date', error_message="Select Date")

db.define_table('postBattery',
    Field('first_name'),
    Field('last_name'),
    Field('email'),
    Field('phone_number'),
    Field('phone_model'),
    Field('spare_phone'),
    Field('price'),
    Field('notes', 'text'))

db.postBattery.first_name.requires = IS_NOT_EMPTY(error_message="Enter first name")
db.postBattery.last_name.requires = IS_NOT_EMPTY(error_message="Enter last name")
db.postBattery.email.requires = IS_EMAIL(error_message="Invalid email")
db.postBattery.phone_number.requires = IS_MATCH('^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$', error_message="Invalid Number")
db.postBattery.phone_model.requires = IS_IN_SET(phone_models, zero='Select Model', error_message="Select model")
db.postBattery.spare_phone.requires = IS_IN_SET(spare_phone_options, zero='Select Option', error_message="Select option")

db.define_table('postOther',
    Field('first_name'),
    Field('last_name'),
    Field('email'),
    Field('phone_number'),
    Field('phone_model'),
    Field('request', 'text'))

db.postOther.first_name.requires = IS_NOT_EMPTY(error_message="Enter first name")
db.postOther.last_name.requires = IS_NOT_EMPTY(error_message="Enter last name")
db.postOther.email.requires = IS_EMAIL(error_message="Invalid email")
db.postOther.phone_number.requires = IS_MATCH('^(?:(?:\+?1\s*(?:[.-]\s*)?)?(?:\(\s*([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9])\s*\)|([2-9]1[02-9]|[2-9][02-8]1|[2-9][02-8][02-9]))\s*(?:[.-]\s*)?)?([2-9]1[02-9]|[2-9][02-9]1|[2-9][02-9]{2})\s*(?:[.-]\s*)?([0-9]{4})(?:\s*(?:#|x\.?|ext\.?|extension)\s*(\d+))?$', error_message="Invalid Number")
db.postOther.phone_model.requires = IS_IN_SET(phone_models, zero='Select Option', error_message="Select model")
db.postOther.request.requires = IS_NOT_EMPTY(error_message="Enter a repair request")

db.define_table('comment',
                Field('comment', 'text'))

db.comment.comment.requires = IS_NOT_EMPTY(error_message="No comment entered")
