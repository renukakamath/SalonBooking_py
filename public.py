from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
	
	return render_template('home.html')

@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		username=request.form['username']
		password=request.form['password']
		q="select * from login where username='%s' and password='%s'"%(username,password)
		res=select(q)
		if res:

			session['login_id']=res[0]['login_id']
			if res[0]['usertype']=='admin':
				return redirect(url_for('admin.admin_home'))


			elif res[0]['usertype']=='salon':
				q="select * from salon where login_id='%s'"%(session['login_id'])
				res=select(q)
				session['salon_id']=res[0]['salon_id']
				return redirect(url_for('salon.salon_home'))

			elif res[0]['usertype']=='staff':
				return redirect(url_for('staff.staff_home'))

	return render_template('login.html')

@public.route('/salon_registration',methods=['get','post'])
def salonreg():
	if 'submit' in request.form:
		name=request.form['sname']
		place=request.form['splace']
		phone=request.form['sphone']
		email=request.form['semail']
		address=request.form['saddress']
		username=request.form['susername']
		password=request.form['spassword']

		p="insert into login values(null,'%s','%s','salon')"%(username,password)
		res1=insert(p)
		q="insert into salon values(null,'%s','%s','%s','%s','%s','%s')"%(res1,name,place,phone,email,address)
		res=insert(q)
	return render_template('salon_registration.html')








