# shipment
recruitment task

###How to run:

Go to directory shipments, build virtualn env ('pipenv install'), load needed packagers (pip install -r requirements.txt ) run command:

'./manage.py runserver'

Go to shipments-gui, run command: 'npm install' and 'npm run serve'. The front should be on address: http://localhost:8080/



###
Data model:

I've created the four models: 

Delivery
Address
Courier
Parcel

Delivery contains informations about date of send and delivery and status of parcel.
Parcel contains information about parcel (number) and addresses.
Courier - name of the man, who deliver.
Address: information about the sender or receiver.




