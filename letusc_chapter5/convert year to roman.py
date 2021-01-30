def convert_year(year):
    while year>0:
        if year>=1000:
            print("m",end='')
            year=year-1000
        elif year>=500:
            print("d",end='')
            year=year-500
        elif year>=100:
            print("c",end='')
            year=year-100
        elif year>=50:
            print("l",end='')
            year=year-50
        elif year>=10:
            print("x",end='')
            year=year-10
        elif year>=5:
            print("v",end='')
            year=year-5
        elif year>=1:
            print("i",end='')
            year=year-1
convert_year(2020)
