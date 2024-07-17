
# define the function
def weekly_paycheck(num_hours):
    # calculate the pay_pretax
    pay_pretax = num_hours*15
    #calculate the pay_aftertax
    pay_aftertax = pay_pretax * (1-.12)
    return pay_aftertax
salary_apo = weekly_paycheck(40)
print(salary_apo)
salary_phed = weekly_paycheck(50)
print(salary_phed)

# define the fonction 
def lab_incomes_with_more_inputs(num_hours,hourly_wage, tax_bracket):
    #calculate the pay_pretax
    pay_pretax = num_hours*hourly_wage
    #calculate the pay_aftertax
    pay_aftertax = pay_pretax * (1-tax_bracket)
    return pay_aftertax
salary_apo = lab_incomes_with_more_inputs(40,24,.22)
print(salary_apo)
# define  the function with no arguments
def original_log():
    print("This is the original log")
    print("It is very boring")
    print("nobody knows why it exists")
    return
original_log()

# define the function with two arguments
def get_expected_cost(num_beds, num_baths):
    #calculate the cost of the house
    if num_beds == 0 and num_baths ==0:
        house_cost = 80000
    else:
        house_cost = 80000 + 30000*num_beds + 10000*num_baths
    return house_cost
villa = get_expected_cost(1,1) 
print(villa)   
villa = get_expected_cost(2,1)
print(villa)
villa = get_expected_cost(2,6)
print(villa)  
# define the function with more than two arguments
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    #calculate the cost of the paint
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = total_sqft/sqft_per_gallon
    cost = gallons_needed * cost_per_gallon
    return cost
the_cost = get_cost(120, 5, 220, 24)
print(the_cost)
project_cost = get_cost(432, 144, 400, 15)
print(project_cost)
# define the particular function 
def get_actual_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    #calculate the cost of the paint
    total_sqft = sqft_walls + sqft_ceiling
    gallons_needed = round(total_sqft/sqft_per_gallon)
    cost = gallons_needed * cost_per_gallon
    return cost
the_cost = get_actual_cost(120, 5, 220, 24)
print(the_cost)
project_cost = get_actual_cost(432, 144, 400, 15)
print(project_cost)
low_cost = get_actual_cost(12, .5, 22, 4)
print(low_cost)
high_cost = get_actual_cost(120009, 5050, 4570, 870)
print(high_cost)
# introduction to data types
# integer : numbers without decimal points
x = 12
print(x)
print(type(x))

# float : numbers with decimal points
y = 12.9
print(y)
print(type(y))
import numpy as np
print(np.pi)
almost_pi =22/7
print(almost_pi)
print(type(almost_pi))
y_a = 14.
y_b = .31
print(y_a)
print(y_b)  
print(type(y_a))
print(type(y_b))

# the round function : it lets you round a number to the nearest whole number
yy = 22/7
rounded_yy = round(yy,6)
print(rounded_yy)

# Booleans : True or False
z_a = True
z_b = False
z_c = (12<13)
Z_d = (2==3)
print(z_a)
print(z_b)
print(z_c)
print(Z_d)
print(type(z_a))
print(type(z_b))
print(type(z_c))
print(type(Z_d))

# we can switch the value of a bolean by using "not". So if x is True, then not x is False
z_e = not Z_d
print(z_e)
print(type(z_e))

# Strings : sequence of characters. they are commonly used to represent text
work = "I am a data scientist"
print(work)
print(type(work))

# with len() function, we can get the length of a string
print(len(work))
shortest_string = ""
print(len(shortest_string))

# note that if you put a number in quotes, it becomes a string
the_number = "129"
print(the_number)
print(type(the_number))

# the float() function converts a string that is convertible to a float
float_the_number = float(the_number)
print(float_the_number)
print(type(float_the_number))

# the int() function converts a string that is convertible to an integer
int_the_number = int(the_number)
print(int_the_number)
print(type(int_the_number))

# just like you can add two numbers, you can also add two strings
top_matter = "lazy" + " " + "Data scientist"
print(top_matter)
print(type(top_matter))

# you can also multiply a string by an integer
one_word = "data " * 5
print(one_word)

# what will happen if you multiply a boolean by any of the other data types?
print(False * 10)
print(True * (2.3))
print(False * (2.3))
print(True * "data")
print(False * (-4.5))
print(True * "true")
print(False * "true")
print(False * "love")
print(type(False * "true"))
print(len(False * "true"))

# we can logically see that True is equivalent to 1 and False is equivalent to 0
# define the function 
def get_expected_cost(beds, baths, has_basement):
    if beds == 0 and baths == 0 and has_basement == False:
        house_cost = 80000
    else:
        house_cost = 80000 + 30000*beds + 10000*baths + 40000*has_basement
    return house_cost
