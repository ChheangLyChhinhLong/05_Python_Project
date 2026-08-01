# create a list to store accounts | បង្កើត List មួយដើម្បីផ្ទុកគណនី
def create_account(accounts):
    account = {}
    account['id'] = input("Enter account ID: ")
    account['ssn'] = input("Enter SSN: ")
    account['acc_num'] = input("Enter account number: ")
    account['acc_name'] = input("Enter account name: ")
    account['acc_type'] = input("Enter account type: ")
    account['balance'] = float(input("Enter initial balance: "))
    accounts.append(account)
    print("Account created successfully!")

# update an existing account​​ | Update គណនីដែលមានស្រាប់
def update_account(accounts):
    acc_id = input("Enter account ID to update: ")
    for account in accounts:
        if account['id'] == acc_id:
            account['ssn'] = input("Enter new SSN: ")
            account['acc_num'] = input("Enter new account number: ")
            account['acc_name'] = input("Enter new account name: ")
            account['acc_type'] = input("Enter new account type: ")
            print("Account updated successfully!")
            return
    print("Account not found.")

# delete an account | លុបគណនី
def delete_account(accounts):
    acc_id = input("Enter account ID to delete: ")
    for account in accounts:
        if account['id'] == acc_id:
            accounts.remove(account)
            print("Account deleted successfully!")
            return
    print("Account not found.")

# deposit money into an account | ដាក់ប្រាក់ទៅក្នុងគណនី
def deposit(accounts):
    acc_id = input("Enter account ID to deposit: ")
    for account in accounts:
        if account['id'] == acc_id:
            amount = float(input("Enter amount to deposit: "))
            account['balance'] += amount
            print(f"Deposited {amount}. New balance is {account['balance']}.")
            return
    print("Account not found.")

# withdraw money from an account | ដកប្រាក់ទៅក្នុងគណនី
def withdraw(accounts):
    acc_id = input("Enter account ID to withdraw: ")
    for account in accounts:
        if account['id'] == acc_id:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= account['balance']:
                account['balance'] -= amount
                print(f"Withdrew {amount}. New balance is {account['balance']}.")
            else:
                print("Insufficient balance.")
            return
    print("Account not found.")

# show all accounts | បង្ហាញគណនីទាំងអស់
def show_all_accounts(accounts):
    if not accounts:
        print("No accounts to show.")
        return
    for account in accounts:
        print(f"ID: {account['id']}, SSN: {account['ssn']}, Account Number: {account['acc_num']}, "
              f"Account Name: {account['acc_name']}, Account Type: {account['acc_type']}, "
              f"Balance: {account['balance']}")

# main function to run the bank account system | មុខងារសំខាន់ដើម្បីដំណើរការប្រព័ន្ធគណនីធនាគារ
def main():
    accounts = []
    while True:
        print("\nBank Account System")
        print("1. Create Account")
        print("2. Update Account")
        print("3. Delete Account")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Show All Accounts")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            create_account(accounts)
        elif choice == '2':
            update_account(accounts)
        elif choice == '3':
            delete_account(accounts)
        elif choice == '4':
            deposit(accounts)
        elif choice == '5':
            withdraw(accounts)
        elif choice == '6':
            show_all_accounts(accounts)
        elif choice == '7':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
    
# run the main function | ដំណើរការមុខងារសំខាន់     
if __name__ == "__main__":
    main()

# Python List & Dictionaries
# ------------------------------------------------------------------------------------
# -Assignment-Bank Account System
# 1-ចូរបង្កើត List មួយដែលអាចផ្ទុកគណនីជា dictionary បានច្រើន ដែល dictionary នោះមានពត៌មានដូចខាងក្រោម៖
# -id: លេខរៀង
# -ssn: លេខអត្តសញ្ញាណប័ណ
# -acc_num: លេខគណនី
# -acc_name: ឈ្មោះគណនី
# -acc_type: ប្រភេទគណនី (Saving/Current)
# -balance: ចំនួនទឹកប្រាក់
# 2-ចូរបង្កើតមុខងារដូចជា៖
# -Create New Account
# -Update Account
# -Delete Account
# -Deposit
# -Witdrawal
# -Show All Account
# ------------------------------------------------------------------------------------

# ឧទាហរណ៍នៃការប្រើប្រាស់កម្មវិធីនេះ៖
# បង្កើតគណនីថ្មី:
# Enter account ID: 1 | បញ្ចូលលេខសម្គាល់គណនី: 1
# Enter SSN: 123456789 | បញ្ចូលលេខសម្គាល់សង្គម: 123456789
# Enter account number: 987654321 | បញ្ចូលលេខគណនី: 987654321
# Enter account name: John Doe | បញ្ចូលឈ្មោះគណនី: John Doe
# Enter account type: Saving | បញ្ចូលប្រភេទគណនី: សន្សំ
# Enter initial balance: 1000 | បញ្ចូលតម្លៃដើម: 1000
# Account created successfully!