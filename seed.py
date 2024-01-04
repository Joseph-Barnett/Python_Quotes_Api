from application import db
from application.quotes.models import Quote

db.drop_all()
print("Dropping Database")

db.create_all()
print("Creating Database")

print("Seeding Database")

entry1 = Quote(text="The Analytical Engine has no pretensions whatever to originate anything. It can do whatever we know how to order it to perform.", author="Ada Lovelace")
entry2 = Quote(text="The computer was born to solve problems that did not exist before.", author="Bill Gates")
entry3 = Quote(text="People worry that computers will get too smart and take over the world, but the real problem is that they're too stupid and they've already taken over the world.", author="Pedro Domingos")
entry4 = Quote(text="That's the thing about people who think they hate computers. What they really hate is lousy programmers.", author="Larry Niven")
entry5 = Quote(text="Man is a slow, sloppy, and brilliant thinker; computers are fast, accurate, and stupid.", author="John Pfeiffer")
entry6 = Quote(text="We build our computers the way we build our cities—over time, without a plan, on top of ruins.", author="Ellen Ullman")
entry7 = Quote(text="Programs must be written for people to read, and only incidentally for machines to execute.", author="Harold Abelson")
entry8 = Quote(text="No computer is ever going to ask a new, reasonable question. It takes trained people to do that.", author="Grace Hopper")
entry9 = Quote(text="Einstein repeatedly argued that there must be simplified explanations of nature, because God is not capricious or arbitrary. No such faith comforts the software engineer.", author="Frederick P. Brooks Jr.")

db.session.add_all([entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9])

db.session.commit()
