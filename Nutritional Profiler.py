# Nutritional Profiler - Capstone 3 (Tanish Bhatta)
import time
from colorama import Fore, Style

def get_user_profile():
    try:
        #Print Ask Name
        time.sleep(1)
        print(Fore.LIGHTYELLOW_EX + "1) What is your name?" + Style.RESET_ALL)
        #Name
        name = str(input("-> "))

        #Age
        time.sleep(1)
        age = int(input(Fore.LIGHTYELLOW_EX + "2) Enter your age: " + Style.RESET_ALL))

        time.sleep(1)
        #Print Unit preference for weight
        print(Fore.CYAN + "\nChoose your mass unit preference :-" + Style.RESET_ALL + Fore.MAGENTA + "\n1. Kilogram (kg)\n2. Pound (lb)" + Style.RESET_ALL)
        #Weight list
        w = [["1" , "kilogram"] , ["2" , "pound"]]
        while True:
            w_pref = str(input("-> "))
            #Weight
            if w_pref.lower() in w[0]:
                #Kilogram Preference
                time.sleep(0.5)
                print(Fore.LIGHTYELLOW_EX + "\n3) What is your weight in kilograms?" + Style.RESET_ALL)
                weight_k = float(input("-> "))
                weight = weight_k
                break
            elif w_pref.lower() in w[1]:
                #Pound Preference
                time.sleep(0.5)
                print(Fore.LIGHTYELLOW_EX + "\n3) What is your weight in pounds?" + Style.RESET_ALL)
                weight_p = float(input("-> "))
                weight = weight_p / 2.205
                break
            else: 
                time.sleep(0.5)
                print(Fore.RED + "\nInvalid input." + Style.RESET_ALL)

        time.sleep(1)
        #Print Unit preference for Height
        print(Fore.CYAN + "\nChoose your length unit preference :-" + Style.RESET_ALL + Fore.MAGENTA + "\n1. Centimetre (cm)\n2. Inch (in)\n3. Foot\n4. Foot + Inch" + Style.RESET_ALL)
        #Height list
        h = [["1" , "centimetre"] , ["2" , "inch"] , ["3" , "foot"] , ["4" , "foot + inch"]]
        while True:
            h_pref = str(input("-> "))
            #Height
            if h_pref.lower() in h[0]:
                #Centimetre Preference
                time.sleep(0.5)
                print(Fore.LIGHTYELLOW_EX + "\n3) What is your height in centimetres?" + Style.RESET_ALL)
                height_c = float(input("-> "))
                height = height_c / 100
                break
            elif h_pref.lower() in h[1]:
                #Inch Preference
                time.sleep(0.5)
                print(Fore.LIGHTYELLOW_EX + "\n3) What is your height in inches?" + Style.RESET_ALL)
                height_i1 = float(input("-> "))
                height = height_i1 / 39.37
                break
            elif h_pref.lower() in h[2]:
                #Foot Preference
                time.sleep(0.5)
                print(Fore.LIGHTYELLOW_EX + "\n3) What is your height in feet?" + Style.RESET_ALL)
                height_f1 = float(input("-> "))
                height = height_f1 / 3.281
                break
            elif h_pref.lower() in h[3]:
                #Foot + Inch Preference
                time.sleep(0.5)
                print(Fore.LIGHTYELLOW_EX + "\n3) What is your weight in:" + Style.RESET_ALL)
                height_f2 = float(input(Fore.CYAN + "Feet = " + Style.RESET_ALL))
                height_i2 = float(input(Fore.CYAN + "Inches = " + Style.RESET_ALL))
                height = (height_f2 / 3.281) + (height_i2 / 39.37)
                break

        time.sleep(1)
        #Print Goal Preference
        print(Fore.LIGHTYELLOW_EX + "\n4) Whats your goal :-" + Style.RESET_ALL  + Fore.MAGENTA + "\n1. Weight Gain\n2. Maintainance\n3. Weight Loss" + Style.RESET_ALL)
        #Goal List
        g = [["1" , "weight gain"] , ["2" , "maintainance"] , ["3" , "weight loss"]]
        while True:
            g_pref = str(input("-> "))

            if g_pref.lower() in g[0]:
                goal = 500
                break
            elif g_pref.lower() in g[1]:
                goal = 0
                break
            elif g_pref.lower() in g[2]:
                goal = -500
                break
            else: 
                time.sleep(0.5)
                print(Fore.RED + "\nInvalid input." + Style.RESET_ALL)

        time.sleep(1)
        #Activity Checker
        print(Fore.LIGHTYELLOW_EX + "\n5) How much active are you in a week?  :-" + Style.RESET_ALL  + Fore.MAGENTA + "\n1. (Sedentary): Not at all\n2. (Lightly Active): 1-3 days per week\n3. (Moderately Active): 3-5 days per week\n4. (Very Active): 6-7 days per week\n5. (Extra Active): Almost twice per day" + Style.RESET_ALL)
        #Activity List
        a = [["1" , "sedentary"] , ["2" , "lightly active"] , ["3" , "moderately active"] , ["4" , "very active"] , ["5" , "extra active"]]

        while True:
            a_pref = str(input("-> "))

            if a_pref.lower() in a[0]:
                activity = 1.2
                break
            elif a_pref.lower() in a[1]:
                activity = 1.375
                break
            elif a_pref.lower() in a[2]:
                activity = 1.55
                break
            elif a_pref.lower() in a[3]:
                activity = 1.725
                break
            elif a_pref.lower() in a[4]:
                activity = 1.9
                break
            else: 
                time.sleep(0.5)
                print(Fore.RED + "\nInvalid input." + Style.RESET_ALL)

    except Exception as err:
        print(f"Error: {err}")

    return name , age , weight , height , goal , activity

