import json
Wallet_Emails = {}#stores old and new created wallets with username as key and password as value

file_name = "/Users/omarmedhat/CS/MySceretWallet/mydata.json"
def save_dictionary( Wallet_Emails , filename ): # to save what's in Wallet_Emails into mydata.json
    with open(filename , 'w') as file:
        json.dump(Wallet_Emails, file)

def load_dictionary( filename ): # load dictionary from json into Wallet_Emails in each run
    with open(filename , 'r') as file:
        dictionary = json.load(file)
        return dictionary 
    
Wallet_Emails = load_dictionary(file_name)

def Encryption(text): #change normal text into Encrtypted text 
    Encrypted = ""
    for char in text:
        if char.isalpha():
            character = chr((ord(char) - 97 + 5) % 26 + 97) # used the number 97 to treat all characters as lowecase based on ASCI
            Encrypted = Encrypted + character
        else: #spaces, special characters, and numbers
            Encrypted = Encrypted + char
    return Encrypted

def Decryption(Enc_text):
    Decrypted=""
    for char in Enc_text:
        if char.isalpha():
            character = chr((ord(char) - 97 - 5) % 26 + 97) # used the number 97 to treat all characters as lowecase based on ASCI
            Decrypted = Decrypted + character
        else: #spaces, special characters, and numbers
            Decrypted = Decrypted + char
    return Decrypted


def Create_Wallet():
    created = False
    Username = input("Enter your User Name: ")
    Password = input("Enter your Password: ")
    for key in Wallet_Emails:
        if Username == key :
            print("This UserName already exist")  
        elif Username != key :
            created = True
            print("You sucessfuly created a Wallet, Now you could store anything inside!")
            break
    if created :
         Wallet_Emails[Username] = {"password" : Password , "text": ""}
         save_dictionary( Wallet_Emails , file_name )


def LogIn():
    found = False
    Input_UserName = input("Enter your User Name: ")
    Input_Password = input("Enter your password: ")
    for keys in Wallet_Emails:
        if Input_UserName == keys:
            print("You sucessfuly logged in")
            Store_inside_wallet(Input_UserName , Input_Password)
            found = True
    if not found:
        print("Wrong username or password")
            

def Store_inside_wallet(username , password):
    secret_text = input("enter the text you want to store: ")
    found = False
    for key in Wallet_Emails:
        if key == username :
            Wallet_Emails[username]["text"] = Encryption(secret_text)
            save_dictionary(Wallet_Emails , file_name)
            print("Done, your text is stored and encrypted!")
            print(Wallet_Emails[key])
            found = True
            Read_from_wallet(username) #remove the comment to decrypt what's stored in the wallet 
    if not found:
        print("Error")
    
    

def Read_from_wallet(user):
    for key in Wallet_Emails:
        if key == user:
            stored_text = Decryption(Wallet_Emails[user]["text"])
            print("Your decrypted stored text is: ", stored_text)

LogIn()