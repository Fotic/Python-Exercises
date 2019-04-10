# Εισαγωγή στον Προγραμματισμό με Python
# Εβδομάδα 4
# Ενδεικτικες λύσεις mini-project
#===================================================
#
# Άσκηση 4.1 Ονόματα & Αριθμός Μητρώου 
#
# Μία απλη λύση είναι η παρακάτω:
#

##di = {}                         # Κατασκευάζω το κενό λεξικο di 
##
##while True:
##    inp = input('ΑΜ, Όνομα (χωρισμένα με κόμμα) / q για Έξοδο: ')
##
##    if inp=='q':                # Ελέγχω πρώτα για q και μετά καλώ split παρακάτω 
##        break
##
##    am, onoma = inp.split(',')  # Αποφεύγω έτσι το πρόβλημα που δημιουργει η split αν δεν δοθούν 2 στοιχεία στην είσοδο
##    am = int(am)                # Μετατρέπω σε int. Θα μπορουσα και σε float 
##    di[am] = onoma              # Ο απλούστερος τροπος να καταχωρήσω ζεύγη δεδομένων σε λεξικό: εντολή ανάθεσης της μορφης Λεξικό[Κλειδί] = Τιμη
##
##for key in sorted(di):          # Η sorted μας δινει μια ταξινομημένη μορφη του λεξικού με βάση τα κλειδιά 
##    print(key, di[key])         # Εμφανίζω τα ζευγη Κλειδί:Τιμή δηλ. key:di[key]


#
#
#=========================================================================================================================
#
#
# Άσκηση 4.2 Λέξεις του Scrabble
#

# Το λεξικό letters έχει ως κλειδιά τα γράμματα της ελληνικής γλωσσας
# και αντιστοιχες τιμές τους πόντους που δίνει καθε γράμμα στο Srabble 

##letters = {'Α':1,'Β':8,'Γ':4,'Δ':4,'Ε':1,'Ζ':10,
##           'Η':1,'Θ':10,'Ι':1,'Κ':2,'Λ':3,'Μ':3,
##           'Ν':1,'Ξ':10,'Ο':1,'Π':2,'Ρ':2,'Σ':1,
##           'Τ':1,'Υ':2,'Φ':8,'Χ':8,'Ψ':10,'Ω':3
##           }
##
##my_words = {}         # Κατασκευάζω το κενό λεξικό my_words για να αποθηκευω τα ζευγη Λέξη:Πόντοι_Λέξης
##
##while True:
##    word = input('Λέξη (ή q για Έξοδο): ')      # Διαβάζω την είσοδο που δίνει ο παικτης...
##
##    if word == 'q':                             # ...και ελέγχω για τιμή 'q'
##        break
##
##    points = 0
##    for ch in word:                     # Στο βροχο αυτό ο επαναλήπτης ch παίρνει ως τιμές το ένα μετά το άλλο τα γράμματα που αποτελούν τη λέξη που δόθηκε ως είσοδος
##        points += letters[ch]           # Ο αθροιστης points αθροίζει καθε φορά τους πόντους που αντιστοιχούν στο γράμμα ch 
##
##    print('Βαθμοί Λέξης:',points)       # Εμφανίζουμε τους πόντους της λέξης
##
##    my_words[word] = points             # Καταχωρούμε στο λεξικο my_words το ζευγάρι word:points
##
##for key in sorted(my_words):            # Καλούμε τη sorted για ταξινόμηση με βάση τα λειδιά, δηλ. τις λεξεις
##    print(key, my_words[key])           # Εμφανίζουμε τα ζευγη Κλειδί:Τιμή δηλ. key:my_words[key]  
##        



# ΣΧΟΛΙΑ

# Προσέξτε την απλοτητα της Python στο βρόχο:

##    for ch in word:
##        points += letters[ch]

# Γράφοντας: for ch in word
# 'σαρώνω' σε ένα βρόχο όλους τους χαρακτήρες (γράμματα) της λέξης word χωρίς να χρειάζομαι κάποιον άλλο δεικτη επανάληψης
# Στη συνέχεια βάζοντας ως κλειδί τον χαρακτηρα ch στο λεξικο letters έχω την τιμή, δηλ. τους πόντους που δίνει αυτό το γράμμα
# ώστε να υπολογίσω το άθροισμα όλων των πόντων στον αθροιστη points
#
  



