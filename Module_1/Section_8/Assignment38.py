'''
@author: SOURABH GUPTA
'''
'''
Refer to the following assignment which you have already executed in Functions section.
Modify your code to implement Exception Handling and display appropriate error message wherever applicable.At an airport,
a traveler is allowed entry into the ﬂight only if he clears the following checks:
1.Baggage Check
2.Immigration Check
3.Security Check

The logic for the check methods are given below:

check_baggage (baggage_weight)•
returns True if baggage_weightis greater than or equal to 0 and less than or equal to 40.
Otherwise returns False.

check_immigration (expiry_year)
•returns True if expiry_yearis greater than or equal to 2001 and less than or equal to 2025.
Otherwise returns False.

check_security(noc_status)
•returns True if noc_statusis 'valid' or 'VALID', for all other values return False.

traveler()

•Initialize the traveler Id and traveler name and invoke the functions check_baggage(),
check_immigration() and check_security() by passing required arguments.
•Refer the table below for values of arguments.
    variable            values
    traveler_Id         1001
    traveler_name       Jim
    baggage_weight      Thirty
    expiry_year         2016
    noc_status          0
•If all values of check_baggage(), check_immigration() and check_security() are true,
display traveler_id and traveler_name
display "Allow Traveler to ﬂy!"
Otherwise,
display traveler_id and traveler_name
display "Detain Traveler for Re-checking!“
Invoke the traveler() function.
Modify the values of diﬀerent variables in traveler() function and observe the output
'''
def check_baggage(baggage_weight):
    if baggage_weight >= 0 and baggage_weight <= 40:
        return True
    else:
        return False

def check_immigration(expiry_year):
    if expiry_year >= 2001 and expiry_year <= 2025:
        return True

    else:
        return False

def check_security(noc_status):
    if noc_status == 'valid' or noc_status == 'VALID':
        return True
    else:
        return False

def traveler():
    traveler_Id = 1001
    traveler_name = "Jim"
    print(traveler_Id)
    print(traveler_name)
    try:
        if check_baggage(35) and check_immigration(2019) and check_security("VALID"):
            print("Allow Traveler to ﬂy")
        else:
            print("Detain Traveler for Re-checking")
    except TypeError:
        print("Invalid input")

traveler()
