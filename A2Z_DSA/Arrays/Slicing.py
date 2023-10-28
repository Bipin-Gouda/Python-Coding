# slicing, slicing in 2d list , df same only in df we use iloc

ls=['a','b','c','d','e','f','g','h']
print(ls[1:5])    # slicing[:]

# for 2d, dataframe, arrays
ls2=[['a','b','c','d','m','n','o','p'],               #    df3=df.iloc[1:16][:]   row  col
     ['e','f','g','h','i','j','k','l']]               #    df3.columns=df3.iloc[0]   0th row
print(ls2[0])
print(ls2[0][1:5]) 
print(ls2[0:5]) # 0 to 5th row but we hv only 2 so prints 2 rows
print(ls2[1:5]) # 1 to 5th row but we hv only 1 so prints 1 row as 0th row excluded