villa = get_expected_cost(1,1, True)
print(villa)
villa = get_expected_cost(20,13, False)
print(villa)    
# define the function
def cost_of_project(engraving, solid_gold):
    if engraving == False and solid_gold == False:
        the_cost = 50
    elif engraving == False and solid_gold == True:
        the_cost = 100
    elif engraving == True and solid_gold ==False:
        the_cost = 50 + 7*len(engraving)
    else:
        the_cost = 100 + 10*len(engraving)
    return the_cost
my_cost = cost_of_project("I love data", True)
print(my_cost)
my_cost = cost_of_project("passionate data scientist", False)   
print(my_cost) 
my_cost = cost_of_project("08/10/2000", False)
print(my_cost)



# define the function that performs an  action that depends on th input
def add_three_or_eight(input_num):
    if input_num < 10:
        output_num = input_num + 3
    else:
        output_num = input_num + 8
    return output_num
print(add_three_or_eight(51))
piece = add_three_or_eight(1)
print(piece)    

# conditions and contional statements
print(11<12)
print(2>3)
the_one = 4
the_two = 12
print(the_one > the_two)
print(the_one<the_two)
print(the_one == the_two)
print(the_one != the_two)
print(the_one >= 3)

# define the function
def evaluate_temp(T):
    #check if the temperature is too high or too low
    if T > 38:
        message = "the temperature is too high"
    else:
        message = "the temperature is correct"
    return message
print(evaluate_temp(43))
print(evaluate_temp(27))

# other ways
def evaluate_temp(T):
    #initial message
    message = "the temperature is correct"
    #update value of message
    if T > 38:
        message = "Alert: fever!"
    return message
print(evaluate_temp(36))
print(evaluate_temp(39))

# define the function
def evaluate_temp_with_elif(T):
    if T > 38:
        message = "Alert: fever!"
    elif T > 35:
        message = "Normal temperature"
    else:
        message = "the temperature is too low"
    return message
print(evaluate_temp_with_elif(33))

#define the function
def tax_payment(income):
    if income < 12000:
        tax_payment = income * .25
    else:
        tax_payment = income * .30
    return tax_payment
print(tax_payment(10000))
print(tax_payment(9000))
print(tax_payment(15000))


from datetime import*
# define the  function
def the_best_choice(have_old_doc, the_right_time, the_date):
    #definition of the best
    the_right_time = ((the_right_time >= time(10,00)) and (the_right_time <= time(19,00 )))
    the_date = ((the_date != "friday") and (the_date != "saturday"))
    if have_old_doc == True and the_right_time == True and the_date == True:
        output_choice = "choose the relevant TD"
    elif have_old_doc == False and the_right_time == True and the_date == True:
        output_choice = "approved"
    elif have_old_doc == False and the_right_time == False and the_date == False:
        output_choice = "please it's an unfavourable choice"
    else:
        output_choice = input("is it the only favourable TD on your list?")
        if output_choice == "yes":
            print(f"no choice, you have to go : {the_right_time, the_date}")
        elif output_choice == "no":
            print("Can u update your list?")
        else:
            print("Please try again")
    return output_choice
print(the_best_choice(True, time(12, 00), "monday"))
print(the_best_choice(False, time(12, 30), "saturday"))
print(the_best_choice(False, time(22, 30), "saturday"))
print(the_best_choice(False, time(22, 30), "thursday"))
# define the function
def get_grade(score):  
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade= "C"
    elif score >= 60:
        grade ="D"
    elif score >= 0 and score < 60:  
        grade = "F"
    else:
        grade = "check if the score is correct"
    return grade   
print(get_grade(85))
print(get_grade(49))  
print(get_grade(101))
print(get_grade(0))
print(get_grade(-12))
print(get_grade(4.5))
# define the function
def cost_of_project(engraving, solid_gold):
    if solid_gold ==True:
        cost = ((len(engraving) * 10) + 100) 
    else:
        cost = ((len(engraving) * 7) + 50)
    return cost
print(cost_of_project("data is bae", True))
print(cost_of_project("data is sweet", False))
#define the function
def get_water_bill(num_gallons):
   #define the price per 1000 gallons
   price_per_mil = num_gallons/1000
   if num_gallons <= 8000:
        bill = price_per_mil * 5
   elif num_gallons <= 22000:
        bill = price_per_mil * 6
   elif num_gallons <= 30000:
        bill = price_per_mil * 7
   elif num_gallons >= 30001:
        bill = price_per_mil * 10
   return bill 
print(get_water_bill(10000))
print(get_water_bill(25000))
# define the function
def get_phone_bill(gb):
    gb_price = 100 * abs(15 - gb)
    if gb <= 15:
        phone_bill = 100
    else:
        phone_bill = gb_price + 100
    return phone_bill
print(get_phone_bill(10))
print(get_phone_bill(20))
print(get_phone_bill(10.8))
print(get_phone_bill(15.1))
# Data structures: Intro to lists
courses = ["microeconomics", "macroeconomics", "linear algebra", "math", "english", "statistics", "economics", "economic history", "data science", "econometrics", "finance", "accounting", "marketing"]

