import os
def winner(new_data):
    amt=0
    for keys in new_data:
        if new_data[keys]>amt:
            amt=new_data[keys]
            winner=keys
    print(f"the winner is {winner} with amount={amt}")
    print('Here the details of Auction bidders:')
    print(new_data)

bidder_data={}
end=False
while not end:
    bidder=input("what is your name?:")
    price=int(input("Enter your money:"))
    bidder_data[bidder]=price
    more_bidders=input("Enter 'yes' to continue Auction or 'no' to end Auction:").lower()
    if more_bidders=='no':
        end=True
        winner(bidder_data)
    elif more_bidders=='yes':
        os.system('cls')
