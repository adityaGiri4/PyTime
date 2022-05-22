def timer(time, duration, current_day):
    givenTime = time.split(":")
    givenHrs = givenTime[0]
    givenMins = givenTime[1].split(" ")[0]
    print(f"\nUser given time is :- {givenHrs} hours and {givenMins} minutes")
    
    durationTime = duration.split(":")
    durationHrs = durationTime[0]
    durationMins = durationTime[1]
    print(f"Duration time is :- {durationHrs} hours and {durationMins} minutes")
    
    addHrs = int(givenHrs) + int(durationHrs)
    addMins = int(givenMins) + int(durationMins)
    
    fake_addHrs = addHrs
    
    addHrs = int(addHrs)
    addMins = int(addMins)
    
    if addMins >= 60:
        
        
        i = 1
        while True:
            number_of_hours = 60 * i 
            diffMins = addMins - number_of_hours
            
            if diffMins < 60:
                addMins = diffMins
                divHrs = number_of_hours / 60
                addHrs = addHrs + divHrs
                break
            elif diffMins > 60:
                i += 1
                continue
    
   
    days = 0
    if addHrs >= 24:
        days = addHrs / 24
        
        
        
        if int(days) > 1:
            days = int(days)
        else:
            pass
            
    status = None    
    
    
    if givenTime[1].split(" ")[1] == "PM":
        if addHrs < 12:
            status = "P.M."
        elif addHrs > 12:
            while addHrs > 12:
                addHrs -= 12
            status = "A.M."
        elif addHrs == 12:
            status = "A.M."
    elif givenTime[1].split(" ")[1] == "AM":
        while addHrs > 12:
            addHrs -= 12
        if fake_addHrs < 12:
            status = "A.M."
        
        if fake_addHrs > 12:
            status = "P.M."
        elif addHrs == 12:
            status = "P.M."
            
    if addMins < 10:
        addMins = f"0{addMins}"
    # addMins = int(addMins)
    
    
    
   
        
    week = [
        "Sunday", 
        "Monday", 
        "Tuesday", 
        "Wednesday", 
        "Thursday", 
        "Friday", 
        "Saturday"
    ]
    
    
    i = 1
    weekDays = {}
    for day in week:
        weekDays[day] = i
        i += 1
    
    
    
    
    for i in range(int(days) + 1):
        a = i
    
    
    
    o = []
    for p in week[weekDays[current_day]::]:
        o.append(p)
    
    while len(o) < days + 7:
        for i in week:
            o.append(i)
            
    daysWeek = o[int(days)]
    
    if givenTime[1].split(" ")[1] == "PM" and status == "A.M.":
        days += 1
    
    if days == 0:
        display_time = f"It will be :- {int(addHrs)}:{addMins} {status}"
    elif int(days) == 1:
        display_time = f"It will be :- {int(addHrs)}:{addMins} {status}\nNext day.....\nIt will be {daysWeek} "
    elif int(days) != 1:
        display_time = f"It will be :- {int(addHrs)}:{addMins} {status}\n{int(days)} days ahead....\nIt will be {daysWeek}"
    else:
        pass
    
    
    print(f"\n{display_time}")
    
    

def start():

    try: 
        hrsInput = int(input("Enter the time in hours: \n"))
        minsInput = int(input("Now enter the time in minutes: \n"))
        if hrsInput > 12 or minsInput > 59 or hrsInput == 0 and minsInput == 0:
            print("Type the time in 12 hour clock format..")
            hrsInput, minsInput = (None, None)
        

        

        if hrsInput and minsInput is not None:
            status = input("Enter 'AM' or 'PM':\n")
            
            if status not in ["AM", "PM"]:
                status = None
                
            if status is not None:
                duration_hrsInput = int(input("Enter the time of duration in hours: \n"))
                duration_minsInput = int(input("Now enter the time of duration in minutes: \n"))

                day_week1 = input("Enter the day:\n")
                if day_week1 in ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]:
                    day_week = day_week1
                    
                edit_time = f"{hrsInput}:{minsInput} {status}"  
                edit_duration = f"{duration_hrsInput}:{duration_minsInput}"

            
                timer(edit_time, edit_duration, day_week)
            elif status is None:
                print("Please enter 'AM' or 'PM'....")
        elif hrsInput and minsInput is None:
            print("Enter the time in 12 hour clock format..")
    except:
        print("Something went wrong, try running the program again..")

        

