def evaluate_password_strength(password):
    score = 0

# Password length : 

    recommandation = "consider it being at least 10 characters long"
    passlen = ""

    if len(password) <= 2:
        score -= 80
        passlen = "Your password is way too short," + recommandation
    elif len(password) == 3:
        score -= 50
        passlen = "Your password is way too short," + recommandation
    elif len(password) <= 5:
        score -= 25
        passlen = "Your password is way too short," + recommandation
    elif len(password) <= 7:
        score -= 10
        passlen = "Your password is too short," + recommandation
    elif len(password) <= 9:
        score += 0
        passlen = "Your password is not short but it would be preferable if you " + recommandation
    elif len(password) == 10:
        score += 25
        passlen = "The length of your password is optimal, hats off"
    elif len(password) >= 11:
        score += 35
        passlen = "The length of your password is really optimal, hats off"
    
   


# Password containing consecutive identical charachters
    
    identicals = False
    consecutive = "" 

    
    for x in range(len(password) - 1):
         if password[x] == password[x + 1]:
              identicals = True
              
         

    if identicals == True:
        score -= 5
        consecutive = "Your password contains two or more consecutive identical characters, consider modifying them"
    elif identicals == False:
        score += 15
        consecutive = "Your password does not contain any consecutive identical characters, well done"

# Password containing uppers lowers and numbers / symbols :
    
    uplow = ""
    numbers = ""
    symbols = ""
    
    # Checking for uppers, lowers, numbers/symbols:
    
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 10
        uplow = "Your password contains upper and lower case letters, Good job !"
    else : 
        score -= 15
        uplow = "Your password does not contain upper and lower case letters, consider having the two of them for an increased password strength."
    if any(c.isdigit() for c in password):
        score += 15
        numbers = "Your password contains numbers, Great work !"
    else : 
        score -= 10
        numbers = "Your password does not contain any number, consider having at least 2 numbers in it."
    if any(not c.isalnum() for c in password):  
        score += 20
        symbols = "Your password contains symbols, Great job !"
    else : 
        score -= 10
        symbols = "Your password does not contain any symbol, they are really important ! Dont forget them."

# Password contained in one of the common passwords list :

    with open("CommonPasswords100k.txt", "r", encoding='utf-8') as file:
      mdplist = [line.strip() for line in file]
   
    match_password = False
    commonality = "No part of your password is commonly used. Good job!"

    for mdp in mdplist:
          if len(mdp) >=4 and ( mdp in password or mdp == password ):
             score -= 45
             match_password = True
             commonality = "A part of your password has been found in a common list of passwords, consider changing it !"
             break
        
    if match_password == False:
             score += 15

# The final score  out of ten /10
    
    # Score standarization from (-100 -> 100) to ( 0 -> 10) rounded )
    score = (( ( score + 100 ) / 200 ) * 10 )
    score = int(round(score,0))
    score = f"{score}/10"
    
    print("Your Score is:", score)

# Specific weaknesses
  
    print(passlen)
    print(consecutive)
    print(uplow)
    print(numbers)
    print(symbols)
    print(commonality)

    return score, passlen, consecutive, uplow, numbers, symbols, commonality

    

   



