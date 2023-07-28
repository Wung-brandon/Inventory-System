from tkinter import *
from tkinter import messagebox
import random
import os
import tempfile


root = Tk()
root.title("Inventory Management System")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f'{screen_width}x{screen_height}')
#root.geometry('1270x685')
root.resizable(False, False)

#FUNCTIONALITY PART

#function to calculate total
def total():
    global soap_price,facecream_price,facewash_price,hairgel_price,hairspray_price,bodylotion_price
    global rice_price,oil_price,sugar_price,wheat_price,tea_price,flour_price
    global coca_cola_price,fanta_price,sprite_price,pepsi_price,orangina_price,vimto_price
    global pizza_price,hamburger_price,sandwich_price,onion_ring_price,fried_chicken_price,cheeseburger_price
    global totalbill
    #Cosmestic Price calculation 
    soap_price = int(bathsoapEntry.get())*500
    facecream_price = int(facecreamEntry.get())*5000
    facewash_price = int(facewashEntry.get())*5000
    hairgel_price = int(hairgelEntry.get())*4000
    hairspray_price = int(hairsprayEntry.get())*3000
    bodylotion_price = int(bodylotionEntry.get())*5000
    
    total_Cosmetic_price = soap_price + facecream_price + hairgel_price + bodylotion_price + hairspray_price + facewash_price
    cosmeticprice_labelEntry.delete(0,END)
    cosmeticprice_labelEntry.insert(0,f'{total_Cosmetic_price} Frs ')
    
    #Grocery Price Calculations
    rice_price = int(ricelabelEntry.get())*12500
    oil_price = int(oil_labelEntry.get())*8000
    sugar_price = int(sugarlabelEntry.get())*4000
    wheat_price = int(wheatlabelEntry.get())*3000
    tea_price = int(tealabelEntry.get())*2000
    flour_price = int(flourlabelEntry.get())*4000
    
    total_grocery_price = rice_price + oil_price + sugar_price + wheat_price + tea_price + flour_price
    grocery_price_labelEntry.delete(0,END)
    grocery_price_labelEntry.insert(0,f'{total_grocery_price} Frs')
    
    #Cold Drinks price Calculations
    coca_cola_price = int(coca_cola_labelEntry.get())*500
    fanta_price = int(fantalabelEntry.get())*500
    sprite_price = int(spritelabelEntry.get())*600
    pepsi_price = int(pepsilabelEntry.get())*1000
    orangina_price = int(orangina_labelEntry.get())*500
    vimto_price = int(vimto_labelEntry.get())*500
    
    total_cold_drinks_price = coca_cola_price + fanta_price + sprite_price + pepsi_price + orangina_price + vimto_price
    cold_drinks_price_labelEntry.delete(0,END)
    cold_drinks_price_labelEntry.insert(0,f'{total_cold_drinks_price} Frs')
    
    #Fast food price Calculations
    pizza_price = int(pizzalabelEntry.get())*7000
    hamburger_price = int(hamburger_labelEntry.get())*4000
    sandwich_price = int(sandwich_labelEntry.get())*3000
    onion_ring_price = int(onion_ring_labelEntry.get())*1000
    fried_chicken_price = int(chicken_labelEntry.get())*1000
    cheeseburger_price = int(cheeseburger_labelEntry.get())*1000
    
    total_fast_food_price = pizza_price + hamburger_price + onion_ring_price + sandwich_price + fried_chicken_price + cheeseburger_price
    fast_food_price_labelEntry.delete(0,END)
    fast_food_price_labelEntry.insert(0, f'{total_fast_food_price} Frs')
    
    #Cosmetics tax price calculation
    total_cosmetics_tax_price = round(total_Cosmetic_price*0.06)
    cosmetic_tax_price_labelEntry.delete(0,END)
    cosmetic_tax_price_labelEntry.insert(0, f'{total_cosmetics_tax_price} Frs')
    
    #Grocery tax price calculation
    total_grocery_tax_price = round(total_grocery_price*0.04)
    grocery_tax_price_labelEntry.delete(0,END)
    grocery_tax_price_labelEntry.insert(0,f'{total_grocery_tax_price} Frs')
    
    #Cold drinks tax price calculation
    total_cold_drinks_tax_price = round(total_cold_drinks_price *0.125)
    cold_drinks_tax_price_labelEntry.delete(0,END)
    cold_drinks_tax_price_labelEntry.insert(0,f'{total_cold_drinks_tax_price} Frs')
    
    #Fast food tax price calculation
    total_fast_food_tax_price = round(total_fast_food_price*0.03)
    fast_food_tax_price_labelEntry.delete(0,END)
    fast_food_tax_price_labelEntry.insert(0,f'{total_fast_food_tax_price} Frs')
    
    totalbill = total_Cosmetic_price + total_cold_drinks_price + total_grocery_price + total_fast_food_price + total_cosmetics_tax_price + total_cold_drinks_tax_price + total_grocery_tax_price + total_fast_food_tax_price


