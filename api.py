from flask import *
from database import *
import uuid

api=Blueprint('api',__name__)

@api.route('/login',methods=['get','post'])
def login():
	data={}
	username=request.args['username']
	password=request.args['password']
	q ="select * from login where username='%s' and password='%s'" % (username,password)
	res=select(q)
	if len(res)>0:
		data['status'] = 'success'
		data['data']=res
	else:
		data['status'] = 'failed'
	return str(data)
@api.route('/registration',methods=['get','post'])
def registration():
	data={}
	firstname=request.args['firstname']
	lastname=request.args['lastname']
	gender=request.args['gen']
	hname=request.args['housename']
	city=request.args['place']
	pincode=request.args['pin']
	email=request.args['email']
	contact=request.args['phonenumber']
	username=request.args['uname']
	password=request.args['pass']
	q="select * from  login where username='%s'"%(username)
	res=select(q)
	if res:
		data['status']='failed'

	else:
		q = "insert into login(username,password,usertype)values('%s','%s','user')" % (username,password)
		login_id = insert(q)
		q = "insert into customer values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (login_id,firstname,lastname,gender,hname,city,contact,email,pincode)
		id=insert(q)
		if id>0:
			data['status'] = 'success'
		else:
			data['status'] = 'failed'
	return str(data)

@api.route('/view_ornament')
def view_ornament():
	data={}
	sid=request.args['sid']
	q = "select * from design  where salon_id='%s'"%(sid)
	res = select(q)
	if res:
		data['status'] = 'success'
		data['data']=res
	else:
		data['status'] = 'failed'
	return str(data)



@api.route('/feedback',methods=['get','post'])
def feedback():
	data={}
	feedbacks=request.args['feedbacks']
	log_id=request.args['log_id']
	q = "insert into feedback values(null,(SELECT `customer_id` FROM `customer` WHERE `login_id`='%s'),'%s',curdate())" % (log_id,feedbacks)
	id = insert(q)
	if id>0:
		data['status'] = 'success'
	else:
		data['status'] = 'failed'
	return str(data)
@api.route('/view_categories',methods=['get','post'])
def view_categories():
	data={}

	cid=request.args['cid']
	q = "select * from category  where salon_id='%s'"%(cid)
	res = select(q)
	if res:
		data['status'] = 'success'
		data['data']=res
	else:
		data['status'] = 'failed'
	return str(data)


@api.route('/spinner',methods=['get','post'])
def spinner():
	data={}
	# catid=request.args['catid']
	q = "select * from salon "
	res = select(q)
	if res:
		data['status'] = 'success'
		data['data']=res
		data['method']="spinner"
	else:
		data['status'] = 'failed'
		data['method']="spinner"
	return str(data)






@api.route('/addcart',methods=['get','post'])
def addcart():
	data={}
	qty=request.args['qua']
	logid=request.args['logid']
	pid=request.args['pid']
	tot=request.args['tot']
	q = "insert into order_table values(null,(SELECT `cust_id` FROM `customers_table` WHERE `log_id`='%s'),'%s','%s','cart','%s')" % (logid,pid,tot,qty)
	id = insert(q)
	q = "insert into orderstatus_table values(null,'%s','Pending')" % (id)
	id = insert(q)
	if id>0:
		data['status'] = 'success'
	else:
		data['status'] = 'failed'
	return str(data)

@api.route('/view_cart',methods=['get','post'])
def view_cart():
	data={}

	q = "select * from booking_child inner join booking_master using(bm_id)  inner join customer using (customer_id) inner join service using (service_id) "
	res = select(q)
	if res:
		data['status'] = 'success'
		data['data']=res
		data['method'] = 'view_cart'
	else:
		data['status'] = 'failed'
		data['method'] = 'view_cart'
	return str(data)


@api.route('/buy',methods=['get','post'])
def buy():
	data={}
	logid=request.args['logid']
	q = "select * from order_table where cust_id=(SELECT `cust_id` FROM `customers_table` WHERE `log_id`='%s') and order_status='cart'" % (logid)
	res = select(q)
	if res:
		for row in res:
			q = "insert into payment_table values(null,'%s','%s','%s','%s','pending')" % (row['cust_id'],row['order_id'],row['pro_id'],row['tot_price'])
			id = insert(q)
		q = "update order_table set order_status='requested' where cust_id=(SELECT `cust_id` FROM `customers_table` WHERE `log_id`='%s') and order_status='cart'" % (logid)
		c = update(q)
		data['status'] = 'success'
		data['method'] = 'buy'
	else:
		data['status'] = 'failed'
		data['method'] = 'buy'
	return str(data)

