"""Chapter : 2 - item : 4 - nong saimai
 ส่งมาแล้ว 1 ครั้ง
หาค่าฐานของอายุของน้องสายไหม ที่อายุ 20,21 ตลอดกาล

เช่น

hbd(65) = "saimai is just 21, in base 32!"

hdb(21) = "saimai is just 21, in base 10!"

hdb(8888) = "saimai is just 20, in base 4444!"

def hbd(age):

    ### Enter Your Code Here ###

year = input("Enter year : ")

print(hbd(int(year)))"""
def hbd(age):
    k =""
    if age %2==0:
        k+="saimai is just 20, in base " 
        k+=str(age//2)
        k+="!"
    elif age %2==1:
        k+="saimai is just 21, in base " 
        k+=str(age//2)
        k+="!"
    return k

year = input("Enter year : ")

print(hbd(int(year)))