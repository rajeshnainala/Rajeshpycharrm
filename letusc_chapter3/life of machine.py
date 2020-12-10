life=1
alternative_per_year=int((0.12)*6000)

alternative_investment=0
attractive_investment=0
while alternative_investment>=attractive_investment:
    attractive_investment=0
    alternative_investment=0
    alternative_investment=life*alternative_per_year
    attractive_investment=(life*1000)-4000
    life+=1
print("life of a machine  to get attractive investment more than alternative investmentis ",life,"years")

