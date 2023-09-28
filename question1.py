N=str(input("Enter any sentence: "))
vowel="AEIOUaeiou"
count=0
nv_count=0
space=0
for char in N:
    if char in vowel:
        count+=1
    if char not in vowel:
        nv_count+=1
    if char in " ":
        space+=1
print("The total vowels are: ",count)
print("The total nonvowels are: ",nv_count)
print("The total Words are: ",space+1)