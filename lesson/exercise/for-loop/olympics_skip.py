for year in range(1900, 2030, 4):
    # The Olympics were skipped during WWI and WWII .
    if year == 1916 or year == 1940 or year == 1944:
        print(str(year) + " (CANCELLED)")
    else:
        print(str(year) + " Summer Olympics")
        
        