#function to search bill number from the bill folder and display it on the textarea
def search_bill():
    for num in os.listdir('bills/'):
        #seperating the bill number and the txt string using the split() method and checking if it matches the number the user 
        #in the bill number entry
        if num.split('.')[0] == billEntry.get():
            file = open(f'bills/{num}','r')
            textarea.delete(1.0,END)
            for data in file:
                textarea.insert(END,data)
            file.close() #break out of loop if the bill number is found in the file
            break  #or use the return statement
    else:
       messagebox.showerror('error', 'Invalid Bill Number')


#checking if the bills folder is not created then we use the os module to create it
if not os.path.exists('bills'):
    os.mkdir('bills')
#function to save bill
def save_bill():
    global billnumber
    if textarea.get(1.0,END) == '\n':
        messagebox.showerror('error','Bill Content is empty')
        return
    
    result = messagebox.askyesno('Confirm','Do you want save the bill?')
    if result:
        bill_content = textarea.get(1.0,END)
        file = open(f'bills/{billnumber}.txt', 'w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Success',f'Bill bumber {billnumber} is Saved Successfully')
        #resetting the bill number so that 2 users dont't have the same bill number
        billnumber = random.randint(1000,3000)

billnumber = random.randint(1000,3000)
#function for the Bill
def bill():
    if nameEntry.get() == '' or phoneEntry.get() == '':
        messagebox.showerror('Error','Customer Details Are Required')
    elif cosmeticprice_labelEntry.get() == '' and grocery_price_labelEntry.get() == '' or cold_drinks_price_labelEntry.get() == '' and fast_food_price_labelEntry == '':
        messagebox.showerror('Error','No Products Are Selected')
    elif cosmeticprice_labelEntry.get() == '0 Frs' and grocery_price_labelEntry.get() == '0 Frs' or fast_food_price_labelEntry.get() == '0 Frs' and cold_drinks_price_labelEntry.get() == '0 Frs':
        messagebox.showerror('Error','No Products Are Selected')  
    else:
        textarea.delete(1.0,END)    
        billEntry.delete(0,END)
        textarea.insert(END,'\t\t**Welcome Customer**')
        textarea.insert(END,f'\n Bill Number: {billnumber}')
        textarea.insert(END,f'\n Customer Name: {nameEntry.get()}')
        textarea.insert(END,f'\n Customer Phone Number: {phoneEntry.get()}')
        textarea.insert(END,f'\n ==========================================')
        textarea.insert(END,"\n Product\t\tQuantity\t\tPrice")
        textarea.insert(END,f'\n ==========================================')
        
        if bathsoapEntry.get() != '0':
            textarea.insert(END,f'\t Bath Soap\t\t{bathsoapEntry.get()}\t\t{soap_price} Frs')
        if facecreamEntry.get() != '0':
            textarea.insert(END,f'\n Face Cream\t\t{facecreamEntry.get()}\t\t{facecream_price} Frs')
        if facewashEntry.get() != '0':
            textarea.insert(END,f'\n Face Wash\t\t{facewashEntry.get()}\t\t{facewash_price} Frs')
        if hairgelEntry.get() != '0':
            textarea.insert(END,f'\n Hair Gel\t\t{hairgelEntry.get()}\t\t{hairgel_price} Frs')
        if hairsprayEntry.get() != '0':
            textarea.insert(END,f'\n Hair Spray\t\t{hairsprayEntry.get()}\t\t{hairspray_price} Frs')
        if bodylotionEntry.get() != '0':
            textarea.insert(END,f'\n Body Lotion\t\t{bodylotionEntry.get()}\t\t{bodylotion_price} Frs')

        if ricelabelEntry.get() != '0':
            textarea.insert(END,f'\n Rice\t\t{ricelabelEntry.get()}\t\t{rice_price} Frs')
        if oil_labelEntry.get() != '0':
            textarea.insert(END,f'\n Oil\t\t{oil_labelEntry.get()}\t\t{oil_price} Frs')
        if sugarlabelEntry.get() != '0':
            textarea.insert(END,f'\n Sugar\t\t{sugarlabelEntry.get()}\t\t{sugar_price} Frs')
        if wheatlabelEntry.get() != '0':
            textarea.insert(END,f'\n Wheat\t\t{wheatlabelEntry.get()}\t\t{wheat_price} Frs')
        if tealabelEntry.get() != '0':
            textarea.insert(END,f'\n Tea\t\t{tealabelEntry.get()}\t\t{tea_price} Frs')
        if flourlabelEntry.get() != '0':
            textarea.insert(END,f'\n Flour\t\t{flourlabelEntry.get()}\t\t{flour_price} Frs')
            
        if coca_cola_labelEntry.get() != '0':
            textarea.insert(END,f'\n Coca Cola\t\t{coca_cola_labelEntry.get()}\t\t{coca_cola_price} Frs')
        if fantalabelEntry.get() != '0':
            textarea.insert(END,f'\n Fanta\t\t{fantalabelEntry.get()}\t\t{fanta_price} Frs')
        if spritelabelEntry.get() != '0':
            textarea.insert(END,f'\n Sprite\t\t{spritelabelEntry.get()}\t\t{sprite_price} Frs')
        if pepsilabelEntry.get() != '0':
            textarea.insert(END,f'\n Pepsi\t\t{pepsilabelEntry.get()}\t\t{pepsi_price} Frs')
        if orangina_labelEntry.get() != '0':
            textarea.insert(END,f'\n Orangina\t\t{orangina_labelEntry.get()}\t\t{orangina_price} Frs')
        if vimto_labelEntry.get() != '0':
            textarea.insert(END,f'\n Vimto\t\t{vimto_labelEntry.get()}\t\t{vimto_price} Frs')
            
        if pizzalabelEntry.get() != '0':
            textarea.insert(END,f'\n Pizza\t\t{pizzalabelEntry.get()}\t\t{pizza_price} Frs')
        if hamburger_labelEntry.get() != '0':
            textarea.insert(END,f'\n Hamburger\t\t{hamburger_labelEntry.get()}\t\t{hamburger_price} Frs')
        if sandwich_labelEntry.get() != '0':
            textarea.insert(END,f'\n Sandwich\t\t{sandwich_labelEntry.get()}\t\t{sandwich_price} Frs')
        if onion_ring_labelEntry.get() != '0':
            textarea.insert(END,f'\n Onion Rings\t\t{onion_ring_labelEntry.get()}\t\t{onion_ring_price} Frs')
        if chicken_labelEntry.get() != '0':
            textarea.insert(END,f'\n Fried Chicken\t\t{chicken_labelEntry.get()}\t\t{fried_chicken_price} Frs')
        if cheeseburger_labelEntry.get() != '0':
            textarea.insert(END,f'\n Cheeseburger\t\t{cheeseburger_labelEntry.get()}\t\t{cheeseburger_price} Frs')
            
        textarea.insert(END,f'\n ------------------------------------------')
        
        if cosmetic_tax_price_labelEntry.get() != '0 Frs':
            textarea.insert(END,f'\n Cosmetic Tax Price\t\t\t{cosmetic_tax_price_labelEntry.get()}')
        if grocery_tax_price_labelEntry.get() != '0 Frs':
            textarea.insert(END,f'\n Grocery Tax Price\t\t\t{grocery_tax_price_labelEntry.get()}')
        if cold_drinks_tax_price_labelEntry.get() != '0 Frs':
            textarea.insert(END,f'\n Cold Drinks Tax Price\t\t{cold_drinks_tax_price_labelEntry.get()}')
        if fast_food_tax_price_labelEntry.get() != '0 Frs':
            textarea.insert(END,f'\n Fast Food Tax Price\t\t\t{fast_food_tax_price_labelEntry.get()}')
            
        textarea.insert(END,f'\n ------------------------------------------')
        textarea.insert(END,f'\n Total Bill\t\t{totalbill} Frs')
    
