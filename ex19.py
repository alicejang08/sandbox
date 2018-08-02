# cheese_and_crackers function definition and printing 4 main lines of text
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


# Using numbers direcctly to set up the numbers fo cheese and crackers
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


# Using variables for setting up the numbers
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackes = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackes)

# math function detected
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


# double kill: variables plus math damn
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackes + 1000)
