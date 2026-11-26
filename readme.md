# Biljettpriskalkylator.

Barn mellan 0 och 12 år betalar 50 kronor.
Besökare mellan 13 och 64 år betalar 100 kronor.
Besökare som är 65 år eller äldre betalar 80 kronor.
Om åldern är ett negativt tal ska programmet ge ett ValueError

# Åtgärder i koden:

Åldrarna beräknades fel i programmet.
 **if age <= 13:**
Ska vara 12. om åldern är mindre eller lika med 12 ska priset vara 50
 **if age < 65:**
ska vara 64 och det fattas ett lika med tecken. Om åldern är mindre eller lika med eller mindre än 64 ska priset vara 100.

La till 
 **if age >= 65:**
för att räkna ut ålder över 65. då den saknades. Om åldern är högre eller lika med 65 är priset 80.

# Åtgärger i test koden:

Bytte ut test koden till:

        (0, 50),
        (11, 50),
        (12, 50),
        (13, 100),
        (64, 100),
        (65, 80),
        (66, 80)

Då de enda värden som är intressanta att beräkna är dessa och det gjordes genom gränsvärdesanalys.
