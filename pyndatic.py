def insert_patient_data(name:str , age:int): #typehunting
    print(name)
    print(age)

#insert_patient_data("pulkit" , "no")            #the probblem occur here
#so we can use typehuntin alse
insert_patient_data('Ramesh' ,30)  #typing hunting does not give error 


def insert_patient_data(name:str , age:int): #strilicy useing concept

    if(type(name)==str and type(age)==int):

        if(age<0):
            raise TypeError("age should not be in negative ")
        print(age)
        print(name)

    else:
        raise TypeError("Incorrect data type")  #this idea is not scaleble
insert_patient_data('Ramesh' ,"30")  

#problem 2 is data validation