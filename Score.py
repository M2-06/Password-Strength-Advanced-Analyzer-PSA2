def evaluate_password_strength(password):
    score = 0

# Password length : 

    recommandation = "consider it being at least 10 characters long"
    passlen = ""

    if len(password) <= 4:
        score -= 100
        passlen = "Your password is way too short," + recommandation
    elif len(password) < 6:
        score -= 20
        passlen = "Your password is too short," + recommandation
    elif len(password) < 7:
        score -= 20
        passlen = "Your password is short," + recommandation
    elif len(password) <= 9:
        score += 0
        passlen = "Your password is not short but it would be preferable if you " + recommandation
    elif len(password) >= 12:
        score += 35
        passlen = "The length of your password is optimal, hats off"
    elif len(password) >= 10:
        score += 25
        passlen = "The length of your password is optimal, hats off"
   


# Password containing consecutive identical charachters
    
    identicals = False
    consecutive = "" 

    
    for x in range(len(password) - 1):
         if password[x] == password[x + 1]:
              identicals = True
              
         

    if identicals == True:
        score -= 15
        consecutive = "Your password contains two or more consecutive identical characters, consider modifying them"
    elif identicals == False:
        score += 15
        consecutive = "Your password does not contain any consecutive identical characters, well done"

# Password containing uppers lowers and numbers / symbols :
    
    uplow = ""
    numbers = ""
    symbols = ""
    
    # Part 1 : containing uppers, lowers, numbers/symbols:
    
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 10
        uplow = "Your password contains upper and lower case letters, good job"
    if any(c.isdigit() for c in password):
        score += 10
        numbers = "Your password contains numbers, great work"
    if any(not c.isalnum() for c in password):  
        score += 15
        symbols = "Your password contains symbols, nice one"

         
    
    # Part 2 : not containing uppers, lowers, numbers/symbols:

    if not ( any(c.islower() for c in password) and any(c.isupper() for c in password) ):
        score -= 10
        uplow = "Your password does not contain any upper and lower case letters, consider adding them"
    if not any(c.isdigit() for c in password):
        score -= 10 
        numbers = "Your password does not contain any number, consider putting in at least 2 of them"
    if not any(not c.isalnum() for c in password):  
        score -= 5 
        symbols = "Your password does not contain any symbol, they are really important so dont forget them"

# Password contained in one of the pwned / common passwords list :

    with open("CommonPasswords100k.txt", "r", encoding='utf-8') as file:
      mdplist = [line.strip() for line in file]
   
    match_password = False
    dbleak = ""

    for mdp in mdplist:
          if len(mdp) >=4 and ( mdp in password or mdp == password ):
             score -= 60
             match_password = True
             dbleak = "Password found in a common list of passwords"
             break
        
    if match_password == False:
             score += 15

# The final score
    
    print("Your Score is:", score)

# Specific weaknesses
  
    print(passlen)
    print(consecutive)
    print(uplow)
    print(numbers)
    print(symbols)
    print(dbleak)

    return score, passlen, consecutive, uplow, numbers, symbols, dbleak

     


    

   


