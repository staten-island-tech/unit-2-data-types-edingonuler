# noun = input("Noun? ")
# first_verb = input("First Verb? ")
# second_verb = input("Second Verb? ")
# number = input("Number? ")
# celeb = input("Celebrity? ")

# print(f"When John was on vacation, he saw {celebrity} in the lobby of the 
# hotel he was staying in. He started {first_verb} and {second_verb} until he
# tripped on a {noun}. Then he got on the elevator and went to the {number}.")

# def even_or_odd(number):
#     if number % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")
# even_or_odd(20)


# def tip(bill, service):
#     if service == "Bad":
#         print(f"you tipped 0% bill. Your total is {bill}")
#     elif service == "Okay":
#         print(f"you tipped 15% bill. Your total is {bill*1.15}")
#     elif service == "Good":
#         print(f"you tipped 20% bill. Your total is {bill*1.20}")
#     elif service == "Great":
#         print(f"you tipped 25% bill. Your total is {bill*1.25}")
# tip(120, "Good")


# def factoring(number):
#     factors = []

#     for i in range(1, number+1):
#         if number % i == 0:
#             factors.append(i)

#     print(factors)
# factoring(20)


def gcf(first_number, second_number):
    list1 = []

    for i in range(1, first_number+1):
        if first_number % i == 0 and second_number % i == 0:
            list1.append(i)

    print(list1[len(list1)-1])
gcf(20, 40)