from flask import *
from database import *

staff=Blueprint('staff',__name__)

@staff.route('/staff_home')
def staff_home():
	return render_template('staff_home.html')

@staff.route('/staff_manage_service',methods=['get','post'])
def staff_manage_service():
	data={}
	q="select * from category"
	data['cat']=select(q)
	if 'submit' in request.form:
		name=request.form['sname']
		price=request.form['price']
		p="insert into service values(null,'%s','%s','active')"%(name,price)
		res=select(p)
	return render_template('staff_manage_service.html',data=data)

@staff.route('/staff_view_booking',methods=['get','post'])
def staff_view_booking():
		sid=session['salon_id']
		p="select * from service inner join booking_child using(service_id) inner join booking_master using(bm_id) inner join customer using(customer_id)  where salon_id='%s'"%(sid)
		res=select(p)
		return render_template('staff_view_booking.html',res=res)

@staff.route('/staff_view_customer',methods=['get','post'])
def staff_view_customer():
		sid=session['salon_id']
		p="select * from customer inner join booking_master using(customer_id) where salon_id='%ss33'"%(sid)
		res=select(p)
		return render_template('staff_view_customer.html',res=res)

@staff.route('/staff_view_payment',methods=['get','post'])
def staff_view_payment():
		sid=session['salon_id']
		p="select * from payment inner join card using(card_id) inner join booking_master using(bm_id) inner join customer on customer.customer_id=booking_master.customer_id where salon_id='%s'"%(sid)
		res=select(p)
		return render_template('staff_view_payment.html',res=res)

