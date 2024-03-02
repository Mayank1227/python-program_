# given string
given_string = "madam"
 
reverse_string = ""
 
for i in given_string:
    reverse_string = i + reverse_string  
 
if(given_string == reverse_string):
   print("The string", given_string,"is a Palindrome.")
    
else:
   print("The string",given_string,"is NOT a Palindrome.")