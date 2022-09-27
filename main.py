from replit import clear
from art import *
print(logo)
available=True
all_details=[]

def highest_bid(all_details):
  max_bid=0
  for  dic in all_details:
     if dic["bid_value"]>max_bid:
       max_bid= dic["bid_value"]
       max_bid_position = dic
  print(f'{max_bid_position["name"]} has won the auction with highest bid value of ${max_bid_position["bid_value"]}')
  
while available:
  name = input("what is your name ")
  bid_value = int(input("what's your bid?: $"))
  bidders_available = input("Are there any other bidders? Type 'yes' or  'no'")
  clear()
  if bidders_available =="yes":
    member_details={}
    member_details["name"]=name
    member_details["bid_value"]=bid_value
    all_details.append(member_details)
  elif bidders_available=="no":
    available=False
    highest_bid(all_details)
  else:
    print("Invalid entry")
    bidders_available = input("Are there any other bidders? Type 'yes' or  'no'")