def clear():
    textarea.delete(1.0,END)
    cosmeticprice_labelEntry.delete(0,END)
    grocery_price_labelEntry.delete(0,END)
    cold_drinks_price_labelEntry.delete(0,END)
    fast_food_price_labelEntry.delete(0,END)
    cosmetic_tax_price_labelEntry.delete(0,END)
    grocery_tax_price_labelEntry.delete(0,END)
    cold_drinks_tax_price_labelEntry.delete(0,END)
    fast_food_tax_price_labelEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    billEntry.delete(0,END)
    bathsoapEntry.delete(0,END)
    bathsoapEntry.insert(0,0)
    facecreamEntry.delete(0,END)
    facecreamEntry.insert(0,0)
    facewashEntry.delete(0,END)
    facewashEntry.insert(0,0)
    hairgelEntry.delete(0,END)
    hairgelEntry.insert(0,0)
    hairsprayEntry.delete(0,END)
    hairsprayEntry.insert(0,0)
    bodylotionEntry.delete(0,END)
    bodylotionEntry.insert(0,0)
    
    ricelabelEntry.delete(0,END)
    ricelabelEntry.insert(0,0)
    oil_labelEntry.delete(0,END)
    oil_labelEntry.insert(0,0)
    sugarlabelEntry.delete(0,END)
    sugarlabelEntry.insert(0,0)
    wheatlabelEntry.delete(0,END)
    wheatlabelEntry.insert(0,0)
    tealabelEntry.delete(0,END)
    tealabelEntry.insert(0,0)
    flourlabelEntry.delete(0,END)
    flourlabelEntry.insert(0,0)
    
    coca_cola_labelEntry.delete(0,END)
    coca_cola_labelEntry.insert(0,0)
    fantalabelEntry.delete(0,END)
    fantalabelEntry.insert(0,0)
    spritelabelEntry.delete(0,END)
    spritelabelEntry.insert(0,0)
    pepsilabelEntry.delete(0,END)
    pepsilabelEntry.insert(0,0)
    orangina_labelEntry.delete(0,END)
    orangina_labelEntry.insert(0,0)
    vimto_labelEntry.delete(0,END)
    vimto_labelEntry.insert(0,0)
    
    pizzalabelEntry.delete(0,END)
    pizzalabelEntry.insert(0,0)
    hamburger_labelEntry.delete(0,END)
    hamburger_labelEntry.insert(0,0)
    sandwich_labelEntry.delete(0,END)
    sandwich_labelEntry.insert(0,0)
    onion_ring_labelEntry.delete(0,END)
    onion_ring_labelEntry.insert(0,0)
    chicken_labelEntry.delete(0,END)
    chicken_labelEntry.insert(0,0)
    cheeseburger_labelEntry.delete(0,END)
    cheeseburger_labelEntry.insert(0,0)    
    
