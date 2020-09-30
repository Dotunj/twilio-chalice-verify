from os import environ as env
from chalice import Chalice, Response
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

app = Chalice(app_name='twilio_verify')

twilio_client = Client()
verify_client = twilio_client.verify.services(env.get('TWILIO_SERVICE_SID'))

@app.route('/send/token', methods=['POST'])
def send_verification_token():
    body = app.current_request.json_body
    phone_number = body.get('phone_number')
    if phone_number:
        try:
          verification = verify_client.verifications.create(to=phone_number, channel='sms')
          return Response(status_code=201, body={'message': 'Verification sent', 'message_sid': verification.sid})
        except TwilioRestException as exception:
          return Response(status_code=400, body={ 'message': exception.msg })
    return Response(status_code=400, body={ 'message': 'Provide a phone number'})

@app.route('/verify/token', methods=['POST'])
def verify_token():
    body = app.current_request.json_body
    phone_number = body.get('phone_number')
    token = body.get('token')
    if phone_number and token: 
        try:
          verification_check = verify_client.verification_checks.create(to=phone_number, code= token)
          return Response(status_code=200, body={'message': 'Obtained verification status', 'status': verification_check.status})
        except TwilioRestException as exception:
          return Response(status_code=400, body={ 'message': exception.msg })
    return Response(status_code=400, body={ 'message': 'Provide a phone number and token field'})


    