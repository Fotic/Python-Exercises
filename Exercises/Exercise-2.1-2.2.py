# Εισαγωγή στον Προγραμματισμό με Python
# Εβδομάδα 2
#===================================================
#
# Άσκηση 2.1 Ρίζες τριωνύμου
#

##import math as ma
##
##a = int(input('a = '))
##b = int(input('b = '))
##c = int(input('c = '))
##
##d = b**2 - 4*a*c
##
##if d < 0:
##    print('Δεν υπάρχουν πραγματικές ρίζες')
##elif d == 0:
##    r = -b/(2*a)
##    print('Υπάρχει μία ρίζα: {:10.5f}'.format(r))
##else:
##    r1 = (-b+ma.sqrt(d))/(2*a)
##    r2 = (-b-ma.sqrt(d))/(2*a)
##    print('Υπάρχουν 2 πργματικές ρίζες: {:8.3f} και {:8.3f}'.format(r1, r2))
#
#=========================================================================================================================
#
#
# Άσκηση 2.2 Ρουλέτα
#

##import random as rn
##
##while True:
##    num=rn.randint(0,36)
##    print('\nΚληρώθηκε το', num)
##    
##    if num!=0:
##        if num<=18:
##            print('Μικρός (1-18)')
##        else:
##            print('Μεγάλος (19-36)')
##
##        if num%2:
##            print('Μονός')
##            odd = True 
##        else:
##            print('Ζυγός')
##            odd = False
##            
##        if num<=10 or 19<=num<=28:
##            if odd:
##                print('Κόκκινος')
##            else:
##                print('Μαύρος')
##        else:
##            if odd:
##                print('Μαύρος')
##            else:
##                print('Κόκκινος')
##
##    inp = input('Enter: Συνέχεια, q: Έξοδος ')
##    if inp=='q':
##        break

# Η παραπάνω λυση είναι μια απλη 'τυπική' λυση που θα μπορούσαμε
# να γράψουμε και σε άλλες γλωσσες προγραμματισμού
# Προσεξτε ότι δεν χρειάζεται να δημιουργησουμε πολλα και συνθετα φωλιασμένα if
# (όπως κάνατε πολλοί) αφού τα χαρακτηριστικά μικρός/μεγάλος και μονός/ζυγός
# μπορούν να εξεταστοούν ανεξάρτητα το ένα από το άλλο
#
#

# Μια πιο Pythonic έκδοση του κώδικα δίνεται παρακάτω:
# Προσέξτε πώς χρησιμοποιούνται οι λογικές μεταβλητές is_small, is_even, is_red
# που παιρνουν τιμή True/False ανάλογα αν ισχυουν οι συνθήκες στο δεξιό μέρος της ανάθεσης
# Και επίσης πώς παίρνει τιμη η is_red με μία έκφραση υπό συνθήκη  
# Παρομοια λειτουργούν και οι print (δηλ. με έκφραση υπό συνθήκη)
#
# Επίσης προσέξτε και την τεχνικη με την input στο τέλος του βροχου ώστε να σταματά
# η εκτέλεση (break) αν ο χρήστης εισάγει 'q'
#

##import random as rn
##
##while True: 
##    num=rn.randint(0,36)
##    print('\nΚληρώθηκε το', num)
##
##    if num!=0:
##        is_small = (num<=18)
##        is_even = (num%2==0)
##
##        if num<=10 or 19<=num<=28:
##            is_red = False if is_even else True
##        else:
##            is_red = True if is_even else False
##        
##        print('Μικρός' if is_small else 'Μεγάλος', end=' ')        
##        print('Ζυγός' if is_even else 'Μονός', end=' ')
##        print('Κόκκινος' if is_red else 'Μαύρος')
##    
##    if input('Enter: Συνέχεια, q: Έξοδος ')=='q':
##        break



























