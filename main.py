import Imports.gradeService


# print("Lecture One");
cost=10;
tax_percent=0.25;
tax=cost*tax_percent;
price=cost+tax;

# print(price);

username="Testing program";
firstName="Testing";
# print(firstName +"" +username);

firstNum=10;
secondNum=20;
# print(firstNum + secondNum);

firstName="Eric";
# print(firstName +"" +"hi");
# print(f"Hi{firstName}");

# sentence="Hi {} {}";
# last_name="Roby";
# print(sentence.format(firstName,last_name));
#
# print(f"Hi {firstName} {last_name} I hope you are learning");


# firstName=input("Enter your first name");
# days=input("How many days before your  birthday!");
# print(f"Hi {firstName} only {days} before  your birthday!");

# days=int(input("How many days before your  birthday!"));
# print(type(days));
# print(round(days/7,2));

#
# List are a collection of data

my_list=[1,2,3,4,5,6,7,8,9,10];
# print(type(my_list));
# print(my_list);
# print(my_list[0])

people_list=["Eric","Adil","jeff"];
people_list.append("Teisng sam");
people_list.insert(1,"max shri");
people_list[0]="Erivyest";
people_list.remove("Adil");
people_list.pop(0);
# print(people_list);
# print((people_list));
# print(people_list[0]);
# print(people_list[-1]);
people_list.sort();
# print(people_list);

# print(len(people_list));
# print(people_list[0:2]);
#
# Set are similar to Lists but are unordered and cannot contain duplications Use  curley brackets

# my_set={1,2,3,4,5,6,7,8,9,10};
# print(my_set);
# print(len(my_set));
# print ("TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT")
# # for  x in my_set:
#     # print(x);
#
# my_set.discard(3);
# print(my_set);
# my_set.clear();
# print(my_set);
# my_set.add(99);
# print(my_set);
# my_set.update([0,999]);
# print(my_set);

# my_tuple=(1,2,3,4,5,6,7,8,9,10);
# print(len(my_tuple));
# print(my_tuple[1]);

# Boolean and  Operators

# like_coffee=True;
# like_tea=False;
# print(like_coffee);
# print(like_tea);
# favourite_food="Pizaa";
# favourite_number=32;
# print(type(like_coffee));
# print(type(like_tea));
# print(type(favourite_food));

#print(1==2);
#print(1!=2);
#print(1>2);
x=1
#if x>1:
   # print("x is 1");
#else:
   # print("x is not greater  than 1")
#print("outside of  if statement");

hour=16
if hour<15:
    print("hour is less than 15")
elif hour<30:
    print("hour is less than 30")
else:
    print("Good afternoon")

#IF  ELSE  IN PYTHON
grade=20
if grade >=90:
    print("A")
elif 80<=grade <90:
    print("B")
elif 70<=grade<80:
    print("C")
elif 60<=grade<70:
    print("D")
else:
    print("F")


#LOOPS  IN Python

my_list=[1,2,3,4,5,6,7,8,9,10];
sum_of_for_loop=0
for x in my_list:
    sum_of_for_loop +=x
print(sum_of_for_loop)


#for x in range(1,7):
   # print(x)

my_list=["Monday","Tuesday","Wednesday","Thursday","Friday"]
for x in  my_list:
    print(x)


i=0
while i<5:
    i+=1
    if i==3:
        break
    print(i)
else:
    print("good")

#Dictionaries  in python

user_dictionary={
    'username':'Testing',
    'firstName':'Testing',
    'firstNum':10,
}

user_dictionary["maarried"]=True
print(user_dictionary)
print(user_dictionary.get('username'))
print(len(user_dictionary))
print(user_dictionary.get('firstName'))
user_dictionary.pop("firstNum")
print(user_dictionary)
#user_dictionary.clear()
print(user_dictionary)



for  x,y in user_dictionary.items():
    print(x,y)

user_dictionary2=user_dictionary.copy()
user_dictionary2.pop("username")
print(user_dictionary)

###########################################################################################
#function in python



def my_function():
    print("Hello welcome  to function!")
my_function()


def print_my_name(FirstName,lastName):
    print(f"Hello {FirstName} {lastName}!")

print_my_name("shrikant","Mahajan")


def print_numbers(highest_number,lowest_Number):
    print(highest_number)
    print(lowest_Number)

print_numbers(23,67)

def multiply_numbers(a,b):
    return a*b

print(multiply_numbers(2,6))

#########################################Calling function inside  function ##############
def buy_item(cost_of_item):
    return  cost_of_item+add_tax_to_item(cost_of_item)


def add_tax_to_item(cost_of_item):
    current_tax_rate=.03
    return cost_of_item *current_tax_rate

final_cost=buy_item(50)
print(final_cost)

def user_dictionary(firstname, lastName,age):
    created_user_dictionary={
        'firstName':firstname,
        'lastName':lastName,
        'ahe':age
    }
    return created_user_dictionary

solution_dictionary=user_dictionary(firstname="Shrikant",lastName="Mahajan",age="20")
print(solution_dictionary)

#######################################Imports in python #######################################################

homework_assignement_grades={
    'homework_1':85,
    'homework_2':90,
    'homework_3':90,
}

Imports.gradeService.calculate_homework_grade(homework_assignement_grades)


###Standard Library Comes with Python Useful methods ########################

#Random
import random
import  math

square_root=math.sqrt(64)
print(square_root)

types_of_drinks=['soda','coffee','Water','Tea']
print(random.choice(types_of_drinks))

print(random.randint(1,10))