#function to print bill
def print_bill():
    #checking if the textarea content is empty 
    if textarea.get(1.0,END) == '\n':
        messagebox.showerror('error','Bill Content is empty')
    else:
        #code to print the bill in the the printer
        file = tempfile.mktemp('.txt')
        open(file, 'w').write(textarea.get(1.0,END))
        os.startfile(file,'print') #takes a file as a string argument and opens that file

#function to send bill through Email
def email():
    import smtplib
    import ssl
    from email.message import EmailMessage
     #def send_mail():
            
            #sender_email = senderlabel_Entry.get()
            #receiver_email = email_label_Entry.get()
            #password = passwordlabel_Entry.get()
            
            #smtp = smtplib.SMTP('smtp.gmail.com',587)
            #smtp.starttls()
            #smtp.login(sender_email,password)
            #message = message_text_area.get(1.0,END)
            #smtp.sendmail(sender_email,receiver_email,message)
            #smtp.quit()
            #messagebox.showinfo('Success',f'Bill is successfully sent to {receiver_email}',parent=top) 
        #except:
             #   messagebox.showerror('Error','Something went wrong, please try again',parent=top)
                
    #from email.message import EmailMessage
    if textarea.get(1.0,END) == '\n':
        messagebox.showerror('error','Bill Content is empty')
    else:
        top = Toplevel()
        top.title('Email')
        top.geometry('600x650')
        top.resizable(False,False)
        top.config(bg='firebrick2')
        
        senderframe = LabelFrame(top,text="SENDER",bd=7,relief=GROOVE,fg='white',bg='firebrick2',font=('ariel',20,'bold'))
        senderframe.pack(pady=10,padx=10)
        
        senderlabel = Label(senderframe,text="Sender's Email",bg='firebrick2',fg='white',font=('ariel',15,'bold'))
        senderlabel.grid(row=0,column=0)
        senderlabel_Entry = Entry(senderframe,font=('ariel',12,'bold'),width=30)
        senderlabel_Entry.grid(row=0,column=1,padx=10,pady=10)
        
        passwordlabel = Label(senderframe,text="Password",bg='firebrick2',fg='white',font=('ariel',15,'bold'))
        passwordlabel.grid(row=1,column=0)
        passwordlabel_Entry = Entry(senderframe,font=('ariel',12,'bold'),show='*',width=30)
        passwordlabel_Entry.grid(row=1,column=1,padx=10,pady=10)
        
        recipientframe = LabelFrame(top,text="RECIPIENT",bd=7,relief=GROOVE,fg='white',bg='firebrick2',font=('ariel',20,'bold'))
        recipientframe.pack(pady=15,padx=10)
        
        email_label = Label(recipientframe,text="Email Address",bg='firebrick2',fg='white',font=('ariel',15,'bold'))
        email_label.grid(row=0,column=0)
        email_label_Entry = Entry(recipientframe,font=('ariel',12,'bold'),width=30)
        email_label_Entry.grid(row=0,column=1,padx=10,pady=10)
        
        message_label = Label(recipientframe,text="Message",bg='firebrick2',fg='white',font=('ariel',15,'bold'))
        message_label.grid(row=1,column=0)
             
        #textscroll = Scrollbar(recipientframe,orient=VERTICAL)
        #textscroll.grid(side=RIGHT,fill=Y)
        #textscroll.config(command=message_text_area.yview)
        
        message_text_area = Text(recipientframe,font=('ariel',12,'bold'),bd=3,relief=SUNKEN,height=15,width=44)
        message_text_area.grid(row=2,column=0,pady=5,padx=10,columnspan=2)
        message_text_area.delete(1.0,END)
        message_text_area.insert(END,textarea.get(1.0,END).replace('=','').replace('-',''))
        
        sendbtn = Button(top,text="Send",font=('ariel',15,'bold'),width=11,height=1,cursor='hand2',activeforeground='firebrick2',bd=3,relief=GROOVE,bg='white',fg='firebrick2')
        sendbtn.place(x=220,y=589)
        
        #send_mail()
        
         
            #OR
        sender_email = senderlabel_Entry.get()
        receiver_email = email_label_Entry.get()
        password = passwordlabel_Entry.get()
        new_message = EmailMessage()
        new_message['subject'] = "Bills Content"
        new_message['From'] = sender_email
        new_message['To'] = receiver_email
        new_message.set_content(textarea.get(1.0,END))
        
        context = ssl.create_default_context()
        
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(sender_email,password)
            smtp.send_message(new_message)
        #if smtp.send_message(new_message):
            messagebox.showinfo('success','email sent successfully')
          #  return
        top.mainloop()
