studgrade={"Kevin":78,"Muhire":32,"Kassim":89,"Kendrick":42}
for e in studgrade:
    if studgrade.get(e)>50:
        print(e)
studgrade["Kevin"]=70
studgrade.pop("Kassim")
print(studgrade)
