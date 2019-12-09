import pandas as pd 
import smtplib

df = pd.read_csv("/path_to_file/nameofcsv.csv")
names= []
[names.append(x) for x in df['Name'] if x not in names]
emails = []
[emails.append(x) for x in df['Email'] if x not in emails]
gifts =[]
[gifts.append(x) for x in df['Gifts'] if x not in gifts]
sender= "name@example.com"

pairs=[]

for name in names:
    #first check if it is an odd/even  entry and then pair
    if len(names) % 2 != 0:
        if len(names) - names.index(name) > 2:
    
            above_2= [name, names[names.index(name)+2]]
            pairs.append(above_2)
        else :
     
            less_than_2= [name, names[names.index(name)-3]]
            pairs.append(less_than_2)
       
    else:
        if len(names) - names.index(name) > 1:
  

            above_2= [name, names[names.index(name)+1]]
            pairs.append(above_2)
        else :
    
            less_than_1= [name, names[names.index(name)-2]]
            pairs.append(less_than_1)


for l in pairs:
    #this will enable you see how the pairing is
    print(l[0] +" give gft to "+ l[1] + "send this email to "+ emails[names.index(l[1])]+ " list of gifts  includes: "+ gifts[mames.index(l[0])])
    
    giver= l[0]
    recipient = l[1]
    email = emails[names.index(giver)]
    gift=  gifts[names.index(recipient)]
    text = """Subject: Secret Santa. This is another test

    
    Hi {giver} , you are to act as secret santa to {recipient}, list of helpful gifts include: {gift}"""
   
    s=smtplib.SMTP_SSL('smtp.gmail.com', 465) 
        
    s.login(sender, "your_password")
    s.sendmail(sender,email,text.format(sender= sender , giver=giver, recipient= recipient, gift = gift))
    s.quit()
    