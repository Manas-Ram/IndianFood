biryani=[140, 18.6, 4.5, 5.5, 298]
samosa=[308, 32.2, 17.9, 4.7, 819]
dosa=[489, 82.3, 11.2, 14.6, 884]
uttapam=[92, 14.2, 2.8, 17.9, 7]
idli=[33, 7.2, .1, 1, 1.1]
basmati=[148, 32.4, 0, 3.5, 0]
def get_nut_value(food, quantity): 
    print(food)
    if food.lower() == "chicken biryani": 
        return "Calories " + str(int(quantity)*biryani[0])  + " Carbs " + str(int(quantity)*biryani[1]) + " Fats " + str(int(quantity)*biryani[2]) + " Protein " + str(int(quantity)*biryani[3]) + " Sodium " + str(int(quantity)*biryani[4])
        #print("Calories " + int(quantity)*biryani(0)  + "Carbs " + int(quantity)*biryani(1) + "Fats " + int(quantity)*biryani(2) + "Protein " + int(quantity)*biryani(3) + "Sodium " + int(quantity)*biryani(4))
    elif food.lower() == "samosa":
        return "Calories " + str(int(quantity)*samosa[0])  + " Carbs " + str(int(quantity)*samosa[1]) + " Fats " + str(int(quantity)*samosa[2]) + " Protein " + str(int(quantity)*samosa[3]) + " Sodium " + str(int(quantity)*samosa[4])
    elif food.lower()=="dosa":
        return "Calories " + str(int(quantity)*dosa[0])  + " Carbs " + str(int(quantity)*dosa[1]) + " Fats " + str(int(quantity)*dosa[2]) + " Protein " + str(int(quantity)*dosa[3]) + " Sodium " + str(int(quantity)*dosa[4])
    elif food.lower()=="uttapam":
        return "Calories " + str(int(quantity)*uttapam[0])  + " Carbs " + str(int(quantity)*uttapam[1]) + " Fats " + str(int(quantity)*uttapam[2]) + " Protein " + str(int(quantity)*uttapam[3]) + " Sodium " + str(int(quantity)*uttapam[4])
    elif food.lower()=="idli":
        return "Calories " + str(int(quantity)*idli[0])  + " Carbs " + str(int(quantity)*idli[1]) + " Fats " + str(int(quantity)*idli[2]) + " Protein " + str(int(quantity)*idli[3]) + " Sodium " + str(int(quantity)*idli[4])
    elif food.lower()=="basmati rice":
        return "Calories " + str(int(quantity)*basmati[0])  + " Carbs " + str(int(quantity)*basmati[1]) + " Fats " + str(int(quantity)*basmati[2]) + " Protein " + str(int(quantity)*basmati[3]) + " Sodium " + str(int(quantity)*basmati[4])
    else:
        return "SYNTAX ERROR: I'm sorry this version of IndCalc does not support this, try again"