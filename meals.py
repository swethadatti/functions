def  meal(day,time):
    if day=="sunday":
        if time =="breakfast":
            return"parata"
        elif time =="lunch":
            return"palaw"
        elif time =="dinner":
            return"chapathi"
        else:
            return "not"
    elif day == "monday":
        if time == "breakfast":
            return"poha"
        elif time == "lunch":
            return"ricedal"
        elif time == "dinner":
            return "chola"
        else:
            return "time not found"
print(meal("sunday","lunch"))
print(meal("monday","dinner"))
