## Welcome to the best quotes gen ever made (trust me)

# Installation and Usage

- `git clone git@github.com:Joseph-Barnett/Python_Quotes_Api_Server.git`
- In terminal run `pipenv shell`
- Add a .env file
- Create a database - I used elephantsql
- Inside of the .env add this text
  ```
  FLASK_DEBUG=1
  SQLALCHEMY_DATABASE_URI=postgresql:// you actually link to the database
  ```
- Make sure that you add ql to your postgres url like I have above
- in terminal run `python seed.py`
- in terminal run `pipenv run dev`, server runs on (http://127.0.0.1:5000)
