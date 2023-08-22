from tkinter import*
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox

# BMI_result =''
def ADVICE_PAGE(BMI_result):
    advice = Tk()
    advice.geometry("1600x800+0+0")
    advice.title("Fitness Application")

    Tops = Frame(advice, width = 1600,height = 20)
    Tops.pack(side=TOP)

    # f0 = Frame(advice, width = 800,height = 200, relief=SUNKEN)
    # f0.pack(side=TOP)
    f1 = Frame(advice, width = 800,height = 700, relief=SUNKEN)
    f1.pack(side=TOP)

    lblInfo = Label(Tops, font=('arial',50,'bold'),text="OUR ADVICE\n",fg="Dark Blue", bd=5, anchor='w')
    lblInfo.grid(row=0,column=1)

    def ExitC():
        exit = 1
        advice.destroy()
    
    diet_text = ''
    nut_text = ''
    Exe_text = ''
    # print(BMI_result)

    if(BMI_result == 'Underweight'):
        diet_text = """Breakfast (8:00-8:30AM)	3 paneer stuffed besan cheela + green chutney + 1 cup curd + 3 cashews + 4 almonds + 2 walnuts
                       Mid-Meal (11:00-11:30AM)	1 apple smoothie with maple syrup
                        Lunch (2:00-2:30PM)	1 cup masoor dal + 1 cup calocasia + 3 chapatti + 1/2 cup rice + 1 cup low curd + salad
                        Evening (4:00-4:30PM)	1 cup tomato soup with bread crumbs + 1 cup aloo chaat
                        Dinner (8:00-8:30PM)	1 cup carrot peas vegetable +3 chapatti + salad"""
        nut_text = """1.	Homemade protein smoothies. Drinking homemade protein smoothies can be a highly nutritious and quick way to gain weight. ...
                      2.	Milk. ...
                      3.	Rice. ...
                      4.	Nuts and nut butters. ...
                      5.	Red meats. ...
                      6.	Potatoes and starches. ...
                      7.	Salmon and oily fish. ...
                      8.	Protein supplements."""
        Exe_text = """1. Pushups
                      2. Bench press
                      3. Pullups
                      4. Squats
                      5. Lunges
                      6. Deadlift"""
    elif(BMI_result == 'Normal'):
        diet_text = """Breakfast (310 calories)
                        3/4 cup oatmeal cooked in 1 1/2 cup water
                        1/3 cup raspberries
                        Top oatmeal with raspberries and a pinch of cinnamon.

                        A.M. Snack (95 calories)
                        1 medium apple
                        Lunch (345 calories)
                        1 serving Whole-Wheat Veggie Wrap
                        P.M. Snack (80 calories)
                        1/2 cup nonfat plain Greek yogurt
                        1/4 cup sliced strawberries
                        Dinner (394 calories)
                        1 serving Mushroom-Quinoa Veggie Burgers with Special Sauce"""
        nut_text = """A healthy diet includes the following: Fruit, vegetables, legumes (e.g. lentils and beans),
                      nuts and whole grains (e.g. unprocessed maize, millet, oats, wheat and brown rice).
                      At least 400 g (i.e. five portions) of fruit and vegetables per day (2), excluding potatoes,
                      sweet potatoes, cassava and other starchy roots."""
        Exe_text = """1. Walking
                      2. Squats
                      3. Interval Training
                      4. Lunges
                      5.Pushups"""
    else:
        diet_text = """Breakfast (8:00-8:30AM)	1 cucmber hungcurd sandwich + 1/2 tsp green chutney + 1 orange
                        Mid-Meal (11:00-11:30AM)	1 cup buttermilk
                        Lunch (2:00-2:30PM)	1 cup white chana/ fish curry + 1 chapatti + salad
                        Evening (4:00-4:30PM)	1 cup low fat milk (no sugar)
                        Dinner (8:00-8:30PM)	1 cup cauliflower vegetable + 1 chapatti + salad"""
        nut_text = """Choose minimally processed, whole foods-whole grains, vegetables, fruits, nuts, healthful sources of protein (fish, poultry, beans),
                      and plant oils. Limit sugared beverages, refined grains, potatoes, red and processed meats, and other highly processed foods, such as fast food."""
        Exe_text = """1. Walking
                      2. Jogging
                      3. Swimming
                      4. Cycling
                      5. Weight training"""

    lbl1 = Label(f1, font=('arial',25,'bold'),text="Diet\n",fg="Dark Blue", bd=5, anchor='w')
    lbl1.grid(row=0,column=1)

    DietInfo = Label(f1, font=('arial',12,'bold'),text=diet_text,fg="Dark Blue", bd=5, anchor='w')
    DietInfo.grid(row=2,column=1)
    
    lbl2 = Label(f1, font=('arial',25,'bold'),text="Nutrition\n",fg="Dark Blue", bd=5, anchor='w')
    lbl2.grid(row=4,column=1)

    nutInfo = Label(f1, font=('arial',12,'bold'),text=nut_text,fg="Dark Blue", bd=5, anchor='w')
    nutInfo.grid(row=6,column=1)
    
    lbl3 = Label(f1, font=('arial',25,'bold'),text="Exercise\n",fg="Dark Blue", bd=5, anchor='w')
    lbl3.grid(row=8,column=1)

    ExeInfo = Label(f1, font=('arial',12,'bold'),text=Exe_text,fg="Dark Blue", bd=5, anchor='w')
    ExeInfo.grid(row=10,column=1)
    
    btnExit=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
                text="Close", bg="orange",command = ExitC).grid(row=12,column=3)

    advice.mainloop()