def logout():
    root.destroy()
    import login
    
             
#GUI PART
systemLabel = Label(root,text="Inventory Management System",font=("ariel",30,'bold'),bg='firebrick2',fg='gold2',bd=7,relief=GROOVE,height=3)
systemLabel.pack(fill=X)

logoutbtn = Button(root,text='Logout',fg='gold2',bg='firebrick2',font=("ariel",13,'bold'),bd=0,activebackground='firebrick2',cursor='hand2',
                   activeforeground='gold2',command=logout)
logoutbtn.place(x=20,y=15)

detailsframe  = LabelFrame(root,text="Customer Details",font=("ariel",15,'bold'),bg='firebrick2',fg='gold2',bd=7,relief=GROOVE)
detailsframe.pack(pady=10,fill=X)

namedetails = Label(detailsframe,text="Name",font=("Time new romans",15,'bold'),bg='firebrick2',fg='white')
namedetails.grid(row=0,column=0,padx=10,pady=10)
nameEntry = Entry(detailsframe,font=("ariel",15,'bold'),width=27,bd=7)
nameEntry.grid(row=0,column=1,padx=10)

phonedetails = Label(detailsframe,text="Phone Number",font=("Time new romans",15,'bold'),bg='firebrick2',fg='white')
phonedetails.grid(row=0,column=2,padx=10,pady=10)
phoneEntry = Entry(detailsframe,font=("ariel",15,'bold'),width=27,bd=7)
phoneEntry.grid(row=0,column=3,padx=10,pady=10)

billdetails = Label(detailsframe,text="Bill Number",font=("Time new romans",15,'bold'),bg='firebrick2',fg='white')
billdetails.grid(row=0,column=4,padx=10,pady=10)
billEntry = Entry(detailsframe,font=("ariel",15,'bold'),width=27,bd=7)
billEntry.grid(row=0,column=5,padx=10,pady=10)

searchbtn = Button(detailsframe,text="SEARCH",bg="white",command=search_bill,width=10,fg="firebrick2",relief=GROOVE,bd=7,font=('ariel',10,'bold'),cursor='hand2',activeforeground='firebrick2')
searchbtn.grid(row=0,column=6,padx=10,pady=10)

productsframe = Frame(root)
productsframe.pack()

#COSMETICS FRAME
cosmeticDetails = LabelFrame(productsframe,text="Cosmetics",font=("ariel",15,'bold'),bg='firebrick2',fg='gold2',bd=7,relief=GROOVE)
cosmeticDetails.grid(row=0,column=0)

