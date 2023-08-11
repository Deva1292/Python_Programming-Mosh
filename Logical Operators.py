# AND: both conditions should be true
# OR: at least one condition should be true
# NOT: inverses the value

# if applicant has high income AND good credit
    # Eligible for loan

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

# if applicant has high income OR good credit
   # Eligible for loan

if has_high_income or has_good_credit:
    print("Eligible for loan")

# if the applicant has good credit and doesn't have a criminal record
 # eligible for loan

 has_good_credit = True
 has_criminal_record = False

 if has_good_credit and not has_criminal_record:
     print("Eligible for loan")
