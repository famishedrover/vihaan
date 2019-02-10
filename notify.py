from pyfcm import FCMNotification
import pickle 


APIKEY = "AAAAj9v2Qjo:APA91bHtrwf9MQgQCzmP3J6XqRdK2-Ut4xXA9gtOfuS9wDhlzyutm0Now1LhICV3WSZJ967-OpwreTt_Z2dk4goV7oT_OtXBcjV52SiVYZvza4bTy6LB2MGMi9xZpjUr7vDS2WvaCUoM"
push_service = FCMNotification(api_key=APIKEY)
ARUSHI = 'e4z0KYgVG_0:APA91bFCJsB6kWL3BzFYgm-yf6C0xPPmuwF6__yPEavMRa8cllM4V1E6maOsvKe0DcdUrXhxOWPmpResnWUZzTCAhDUAXIzsqMPsfBnLsQwLVD1Y3wJaHfUqmd4oay7pakEtYYyG4ITv'
MUDIT = 'c7NNwyZx2iY:APA91bHLopMikJhBQB_BA3j9YxdfW4LoNFIWD95kiPnu5XFrV_2jlgk40p4MUOERDmpCK3fZ3ICElQqH2EqEhMePS9rmg9-XFA-nU99POrrjm57KDBamFOwW1PVJSZbrHa1mcndLlWjA'
NIDHI = ''
TUBA = ''


def getUpdatedRecipient():
	with open('savedDevices.pickle', 'rb') as handle:
	    registration_ids = pickle.load(handle)
	    # print registration_ids
	    return registration_ids

def sendNotification(title,body,recipient):
	message_title = title
	message_body = body

	# print recipient
	print recipient

	# result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)
	result = push_service.notify_multiple_devices(registration_ids=recipient, message_title=message_title, message_body=message_body)

	print 'done'




# call update beforehand always! 
def notifyrecs(recs,eta,person='police'):
	if person is 'police' :
		TITLE = '!!AMBULANCE ALERT!! <- POLICE'
		MSG = 'Approaching in '+str(eta)+' ,Clear Way!'
	elif person is 'volun' :
		TITLE = '!!AMBULANCE ALERT!! <- VOLUN'
		MSG = 'Approaching in '+str(eta)+' ,Help Out!'
	else : 
		TITLE = '!!AMBULANCE ALERT!! <- ENROUTE'
		MSG = 'Approaching in '+str(eta)+' ,Clear Way!'

	sendreq(TITLE, MSG, recs) 


def findNearbyDevicesForEnRoutes(p,d):
	r = getUpdatedRecipient()
	return r['mudit']

def findNearbyDevicesForVoluns(p,d):
	r = getUpdatedRecipient()
	return r['nidhi']

def findNearbyDevicesForPolice(p,d):
	r = getUpdatedRecipient()
	return r['arushi']


from grello import nearbykms
def findNearbyDevicesForEnRoutes__(p,d):
	allrecs = getUpdatedRecipient()
	# for range upto 300m it finds points b/w those.
	nearbykms_(300,p,d,allrecs)

	r = getUpdatedRecipient()
	return r['mudit']


import random
if __name__ == '__main__' :
	registration_ids = getUpdatedRecipient()
	# print registration_ids
	# sendreq = registration_ids['arushi']

	# sendreq = []
	# for k,v in registration_ids.iteritems() :
	# 	print v
	# 	sendreq.append(v)

	sendNotification('Mudit','https://maps.app.goo.gl/9cxAP6I58VxhxcFe2',[MUDIT])











	#last line