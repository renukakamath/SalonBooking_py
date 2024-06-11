from flask import *
from database import *

admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
	return render_template('admin_home.html')

@admin.route('/admin_manage_category',methods=['get','post'])
def admin_manage_category():
	if 'submit' in request.form:
		name=request.form['cname']
		description=request.form['description']
		
		p="insert into category values(null,'%s','%s','1')"%(name,description)
		res=insert(p)
	return render_template('admin_manage_category.html')

@admin.route('/admin_view_salon',methods=['get','post'])
def admin_view_salon():
		p="select * from salon"
		res=select(p)
		return render_template('admin_view_salon.html',res=res)

@admin.route('/admin_view_services',methods=['get','post'])
def admin_view_services():
		p="select s.service_name, st.s_fname, st.s_lname, sn.salon_name, s.price from service s join staff st on s.staff_id = st.staff_id join salon sn on st.salon_id = sn.salon_id"
		res=select(p)
		return render_template('admin_view_services.html',res=res)

@admin.route('/admin_view_booking',methods=['get','post'])
def admin_view_booking():
		p="select * from service inner join booking_child using(service_id) inner join booking_master using(bm_id) inner join customer using(customer_id)"
		res=select(p)
		return render_template('admin_view_booking.html',res=res)

@admin.route('/admin_view_complaints',methods=['get','post'])
def admin_view_complaints():
		p="select cus.c_fname, cus.c_lname, sal.salon_name, com.complaint, com.date from complaints com join customer cus ON com.customer_id = cus.customer_id join salon sal on com.salon_id = sal.salon_id"
		res=select(p)
		return render_template('admin_view_complaints.html',res=res)

@admin.route('/admin_add_reply',methods=['get','post'])
def admin_add_reply():
		if 'submit' in request.form:
			reply=request.form['reply']
		
			p="insert into complaints values(null,'%s')"%(reply)
			res=select(p)
		return render_template('admin_add_reply.html',res=res)

@admin.route('/admin_view_payment',methods=['get','post'])
def admin_view_payment():
		sid=session['salon_id']
		p="select * from payment inner join card using(card_id) inner join booking_master using(bm_id) inner join customer on customer.customer_id=booking_master.customer_id where salon_id='%s'"%(sid)
		res=select(p)
		return render_template('admin_view_payment.html',res=res)







