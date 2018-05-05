'''
Created on 26-Mar-2018

@author: SOURABH GUPTA
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