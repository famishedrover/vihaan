from flask import Flask, redirect, url_for, request
from flask import jsonify


from notify import getUpdatedRecipient,sendNotification,notifyrecs,findNearbyDevicesForPolice,findNearbyDevicesForVoluns,findNearbyDevicesForEnRoutes

import pickle

import json

app = Flask(__name__)

allRegisteredDevices = {}

import os

def pol():
	# me
	os.system('curl https://notify.run/1Bm0iWQAEAcNBz1v -d "AMBI ALERT 5mins away! -> POLICE"')
def vol():
	# ar
	os.system('curl https://notify.run/JPhPFQkX4YSg5zcu -d "AMBI ALERT 10mins away! -> VOLUN"')
def enrt():
	# tuba
	os.system('curl https://notify.run/c/khBs09bzpOZXSXu0 -d "AMBI ALERT ! -> ENRT"')


# pol()
# vol()
# enrt()



@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name


@app.route('/success2')
def success2():
	return 'donedoneondondondodne'

@app.route('/callambi',methods=['POST','GET'])
def callambi():
	# get its location from the phone 
	# req = json.loads(request.data)
	# currentloc = req['currentlocation']


	# priority = req['priority']


	# use this loc to find nearby hospitals -> gets its position
	# hospital = getHospital(currentloc)
	# eta = getETA(currentloc,hospital)


	# pickup, dropoff = getUberLinks(currentloc,hospital)

	# allPolice = findNearbyDevicesForPolice(pickup,dropoff)
	# allVoluns = findNearbyDevicesForVoluns(pickup,dropoff)
	# allEnroute = findNearbyDevicesForEnRoutes(pickup,dropoff)

	# send
	# notifyrecs(allPolice,eta,'police')
	# notifyrecs(allVoluns,eta,'volun')
	# notifyrecs(allEnroute,eta,'enroute')

	pol()
	vol()
	enrt()






@app.route('/login',methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		print 'Recevied POST ---------'

		req = json.loads(request.data)
		print req
		# allRegisteredDevices.append(req['TOKEN'])
		allRegisteredDevices[req['NAME'].lower().strip()] = req['TOKEN']


		with open('savedDevices.pickle', 'a') as handle:
			pickle.dump(allRegisteredDevices, handle, protocol=pickle.HIGHEST_PROTOCOL)

		data = {'name': 'muditTHEGreat'}
		return jsonify(data)


if __name__ == '__main__':
   app.run(host = '0.0.0.0',debug = True)