def bmi_calculator(w , h):
    return w / (h**2)

def bmr_calculator(w , h , a):
    return (10 * w) + (6.25 * h * 100) - (5 * a) + 5

def tdee_calculator(bmr , ac):
    return bmr * ac

def goal_cal_calculator(tdee , g):
    return tdee + g

def water_intake_calculator(w):
    return w * 0.033

# Welcome
print(Fore.LIGHTCYAN_EX + "Welcome to " + Style.RESET_ALL + Fore.RED + "Nutritional Profiler " + Style.RESET_ALL + Fore.LIGHTCYAN_EX + "by Tanish Bhatta" + Style.RESET_ALL)
time.sleep(2)
a = print("A scientific health calculator".center(48, "-") + "\n")

name , age , weight , height , goal , activity = get_user_profile()

bmr = bmr_calculator(weight, height, age)
tdee = tdee_calculator(bmr, activity)
goal_calories = goal_cal_calculator(tdee, goal)
bmi = bmi_calculator(weight, height)

#Processing
time.sleep(0.5)
print(Fore.LIGHTCYAN_EX + "\nProcessing user data..." + Style.RESET_ALL)
time.sleep(1)
print("\nCalculating BMI...")
time.sleep(1.5)
print("Calculating BMR...")
time.sleep(1.1)
print("Syncing data...")
time.sleep(1.8)
print("Calculating goal calories...")
time.sleep(0.6)
print("Combining data...")
time.sleep(0.5)
print("Loading...\n")
time.sleep(2.5)

##Layout
print(Fore.LIGHTBLUE_EX + "=" *40 + Style.RESET_ALL)
print()
print(Fore.LIGHTYELLOW_EX + "Nutritional Profile".center(80, " ") + Style.RESET_ALL)
print(Fore.CYAN + "\nName: " + Style.RESET_ALL + Fore.LIGHTMAGENTA_EX + name + Style.RESET_ALL)
print(Fore.CYAN + "Age: " + Style.RESET_ALL + Fore.LIGHTMAGENTA_EX + str(age) + Style.RESET_ALL)
print(Fore.CYAN + "Weight: " + Style.RESET_ALL + Fore.LIGHTMAGENTA_EX + str(weight) + Style.RESET_ALL)
#Inside
print(Fore.LIGHTRED_EX + "\nHealth and Fitness Metrics :-\n" )
#BMI
time.sleep(2.5)
print("Fetching data...")
time.sleep(3)
if bmi >= 30:
    print(Fore.LIGHTCYAN_EX + "Body Mass Index (BMI): " + Style.RESET_ALL + Fore.RED + f"{round(bmi, 2)} (Obese)" + Style.RESET_ALL )
