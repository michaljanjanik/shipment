# shipment
recruitment task

## How to run:

Go to directory shipments, build virtualn env ('pipenv install'), go into ('pipenv shell'), load needed packagers (pip install -r requirements.txt ), run command:

'./manage.py runserver'

Go to shipments-gui, run command: 'npm install' and 'npm run serve'. The front should be on address: http://localhost:8080/

## Data model:

I've created the four models: 

Delivery, Address, Courier, Parcel.

<b>Delivery</b> contains informations about date of send and delivery and status of parcel.<br>
<b>Parcel</b> contains information about parcel (number) and addresses.<br>
<b>Courier</b> - name of the man, who deliver.<br>
<b>Address</b>: information about the sender or receiver.<br>

## Unit test

Go to 'shipments', and run './manage.py test' .