print(type(courses))
print(len(courses))
print(courses)
print(courses[-6])
print("my favorit course is:", courses[5])
print("i like also:", courses[3])
print("my arsenal:", courses[3:13:2])
print("the first 5 courses:", courses[:5])
print("the last 5 courses:", courses[-5:])
print("courses", courses[:])

# to remove an item from a list with we use : .remove()
courses.remove("microeconomics")
print(courses)
courses.remove("english")
print("the updated list:", courses)

# it is also possibe to add an item to a list with the .append() method
courses.append("algorithms")
print(courses)

# lists are not just for strings, they can also contain numbers
exam_scores =[15, 18, 20, 12, 17, 17, 14, 19, 12, 17, 17, 13]
print(type(exam_scores))
print(exam_scores)
print(len(exam_scores))
print(exam_scores[-2])
print("the best score is:", max(exam_scores))
print("the worst score is:", min(exam_scores))
print("the total score is:", sum(exam_scores))
print("the average score is:", sum(exam_scores)/len(exam_scores))
print("the average score for the first 5 scores is:", sum(exam_scores[:5])/len(exam_scores[:5]))

# list_1
menu = ['stewed meat with onions', 'bean soup', 'risotto with trout and shrimp','fish soup with cream and onion', 'gyro', 'grilled chicken', 'grilled fish', 'grilled beef', 'grilled pork', 'grilled lamb', 'grilled goat', 'grilled rabbit', 'grilled duck', 'grilled turkey', 'grilled chicken', 'grilled fish', 'grilled beef', 'grilled pork', 'grilled lamb', 'grilled goat', 'grilled rabbit', 'grilled duck', 'grilled turkey', 'grilled chicken', 'grilled fish', 'grilled beef', 'grilled pork', 'grilled lamb', 'grilled goat', 'grilled rabbit', 'grilled duck', 'grilled turkey', 'grilled chicken', 'grilled fish', 'grilled beef', 'grilled pork', 'grilled lamb', 'grilled goat', 'grilled rabbit', 'grilled duck', 'grilled turkey', 'grilled chicken', 'grilled fish', 'grilled beef', 'grilled pork', 'grilled lamb', 'grilled goat', 'grilled rabbit', 'grilled duck', 'grilled turkey', 'grilled chicken', 'grilled fish', 'grilled beef', 'grilled pork', 'grilled lamb', 'grilled goat', 'grilled rabbit', 'grilled duck', 'grilled turkey', 'grilled chicken', 'grilled fish', 'grilled beef', 'grilled pork', 'grilled lamb', 'grilled goat', 'grilled rabbit', 'grilled duck', 'grilled turkey', 'grilled chicken', 'grilled fish', 'grilled beef', 'grilled pork', 'grilled lamb', 'grilled goat', 'grilled rabbit', 'grilled duck', 'grilled turkey', 'grilled chicken', 'grilled fish', 'grilled beef', 'grilled pork', 'grilled lamb', 'grilled goat', 'grilled rabbit', 'grilled duck', 'grilled turkey', 'grilled chicken', 'grilled fish', 'grilled beef', 'grilled pork', 'grilled lamb', 'grilled goat', 'grilled rabbit', 'grilled duck', 'grilled turkey', 'grilled chicken', 'grilled fish', 'grilled beef', 'grilled pork', 'grilled lamb', 'grilled goat', 'grilled rabbit', 'grilled duck', 'grilled turkey', 'grilled chicken']
print(type(menu))
print(len(menu))
print(menu)
menu.remove('bean soup')
menu.remove('stewed meat with onions')
menu.append('roasted beet salad')
print(menu)

# list_2
num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,
                 141, 148, 132, 147, 168, 153, 170, 161, 148, 152,
                 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]
print(type(num_customers))
print(len(num_customers))
print("average number of customers who visited in the first seven days:", sum(num_customers[:7])/len(num_customers[:7]))
print("average number of customers who visited in the last seven days:", sum(num_customers[-7:])/len(num_customers[-7:]))
print("the max:", max(num_customers))
print("the min:", min(num_customers))

# Note : the .split() method is used to split a string into a list
road = "all.is.over.you.and.i.time.is.mine.nobody.Knows.tomorrow.Moov.New.Old.size.Querry.Rust.dust.simple.Union.big.deal.things.Yiel.feel"
film = "Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey"
print(road.split("."))
print(film.split(","))

# others
feelings_one = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
feelings_two = [16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

feels_restr_one = [i>=5 for i in feelings_one]
print(feels_restr_one)

#define the function
def percentage_liked(ratings):
    test_ratings = [1, 2, 3, 4, 5]
    l_liked = [i>=4 for i in test_ratings]
    l_percentage = sum(l_liked)/len(l_liked)
    return l_percentage
print(percentage_liked([1, 2, 3, 4, 5, 1, 5, 4, 2, 3, 1, 2]))