elif 25 < bmi < 30:
    print(Fore.LIGHTCYAN_EX + "Body Mass Index (BMI): " + Style.RESET_ALL + Fore.LIGHTRED_EX + f"{round(bmi, 2)} kg/m² (Overweight)" + Style.RESET_ALL )
elif 18.5 <= bmi <= 25:
    print(Fore.LIGHTCYAN_EX + "Body Mass Index (BMI): " + Style.RESET_ALL + Fore.GREEN + f"{round(bmi, 2)} kg/m² (Normal)" + Style.RESET_ALL )
elif bmi < 18.5:
    print(Fore.LIGHTCYAN_EX + "Body Mass Index (BMI): " + Style.RESET_ALL + Fore.RED + f"{round(bmi, 2)} kg/m² (Underweight)" + Style.RESET_ALL )

#BMR
print(Fore. LIGHTCYAN_EX + "Basal Metabolic Rate (BMR): " + Style.RESET_ALL + Fore.LIGHTGREEN_EX + f"{round(bmr, 2)} kcal/day" + Style.RESET_ALL)

#TDEE
print(Fore. LIGHTCYAN_EX + "Total Daily Metabolic Expenditure (TDEE): " + Style.RESET_ALL + Fore.LIGHTGREEN_EX + f"{round(tdee, 2)} kcal/day" + Style.RESET_ALL)

if goal == -500:
    print(Fore.LIGHTMAGENTA_EX + "In order to lose weight, you should consume " + Style.RESET_ALL + Fore.GREEN + str(round(goal_calories, 2)) + Style.RESET_ALL + Fore.LIGHTMAGENTA_EX +  " kcal per day." + Style.RESET_ALL )
elif goal == 0:
    print(Fore.LIGHTMAGENTA_EX + "In order to maintain weight, you should consume " + Style.RESET_ALL + Fore.GREEN + str(round(goal_calories, 2)) + Style.RESET_ALL + Fore.LIGHTMAGENTA_EX +  " kcal per day." + Style.RESET_ALL )
elif goal == 500:
    print(Fore.LIGHTMAGENTA_EX + "In order to gain weight, you should consume " + Style.RESET_ALL + Fore.GREEN + str(round(goal_calories, 2)) + Style.RESET_ALL + Fore.LIGHTMAGENTA_EX +  " kcal per day." + Style.RESET_ALL )

#Diet Plan
time.sleep(2.5)
print("\nCollecting data...")
time.sleep(2)
print("Generating diet plan...")
time.sleep(3)
print(Fore.LIGHTRED_EX + "\nStandard Balanced Diet Split (per day) :-\n" )
print(Fore.LIGHTMAGENTA_EX + "Protein: " + Style.RESET_ALL + Fore.GREEN + f"{round((goal_calories * 0.3), 2) / 4} g" + Style.RESET_ALL)
print(Fore.LIGHTMAGENTA_EX + "Carbohydrates: " + Style.RESET_ALL + Fore.GREEN + f"{round((goal_calories * 0.35), 2) / 4} g" + Style.RESET_ALL)
print(Fore.LIGHTMAGENTA_EX + "Fats: " + Style.RESET_ALL + Fore.GREEN + f"{round((goal_calories * 0.35 ), 2) / 9} g" + Style.RESET_ALL)
print(Fore.LIGHTMAGENTA_EX + "Water intake: " + Style.RESET_ALL + Fore.GREEN + f"{round(weight * 0.033 , 1)} L" + Style.RESET_ALL)
print()
print(Fore.LIGHTBLUE_EX + "=" *80 + Style.RESET_ALL)
