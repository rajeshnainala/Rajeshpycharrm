population=80000
men=(52/100)*80000
women=population-men
literate_persons=(48/100)*80000
literate_men=(35/100)*80000
literate_women=literate_persons-literate_men
illiterate_men=men-literate_men
illiterate_women=women-literate_women
total_illiterate=illiterate_men+illiterate_women

print("Number of Men who are illiterate :",illiterate_men)
print("Number of Women who are illiterate: ",illiterate_women)
print("Total No of illiterate are: ",total_illiterate)

#Cost price of single unit
sellingprice_15=int(input("Enter the selling price for 15 units "))
profit_15=int(input("Enter the value of profit for 15 items"))
costprice_15=sellingprice_15-profit_15
costprice_singleunit=costprice_15/15
print("cost price of a single unitis :",round(costprice_singleunit,2))

