# Εισαγωγή στον Προγραμματισμό με Python
# Εβδομάδα 5
#===================================================
#
# Άσκηση 5.1  Στατιστικη
#
# Μια απλη λυση ειναι η παρακάτω:
#
##import random as rn
##import math
##
##def stats(lista):
##    m = sum(lista)/len(lista)            # Μέσος όρος, το m ειναι τοπικό όνομα
##    suma=0
##    for x in lista:
##        suma += (x-m)**2                 # Άθροισμα τετραγώνων 
##    s = math.sqrt(suma/(len(lista)-1))   # Τυπικη απόκλιση, το s επίσης ειναι τοπικό όνομα 
##    return m,s                           # Επιστρέφει στο κύριο πρόγραμμα τα m & s
##
### -- main --  
##N = int(input('Πλήθος ακεραίων στη λίστα: '))
##L = [rn.randint(1,20)for i in range(N)]            # Δημιουργία με list comprehension, η L ανήκει στην καθολική εμβέλεια 
##
##M, sd = stats(L)                                   # Κληση της stats με παράμετρο την L
##                                                   # Τα ονόματα M & sd ειναι στην καθολική εμβέλεια
##                                                   # Συνδέονται με τις τιμές των m & s που υπολόγισε η συνάρτηση  
##
##print('Λίστα:', L)
##print('Mέσος όρος = {:6.2f}, Τυπική απόκλιση = {:6.2f}'.format(M,sd))


#
# Μία περισσότερο 'Pythonic' λυση:
#

##import random as rn
##import math
##
##def stats2(lista):
##    m = sum(lista)/len(lista)            
##    # Υπολογισμός της s στη γραμμή της return
##    # Προσέξτε την τεχνικη list comprehension που δημιουργεί λίστα με τα τετράγωνα που αθροίζει η sum  
##    return m, math.sqrt(sum([(x-m)**2 for x in lista])/(len(lista)-1))
##    
### -- main --  
##N = int(input('Πλήθος ακεραίων στη λίστα: '))
##L = [rn.randint(1,20)for i in range(N)]
##mo, sd = stats2(L)
##print('Λίστα:', L)
##print('Mέσος όρος = {:6.2f}, Τυπική απόκλιση = {:6.2f}'.format(*stats2(L)))   # Κληση της stats2 μέσα στην .format
##



#
#=========================================================================================================================
#
#
# Άσκηση 5.2  Συνάρτηση γεννήτορας 
# 
### Ένας τρόπος για να γράψουμε την myrange μπορεί να είναι ο εξής:  
##
##def myrange(N,logos):
##    z=1
##    for k in range(N):
##        yield z
##        z = z*logos
##
##
##for i in myrange(5,10):
##    print(i)
##
##print()
##
##for i in myrange(6,2):
##    print(i)
##
##------------------------------------
## Ένας άλλος τρόπος:
##
##def myrange(N,logos):
##    z=1;k=0
##    while k<N:
##        yield z
##        z = z*logos
##        k+=1
