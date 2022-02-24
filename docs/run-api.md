## Set-up

Install required packages (ideally in a virtual environment): `pip install -r requirements.txt`.

## How to run the API locally

Run the server: `uvicorn main:app`

The API can be found here: http://127.0.0.1:8000/

And the associated docs here: http://127.0.0.1:8000/docs

The three endpoints are:
1. `http://127.0.0.1:8000/helloworld` -  return JSON `{"msg": "Hello World"}`
2. `http://127.0.0.1:8000/add/?first=6&second=4` - return JSON of sum of 2 numbers `{"sum": 10}` (can change to any integers)
3. `http://127.0.0.1:8000/joinstrings/?first_str=cat&second_str=dog` - return JSON with strings joined by dash `{"output":"cat-dog"}` (can change to any two strings)

## Run the tests

Make sure the relevant packages have been installed. Then run: `python -m pytest`.