from gluon.contrib.user_agent_parser import mobilize
import smtplib

@mobilize
def screen():
    form = SQLFORM(db.post, record=None)
    if form.process().accepted:
        redirect(URL('received'))
    return dict(form=form)

@mobilize
def received():
    fromaddr = 'shipphonerepair@gmail.com'
    toaddrs  = 'shipphonerepair@gmail.com'
    msg = "\r\n".join([
      "Name: shipphonerepair@gmail.com",
      "To: shipphonrepair@gmail.com",
      "Subject: " + db().select(db.post.first_name).last().first_name + " " + db().select(db.post.last_name).last().last_name + " - " + db().select(db.post.phone_model).last().phone_model + " Screen",
      "",
      "Ship Phone Repair Receipt:\n\n" +
            "\tName: " + db().select(db.post.first_name).last().first_name + " " + db().select(db.post.last_name).last().last_name + "\n" +
            "\tNumber: " + db().select(db.post.phone_number).last().phone_number + "\n" +
            "\tEmail: " + db().select(db.post.email).last().email + "\n" +
            "\tModel: " + db().select(db.post.phone_model).last().phone_model + "\n" +
            "\tScreen Color: " + db().select(db.post.phone_screen_color).last().phone_screen_color + "\n" +
            "\tSpare Phone: " + db().select(db.post.spare_phone).last().spare_phone + "\n" +
            "\tPrice: " + db().select(db.post.price).last().price + "\n" +
            "\tNotes: "  + db().select(db.post.notes).last().notes
      ])
    username = 'shipphonerepair@gmail.com'
    password = 'Shipphonerepair1'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    return dict(received=(db().select(db.post.first_name).last().first_name,
                          db().select(db.post.last_name).last().last_name,
                          db().select(db.post.phone_number).last().phone_number,
                          db().select(db.post.email).last().email,
                          db().select(db.post.phone_model).last().phone_model,
                          db().select(db.post.phone_screen_color).last().phone_screen_color,
                          db().select(db.post.spare_phone).last().spare_phone,
                          db().select(db.post.price).last().price))
@mobilize
def battery():
    form = SQLFORM(db.postBattery, record=None)
    if form.process().accepted:
        redirect(URL('receivedBattery'))
    return dict(form=form)

@mobilize
def receivedBattery():
    fromaddr = 'shipphonerepair@gmail.com'
    toaddrs  = ['shipphonerepair@gmail.com', db().select(db.post.email).last().email]
    msg = "\r\n".join([
      "Name: shipphonerepair@gmail.com",
      "To: shipphonrepair@gmail.com",
      "Subject: " + db().select(db.postBattery.first_name).last().first_name + " " + db().select(db.postBattery.last_name).last().last_name + " - " + db().select(db.postBattery.phone_model).last().phone_model + " Battery",
      "",
      "Ship Phone Repair Receipt:\n\n" +
            "\tName: " + db().select(db.postBattery.first_name).last().first_name + " " + db().select(db.postBattery.last_name).last().last_name + "\n" +
            "\tNumber: " + db().select(db.postBattery.phone_number).last().phone_number + "\n" +
            "\tEmail: " + db().select(db.postBattery.email).last().email + "\n" +
            "\tModel: " + db().select(db.postBattery.phone_model).last().phone_model + "\n" +
            "\tSpare Phone: " + db().select(db.postBattery.spare_phone).last().spare_phone + "\n" +
            "\tPrice: " + db().select(db.postBattery.price).last().price + "\n" +
            "\tNotes: "  + db().select(db.postBattery.notes).last().notes
      ])
    username = 'shipphonerepair@gmail.com'
    password = 'Shipphonerepair1'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    return dict(received=(db().select(db.postBattery.first_name).last().first_name,
                          db().select(db.postBattery.last_name).last().last_name,
                          db().select(db.postBattery.phone_number).last().phone_number,
                          db().select(db.postBattery.email).last().email,
                          db().select(db.postBattery.phone_model).last().phone_model,
                          db().select(db.postBattery.spare_phone).last().spare_phone,
                          db().select(db.postBattery.price).last().price))
@mobilize
def other():
    form = SQLFORM(db.postOther, record=None)
    if form.process().accepted:
        redirect(URL('otherReceived'))
    return dict(form=form)

@mobilize
def otherReceived():
    fromaddr = 'shipphonerepair@gmail.com'
    toaddrs  = ['shipphonerepair@gmail.com', db().select(db.post.email).last().email]
    msg = "\r\n".join([
      "Name: shipphonerepair@gmail.com",
      "To: shipphonrepair@gmail.com",
      "Subject: " + db().select(db.postOther.first_name).last().first_name + " " + db().select(db.postOther.last_name).last().last_name + " - " + db().select(db.postOther.phone_model).last().phone_model + " Repair Request",
      "",
      "Ship Phone Repair Receipt:\n\n" +
            "\tName: " + db().select(db.postOther.first_name).last().first_name + " " + db().select(db.postOther.last_name).last().last_name + "\n" +
            "\tNumber: " + db().select(db.postOther.phone_number).last().phone_number + "\n" +
            "\tEmail: " + db().select(db.postOther.email).last().email + "\n" +
            "\tModel: " + db().select(db.postOther.phone_model).last().phone_model + "\n" +
            "\tRequest: " + db().select(db.postOther.request).last().request + "\n"
      ])
    username = 'shipphonerepair@gmail.com'
    password = 'Shipphonerepair1'
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    return dict(received=(db().select(db.postOther.first_name).last().first_name,
                          db().select(db.postOther.last_name).last().last_name,
                          db().select(db.postOther.phone_number).last().phone_number,
                          db().select(db.postOther.email).last().email,
                          db().select(db.postOther.phone_model).last().phone_model,
                          db().select(db.postOther.request).last().request))

@mobilize
def contact():
    form = SQLFORM(db.comment, record=None, formstyle='table2cols')
    if form.process().accepted:
        response.flash = 'Thank you for your feedback!'
    return dict(form=form)

@mobilize
def index():
    return dict()

@mobilize
def prices():
    return dict()