# while(True):
    # exit = 0

home = Tk()
home.geometry("1600x800+0+0")
home.title("Fitness Application")

Tops = Frame(home, width = 1600,height = 50)
Tops.pack(side=TOP)

f0 = Frame(home, width = 800,height = 200, relief=SUNKEN)
f0.pack(side=TOP)
f1 = Frame(home, width = 800,height = 500, relief=SUNKEN)
f1.pack(side=TOP)


lblInfo = Label(Tops, font=('arial',50,'bold'),text="Please Enter your Details:\n",fg="Dark Blue", bd=5, anchor='w')
lblInfo.grid(row=0,column=0)

weight_var = StringVar()
height_var = StringVar()

def Submit():
 
    weight=int(weight_var.get())
    height=float(height_var.get())

    BMI = weight/(height*height)

    BMI_result = ''
    if(BMI <= 18.5):
        BMI_result= "Underweight"
    elif(BMI <= 25):
        BMI_result= "Normal"
    elif(BMI < 30):
        BMI_result= "Overweight"
    else:
        BMI_result = "Obese,Start losing wait please"


    messagebox.showinfo("Your BMI", "Your weight is " + str(weight) + "kg, your height is " + str(height) + "m and your BMI is " + str(BMI) + " and you are " + BMI_result + ".")

    home.destroy()
    ADVICE_PAGE(BMI_result)




   
# def Advice():
#     home.destroy()
#     ADVICE_PAGE()
    

def ExitC():
    exit = 1
    home.destroy()

weight_label = Label(f0, text = 'Weight(kg)', font=('calibre',10, 'bold'), fg="Dark Blue", bd=5)
  
weight_entry = Entry(f0, textvariable = weight_var, font=('calibre',10,'normal'), fg="Dark Blue", bd=5)

height_label = Label(f0, text = 'Height(m+6)', font=('calibre',10, 'bold'), fg="Dark Blue", bd=5)
  
height_entry = Entry(f0, textvariable = height_var, font=('calibre',10,'normal'), fg="Dark Blue", bd=5)  

# sub_btn=Button(f1,text = 'Submit', command = submit)

weight_label.grid(row=0,column=0)
weight_entry.grid(row=0,column=1)
height_label.grid(row=1,column=0)
height_entry.grid(row=1,column=1)
# sub_btn.grid(row=2)


# Weight = simpledialog.askstring("Weight","Enter Your Weight", parent = home)
# Height = simpledialog.askstring("Height","Enter Your Height", parent = home)
btnSubmit=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=25,
                text="Find BMI and get our advice!", bg="orange",command = Submit).grid(row=7,column=3)

# btnadvice=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
#                 text="Get Advice", bg="orange",command = Advice).grid(row=9,column=3)

btnExit=Button(f1,padx=16,pady=8, bd=16, fg="black",font=('arial',16,'bold'),width=10,
                text="Close", bg="orange",command = ExitC).grid(row=11,column=3)

home.mainloop()
    # if(exit == 1):
    #     break