bathsoap = Label(cosmeticDetails,text="Bath Soap",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
bathsoap.grid(row=0,column=0,padx=10,pady=5,sticky='w')
bathsoapEntry = Entry(cosmeticDetails,bd=5)
bathsoapEntry.delete(0,END)
bathsoapEntry.insert(0,0)
bathsoapEntry.grid(row=0,column=1,pady=10,padx=10)

facecream = Label(cosmeticDetails,text="Face Cream",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
facecream.grid(row=1,column=0,padx=10,sticky='w')
facecreamEntry = Entry(cosmeticDetails,bd=5)
facecreamEntry.insert(0,0)
facecreamEntry.grid(row=1,column=1,pady=10,padx=10)
 
facewash = Label(cosmeticDetails,text="Face Watch",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
facewash.grid(row=2,column=0,padx=10,sticky='w')
facewashEntry = Entry(cosmeticDetails,bd=5)
facewashEntry.insert(0,0)
facewashEntry.grid(row=2,column=1,pady=10,padx=10)

hairgel = Label(cosmeticDetails,text="Hair Gel",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
hairgel.grid(row=3,column=0,padx=10,sticky='w')
hairgelEntry = Entry(cosmeticDetails,bd=5)
hairgelEntry.insert(0,0)
hairgelEntry.grid(row=3,column=1,pady=10,padx=10)

bodylotion = Label(cosmeticDetails,text="Body Lotion",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
bodylotion.grid(row=4,column=0,padx=10,sticky='w')
bodylotionEntry = Entry(cosmeticDetails,bd=5)
bodylotionEntry.insert(0,0)
bodylotionEntry.grid(row=4,column=1,pady=10,padx=10)

hairspray = Label(cosmeticDetails,text="Hair Spray",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
hairspray.grid(row=5,column=0,padx=10,sticky='w')
hairsprayEntry = Entry(cosmeticDetails,bd=5)
hairsprayEntry.insert(0,0)
hairsprayEntry.grid(row=5,column=1,pady=10,padx=10)

#GROCERY FRAME
groceryDetails = LabelFrame(productsframe,text="Grocery",font=("ariel",15,'bold'),bg='firebrick2',fg='gold2',bd=7,relief=GROOVE)
groceryDetails.grid(row=0,column=1)

ricelabel = Label(groceryDetails,text="Rice",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
ricelabel.grid(row=0,column=0,padx=10,pady=5,sticky='w')
ricelabelEntry = Entry(groceryDetails,bd=5)
ricelabelEntry.insert(0,0)
ricelabelEntry.grid(row=0,column=1,pady=10,padx=10)

oil_label = Label(groceryDetails,text="Oil",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
oil_label.grid(row=1,column=0,padx=10,pady=5,sticky='w')
oil_labelEntry = Entry(groceryDetails,bd=5)
oil_labelEntry.delete(0,END)
oil_labelEntry.insert(0,0)
oil_labelEntry.grid(row=1,column=1,pady=10,padx=10)

sugarlabel = Label(groceryDetails,text="Sugar",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
sugarlabel.grid(row=2,column=0,padx=10,pady=5,sticky='w')
sugarlabelEntry = Entry(groceryDetails,bd=5)
sugarlabelEntry.delete(0,END)
sugarlabelEntry.insert(0,0)
sugarlabelEntry.grid(row=2,column=1,pady=10,padx=10)

wheatlabel = Label(groceryDetails,text="Wheat",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
wheatlabel.grid(row=3,column=0,padx=10,pady=5,sticky='w')
wheatlabelEntry = Entry(groceryDetails,bd=5)
wheatlabelEntry.insert(0,0)
wheatlabelEntry.grid(row=3,column=1,pady=10,padx=10)

tealabel = Label(groceryDetails,text="Tea",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
tealabel.grid(row=4,column=0,padx=10,pady=5,sticky='w')
tealabelEntry = Entry(groceryDetails,bd=5)
tealabelEntry.insert(0,0)
tealabelEntry.grid(row=4,column=1,pady=10,padx=10)

flourlabel = Label(groceryDetails,text="Flour",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
flourlabel.grid(row=5,column=0,padx=10,pady=5,sticky='w')
flourlabelEntry = Entry(groceryDetails,bd=5)
flourlabelEntry.insert(0,0)
flourlabelEntry.grid(row=5,column=1,pady=10,padx=10)

#COLD DRINKS FRAME
cold_drinks_details = LabelFrame(productsframe,text="Cold Drinks",font=("ariel",15,'bold'),bg='firebrick2',fg='gold2',bd=7,relief=GROOVE)
cold_drinks_details.grid(row=0,column=2)

coca_cola_label = Label(cold_drinks_details,text="Coca Cola",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
coca_cola_label.grid(row=0,column=0,padx=10,pady=5,sticky='w')
coca_cola_labelEntry = Entry(cold_drinks_details,bd=5)
coca_cola_labelEntry.insert(0,0)
coca_cola_labelEntry.grid(row=0,column=1,pady=10,padx=10)

fantalabel = Label(cold_drinks_details,text="Fanta",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
fantalabel.grid(row=1,column=0,padx=10,pady=5,sticky='w')
fantalabelEntry = Entry(cold_drinks_details,bd=5)
fantalabelEntry.insert(0,0)
fantalabelEntry.grid(row=1,column=1,pady=10,padx=10)

spritelabel = Label(cold_drinks_details,text="Sprite",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
spritelabel.grid(row=2,column=0,padx=10,pady=5,sticky='w')
spritelabelEntry = Entry(cold_drinks_details,bd=5)
spritelabelEntry.insert(0,0)
spritelabelEntry.grid(row=2,column=1,pady=10,padx=10)

pepsilabel = Label(cold_drinks_details,text="Pepsi",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
pepsilabel.grid(row=3,column=0,padx=10,pady=5,sticky='w')
pepsilabelEntry = Entry(cold_drinks_details,bd=5)
pepsilabelEntry.insert(0,0)
pepsilabelEntry.grid(row=3,column=1,pady=10,padx=10)

orangina_label = Label(cold_drinks_details,text="Orangina",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
orangina_label.grid(row=4,column=0,padx=10,pady=5,sticky='w')
orangina_labelEntry = Entry(cold_drinks_details,bd=5)
orangina_labelEntry.insert(0,0)
orangina_labelEntry.grid(row=4,column=1,pady=10,padx=10)

vimto_label = Label(cold_drinks_details,text="Vimto",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
vimto_label.grid(row=5,column=0,padx=10,pady=5,sticky='w')
vimto_labelEntry = Entry(cold_drinks_details,bd=5)
vimto_labelEntry.insert(0,0)
vimto_labelEntry.grid(row=5,column=1,pady=10,padx=10)

#FAST FOOD
fast_food_details = LabelFrame(productsframe,text="Fast Food",font=("ariel",15,'bold'),bg='firebrick2',fg='gold2',bd=7,relief=GROOVE)
fast_food_details.grid(row=0,column=3)

pizzalabel = Label(fast_food_details,text="Pizza",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
pizzalabel.grid(row=0,column=0,padx=10,pady=5,sticky='w')
pizzalabelEntry = Entry(fast_food_details,bd=5)
pizzalabelEntry.insert(0,0)
pizzalabelEntry.grid(row=0,column=1,pady=10,padx=10)

hamburger_label = Label(fast_food_details,text="Hamburger",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
hamburger_label.grid(row=1,column=0,padx=10,pady=5,sticky='w')
hamburger_labelEntry = Entry(fast_food_details,bd=5)
hamburger_labelEntry.insert(0,0)
hamburger_labelEntry.grid(row=1,column=1,pady=10,padx=10)

sandwich_label = Label(fast_food_details,text="Sandwich",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
sandwich_label.grid(row=2,column=0,padx=10,pady=5,sticky='w')
sandwich_labelEntry = Entry(fast_food_details,bd=5)
sandwich_labelEntry.insert(0,0)
sandwich_labelEntry.grid(row=2,column=1,pady=10,padx=10)

onion_ring_label = Label(fast_food_details,text="Onion Rings",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
onion_ring_label.grid(row=3,column=0,padx=10,pady=5,sticky='w')
onion_ring_labelEntry = Entry(fast_food_details,bd=5)
onion_ring_labelEntry.insert(0,0)
onion_ring_labelEntry.grid(row=3,column=1,pady=10,padx=10)

chicken_label = Label(fast_food_details,text="Fried Chicken",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
chicken_label.grid(row=4,column=0,padx=10,pady=5,sticky='w')
chicken_labelEntry = Entry(fast_food_details,bd=5)
chicken_labelEntry.insert(0,0)
chicken_labelEntry.grid(row=4,column=1,pady=10,padx=10)

cheeseburger_label = Label(fast_food_details,text="Cheeseburger",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
cheeseburger_label.grid(row=5,column=0,padx=10,pady=5,sticky='w')
cheeseburger_labelEntry = Entry(fast_food_details,bd=5)
cheeseburger_labelEntry.insert(0,0)
cheeseburger_labelEntry.grid(row=5,column=1,pady=10,padx=10)

#BILL FRAME
billframe = Frame(productsframe,bd=8,relief=GROOVE)
billframe.grid(row=0,column=4)

billarea_label = Label(billframe,bd=7,relief=GROOVE,text='Bill Area',font=("ariel",15,'bold'),fg='firebrick2')
billarea_label.pack(fill=X)


textscroll = Scrollbar(billframe,orient=VERTICAL)
textscroll.pack(side=RIGHT,fill=Y)

textarea = Text(billframe,width=44,height=16,yscrollcommand=textscroll.set)
textarea.pack(padx=10)
textscroll.config(command=textarea.yview)

#MENU BILL FRAME
menu_label = LabelFrame(root,text="Bill Menu",font=("ariel",15,'bold'),bg='firebrick2',fg='gold2',bd=7,relief=GROOVE)
menu_label.pack(pady=10,fill=X)

cosmeticprice_label = Label(menu_label,text="Cosmetic Price",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
cosmeticprice_label.grid(row=0,column=0,padx=10,pady=5,sticky='w')
cosmeticprice_labelEntry = Entry(menu_label,bd=5,font=("ariel",10,'bold'))
cosmeticprice_labelEntry.grid(row=0,column=1,pady=10,padx=10)

grocery_price_label = Label(menu_label,text="Grocery Price",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
grocery_price_label.grid(row=1,column=0,padx=10,pady=5,sticky='w')
grocery_price_labelEntry = Entry(menu_label,bd=5,font=("ariel",10,'bold'))
grocery_price_labelEntry.grid(row=1,column=1,pady=10,padx=10)

cold_drinks_price_label = Label(menu_label,text="Cold Drinks Price",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
cold_drinks_price_label.grid(row=2,column=0,padx=10,pady=5,sticky='w')
cold_drinks_price_labelEntry = Entry(menu_label,bd=5,font=("ariel",10,'bold'))
cold_drinks_price_labelEntry.grid(row=2,column=1,pady=10,padx=10)

fast_food_price_label = Label(menu_label,text="Fast Food Price",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
fast_food_price_label.grid(row=3,column=0,padx=10,pady=5,sticky='w')
fast_food_price_labelEntry = Entry(menu_label,bd=5,font=("ariel",10,'bold'))
fast_food_price_labelEntry.grid(row=3,column=1,pady=10,padx=10)

cosmetic_tax_price_label = Label(menu_label,text="Cosmetic Tax Price",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
cosmetic_tax_price_label.grid(row=0,column=2,padx=10,pady=5,sticky='w')
cosmetic_tax_price_labelEntry = Entry(menu_label,bd=5,font=("ariel",10,'bold'))
cosmetic_tax_price_labelEntry.grid(row=0,column=3,pady=10,padx=10)

grocery_tax_price_label = Label(menu_label,text="Grocery Tax Price",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
grocery_tax_price_label.grid(row=1,column=2,padx=10,pady=5,sticky='w')
grocery_tax_price_labelEntry = Entry(menu_label,bd=5,font=("ariel",10,'bold'))
grocery_tax_price_labelEntry.grid(row=1,column=3,pady=10,padx=10)

cold_drinks_tax_price_label = Label(menu_label,text="Cold Drinks Tax Price",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
cold_drinks_tax_price_label.grid(row=2,column=2,padx=10,pady=5,sticky='w')
cold_drinks_tax_price_labelEntry = Entry(menu_label,bd=5,font=("ariel",10,'bold'))
cold_drinks_tax_price_labelEntry.grid(row=2,column=3,pady=10,padx=10)

fast_food_tax_price_label = Label(menu_label,text="Fast Food Tax Price",font=("Time new romans",12,'bold'),bg='firebrick2',fg='white')
fast_food_tax_price_label.grid(row=3,column=2,padx=10,pady=5,sticky='w')
fast_food_tax_price_labelEntry = Entry(menu_label,bd=5,font=("ariel",10,'bold'))
fast_food_tax_price_labelEntry.grid(row=3,column=3,pady=10,padx=10)

#BUTTON FRAME
buttonframe = Frame(menu_label,bd=8,relief=GROOVE)
buttonframe.grid(row=0,column=4,rowspan=4,padx=20)

totalbtn = Button(buttonframe,text="Total",command=total,bg='firebrick2',pady=20,activeforeground='white',cursor='hand2',activebackground='firebrick2',fg='white',bd=6,width=9,font=("Time new romans",12,'bold'))
totalbtn.grid(row=0,column=0,pady=20,padx=10)

billbtn = Button(buttonframe,text="Bill",command=bill,bg='firebrick2',pady=20,activeforeground='white',cursor='hand2',activebackground='firebrick2',fg='white',bd=6,width=9,font=("Time new romans",12,'bold'))
billbtn.grid(row=0,column=1,pady=20,padx=10)

savebtn = Button(buttonframe,command=save_bill,text="Save",bg='firebrick2',pady=20,activeforeground='white',cursor='hand2',activebackground='firebrick2',fg='white',bd=6,width=9,font=("Time new romans",12,'bold'))
savebtn.grid(row=0,column=2,pady=20,padx=10)

emailbtn = Button(buttonframe,text="Email",command=email,bg='firebrick2',pady=20,activeforeground='white',cursor='hand2',activebackground='firebrick2',fg='white',bd=6,width=9,font=("Time new romans",12,'bold'))
emailbtn.grid(row=0,column=3,pady=20,padx=10)

printbtn = Button(buttonframe,text="Print",command=print_bill,bg='firebrick2',pady=20,activeforeground='white',cursor='hand2',activebackground='firebrick2',fg='white',bd=6,width=9,font=("Time new romans",12,'bold'))
printbtn.grid(row=0,column=4,pady=20,padx=10)

clearbtn = Button(buttonframe,command=clear,text="Clear",bg='firebrick2',pady=20,activeforeground='white',cursor='hand2',activebackground='firebrick2',fg='white',bd=6,width=9,font=("Time new romans",12,'bold'))
clearbtn.grid(row=0,column=5,pady=20,padx=10)

root.mainloop()