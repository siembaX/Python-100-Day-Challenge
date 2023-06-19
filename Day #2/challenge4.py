""" Bill Tip Calculator | Split Bills as well """

bill = input("How much is your bill?\n$")
tip = input("Please specify the percentile of your tip e.g 10,12,15..\n")
tip_int = float(tip)
bill_int = float(bill)

percentile = tip_int / 100
total_percentile = bill_int * percentile
total_bill = total_percentile + bill_int

print(f"Your total bill is {total_bill}")

members = input("How many are sharing the bill?\n")
total_shared = total_bill / int(members)
total_shared = round(total_shared, 2)
print(f"Your total bill shared amongst {members} members is: ${total_shared}")
