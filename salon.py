from flask import *
from database import *
import uuid

salon=Blueprint('salon',__name__)

@salon.route('/salon_home')
def salon_home():
	return render_template('salon_home.html')

@salon.route('/salon_manage_staff',methods=['get','post'])
def salon_manage_staff():
	sid=session['salon_id']
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		join=request.form['jdate']
		dob=request.form['ddate']
		gender=request.form['gender']
		house=request.form['house']
		city=request.form['city']
		district=request.form['district']
		pin=request.form['pin']
		phone=request.form['phone']
		username=request.form['uname']
		password=request.form['passwrd']

		p="insert into login values(null,'%s','%s','staff')"%(username,password)
		res1=insert(p)
		q="insert into staff values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','active')"%(res1,sid,fname,lname,join,dob,gender,house,city,district,pin,phone)
		res=insert(q)

		print(q)
	return render_template('salon_manage_staff.html')

@salon.route('/salon_view_booking',methods=['get','post'])
def salon_view_booking():
		sid=session['salon_id']
		p="select * from service inner join booking_child using(service_id) inner join booking_master using(bm_id) inner join customer using(customer_id)  where salon_id='%s'"%(sid)
		res=select(p)
		return render_template('salon_view_booking.html',res=res)

@salon.route('/salon_view_payment',methods=['get','post'])
def salon_view_payment():
		sid=session['salon_id']
		p="select * from payment inner join card using(card_id) inner join booking_master using(bm_id) inner join customer on customer.customer_id=booking_master.customer_id where salon_id='%s'"%(sid)
		res=select(p)
		return render_template('salon_view_payment.html',res=res)

@salon.route('/salon_view_feedback',methods=['get','post'])
def salon_view_feedback():
		sid=session['salon_id']
		p="select * from feedback inner join customer using(customer_id) where salon_id='%s'"%(sid)
		res=select(p)
		return render_template('salon_view_feedback.html',res=res)

@salon.route('/salon_view_rating',methods=['get','post'])
def salon_view_rating():
		sid=session['salon_id']
		p="select * from rating inner join customer using(customer_id )where salon_id='%s'"%(sid)
		res=select(p)
		return render_template('salon_view_rating.html',res=res)

@salon.route('/salon_add_design',methods=['get','post'])
def salon_add_design():
	if 'submit' in request.form:
		title=request.form['title']
		image=request.files['image']
		path="static/image/"+str(uuid.uuid4())+image.filename
		image.save(path)
		
		p="insert into design values(null,'%s','%s')"%(title,path)
		res=insert(p)
	return render_template('salon_add_design.html')

