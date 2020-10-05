# User Verification Service using Python, Chalice and AWS Lambda
This is an example of a serverless user verification service that is built using [Twilio Verify](https://www.twilio.com/verify), the [Chalice Framework](https://aws.github.io/chalice/quickstart.html) and [AWS Lambda](https://aws.amazon.com/lambda/)

## Installation
1. Clone the repo and change into directory
```shell
git clone https://github.com/dotunj/twilio-chalice-verify.git
cd twilio-chalice-verify
```
2. Create a virtual environment and install the dependencies with Pip. For Linux and Mac users:

```shell
virtualenv venv
source venv/bin/activate
(venv) pip install -r requirements-dev.txt
```
If you are on Windows, then use the following commands instead:

```shell
virtualenv venv
venv\Scripts\activate
(venv) pip install -r requirements-dev.txt
```

## Running Locally
Edit the `./chalice/config.json` with your Twilio Credentials and then run the application with the Chalice CLI.

```shell
chalice local
```
This should start a chalice application listening on port `8000`. 

## Examples
You can then make a `POST` request to send a verification token to the user's phone number, as well as another `POST` request to verify the token. For example, using `curl` to send a token:

```shell
curl -H "Content-Type: application/json" -X POST -d '{"phone_number": "+1234567890"}' http://localhost:8000/send/token
```

To verify the token:
```shell
curl -H "Content-Type: application/json" -X POST -d '{"phone_number": "+1234567890", "token": "123456"}' http://localhost:8000/verify/token
```

## Further Reading
* Check out the [Chalice documentation for more details on building with Chalice](https://aws.github.io/chalice/main.html).
* More Information about the [Twilio Verify API](https://www.twilio.com/docs/verify/api)
