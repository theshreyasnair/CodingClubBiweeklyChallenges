class BankAccount:
  def __init__(self, name):
    self.name = name
    self.balance = 0

  def deposit(self, deposit):
    self.balance += deposit

  def withdraw(self, withdrawal):
    self.withdrawal = withdrawal
    self.balance -= withdrawal

  def return_balance(self):
    print(self.balance)

  def return_account_details(self):
    print(f"Account Name: {name}")
    print(f"Balance: {self.balance}")

name = input("Enter your name: ")


acc = BankAccount(name)

while True:
  option = input("Enter something to do: ")
  if(option.lower() == "deposit"):
      deposit = int(input("Enter some money to be deposited: "))
      acc.deposit(deposit)
  elif(option.lower() == "balance"):
    acc.return_account_details()
  elif(option.lower() == "withdraw"):
    if(acc.balance == 0):
      print("You have no money to withdraw")
    else:
      withdraw = int(input("Enter an ammount to withdraw: "))
      acc.withdraw(withdraw)
  elif(option.lower() == "exit"):
      break
