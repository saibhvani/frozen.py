#intersection
attendees= {'bhavani','chinni','sravya'}
attendees1 = {'raju','sravya','chinni'}
print(attendees.intersection_update(attendees1))
print(attendees)
print(attendees1)

#isdisjoint
attendees= {'bhavani','chinni','sravya'}
attendees1 = {'raju','sravya','chinni'}
print(attendees.isdisjoint(attendees1))

#difference
attendees= {'bhavani','chinni','sravya'}
attendees1 = {'raju','sravya','chinni'}
print(attendees.difference(attendees1))

#symmetric
attendees= {'bhavani','chinni','sravya'}
attendees1 = {'raju','sravya','chinni'}
print(attendees.symmetric_difference(attendees1))

#symmetric differencec update
attendees= {'bhavani','chinni','sravya'}
attendees1 = {'raju','sravya','chinni'}
print(attendees.symmetric_difference_update(attendees1))

#issubset
attendees= {'bhavani','chinni','sravya'}
attendees1 = {'raju','sravya','chinni'}
print(attendees.issubset(attendees1))

#issuperset
attendees= {'bhavani','chinni','sravya'}
attendees1 = {'raju','sravya','chinni'}
print(attendees.issuperset(attendees1))

##dictionary
#implict
attendees= {'bhavani','chinni','sravya'}
print(type(attendees))

#explict
attendees=dict=({'bhavani','chinni','sravya'})
print(type(attendees))

#datatype/variable annotation
attendees:dict=({'bhavani','chinni','sravya'})
print(type(attendees))
