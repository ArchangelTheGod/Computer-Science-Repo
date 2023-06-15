#Name: Archangel (Azel)
#Date: 7/6/23
#File Name: 4.02.py
#Description: Displays a KPH to MPH table

#loop
print("MPH\tKPH\n__________________")
for limitkmh in range(60, 131, 10):
    converted = limitkmh * 0.6214
    print(f"{converted:0.0f}\t{limitkmh}")
    if limitkmh == 130:
        print("___________________")
        print("<-- YO -->")