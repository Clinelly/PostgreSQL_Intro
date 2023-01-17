from sqlalchemy import (
    create_engine, Column, Float, ForeignKey, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing the instructions from the "chinook" database
db = create_engine("postgresql:///chinook")
base = declarative_base()


# class for programmer table
class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)


# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)

# opens an actual session by calling the Session() subclass defined above
session = Session()

# creating the database using declarative_base subclass
base.metadata.create_all(db)


# creating records on programmer table
ada_lovelace = Programmer(
    first_name="Ada",
    last_name="Lovelace",
    gender="Female",
    nationality="British",
    famous_for="First Programmer",
)

alan_turing = Programmer(
    first_name="Alan",
    last_name="Turing",
    gender="Male",
    nationality="British",
    famous_for="Modern Computing",
)

grace_hopper = Programmer(
    first_name="Grace",
    last_name="Hopper",
    gender="Female",
    nationality="American",
    famous_for="COBOL Language",
)

margaret_hamilton = Programmer(
    first_name="Margaret",
    last_name="Hamilton",
    gender="Female",
    nationality="American",
    famous_for="Apollo 11",
)

bill_gates = Programmer(
    first_name="Bill",
    last_name="Gates",
    gender="Male",
    nationality="American",
    famous_for="Microsoft",
)

tim_berners_lee = Programmer(
    first_name="Tim",
    last_name="Berners-Lee",
    gender="Male",
    nationality="British",
    famous_for="World Wide Web",
)

stuart_wall = Programmer(
    first_name="Stuart",
    last_name="Wall",
    gender="Male",
    nationality="British",
    famous_for="Going Rogue",
)

# add each instance of programmers to session
# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hamilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(stuart_wall)

# commit to database
# session.commit()

# update single record
# programmer = session.query(Programmer).filter_by(id=7).first()
# programmer.famous_for = "World President"

# updating multiple records
# people = session.query(Programmer)
# for person in people:
#     if person.gender == "Female":
#         person.gender = "F"
#     elif person.gender == "Male":
#         person.gender = "M"
#     else:
#         print("Gender not defined")
#     # commit to database
#     session.commit()

# delete a single record
# fname = input("Enter a first name: ")
# lname = input("Enter a last name: ")
# programmer = session.query(Programmer).filter_by(
#     first_name=fname, last_name=lname
#     ).first()
# # defensive programming
# if programmer is not None:
#     print(
#         "Programmer found: ", programmer.first_name + " " + programmer.last_name
#         )
#     confirmation = input("Are you sure you want to delete this record? (y/n) ")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Record deleted")
#     else:
#         print("Record not deleted")
# else:
#     print("No records found")

# delete multiple records
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()

# query database to find all programmers
programmers = session.query(Programmer)
for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name + " " + programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep=" | "
    )