@api.route('/Viewservice')
def Viewservice():
	data={}
	cid=request.args['cid']
	
	q = "SELECT * FROM service INNER JOIN category USING(category_id)  INNER JOIN staff USING (staff_id) where category_id='%s'"%(cid)
	res = select(q)
	print(q)
	data['data']=res
	data['statussss'] = "success"
	data['method']="Viewservice"
		
	return str(data)


@api.route('/Viewsalon')
def Viewsalon():
	data={}


	
	
	q = "SELECT * FROM salon INNER JOIN rating USING (salon_id)   GROUP BY salon_id   ORDER BY  `out`    "
	res = select(q)
	print(q)
	data['data']=res
	data['status'] = "success"
	data['method']="Viewsalon"
		
	return str(data)




@api.route('/BookCycle')
def BookCycle():
	data={}
	uid=request.args['login_id']
	# pid=request.args['pid']
	# a=request.args['price']
	sid=request.args['sid']
	t=request.args['total']
	qu=request.args['quantity']

	q="select * from booking_master where customer_id=(select customer_id from customer where login_id='%s') and bm_status='pending'"%(uid)
	res=select(q)
	if res:
		omid=res[0]['bm_id']
	else:


		q="insert into booking_master values(null,(select customer_id from customer where login_id='%s'),'0','pending')"%(uid)
		omid=insert(q)

	q="select * from booking_child where service_id='%s' and bm_id='%s'"%(sid,omid)
	res=select(q)
	print(q)

	if res:
			odid=res[0]['bc_id']	

			q="update booking_child set time_slot=time_slot+'%s' , price=price+'%s' where bc_id='%s'"%(qu,t,odid)
			update(q)
			print(q)

	else:
		w="insert into booking_child values(null,'%s','%s','%s',curdate(),'%s')"%(omid,sid,t,qu)
		insert(w)


	q="update booking_master set total_price=total_price+'%s' where bm_id='%s'"%(t,omid)
	update(q)
	data['status']="success"	

		
	return str(data)


@api.route('/uploaddesign',methods=['get','post'])
def uploaddesign():
	data={}
	img=request.files['image']
	path="static/image"+str(uuid.uuid4())+img.filename
	img.save(path)
	bm_id=request.form['bm_id']
	q="insert into userdesign values(null,'%s','%s')"%(bm_id,path)
	insert(q)
	data['status']="success"
	return str(data)


@api.route('/makepayment')
def makepayment():
	data={}
	
	bm_id=request.args['bm_id']
	login_id=request.args['login_id']
	amt=request.args['amt']
	cardnum=request.args['cardnum']
	expdate=request.args['expdate']
	q="insert into card values(null,(select customer_id from customer where login_id='%s'),'%s','%s')"%(login_id,cardnum,expdate)

	id=insert(q)
	q="insert into payment values(null,'%s','%s',curdate(),'%s')"%(bm_id,id,amt)
	insert(q)


	q="update booking_master set bm_status='Paid'  where bm_id='%s'"%bm_id
	update(q)
	data['status']="success"
	return str(data)


@api.route('/cancel')
def cancel():
	bid=request.args['bid']
	q="update booking_master set bm_status ='cancel' where bm_id='%s'"%(bid)
	update(q)
	data['status']="success"
	return str(data)

@api.route('/rate')
def rate():
	data={}
	rate=request.args['rating']
	log_id=request.args['log_id']
	review=request.args['review']
	sid=request.args['sid']


	import torch
	from transformers import BertTokenizer, BertForSequenceClassification

	# Load pre-trained BERT model and tokenizer
	model_name = 'bert-base-uncased'
	tokenizer = BertTokenizer.from_pretrained(model_name)
	model = BertForSequenceClassification.from_pretrained(model_name)

	# Define a function to perform sentiment analysis
	def predict_sentiment(text):
	    # Tokenize the input text
	    inputs = tokenizer(text, padding=True, truncation=True, return_tensors='pt')

	    # Perform inference with the model
	    outputs = model(**inputs)

	    # Get the predicted sentiment (0 for negative, 1 for positive)
	    _, predicted_class = torch.max(outputs.logits, dim=1)

	    return predicted_class.item()

	# Example usage:
	text1 = review
	

	sentiment1 = predict_sentiment(text1)


	if sentiment1 == 1:
	    print("Text 1 is positive.")

	else:
	    print("Text 1 is negative.")

	
	
	q="insert into rating values(null,'%s','%s','%s','%s',now(),'%s')"%(sid,log_id,rate,review,sentiment1)
	insert(q)
	print(q)
	data['status']="success"
	data['method']="rate"
	return str(data)