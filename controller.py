import view
import model

def button():
    data_user = view.write_into_file()
    if "$s$" in data_user:
        model.search(data_user[3:])
    elif "$n$" in data_user:
        model.add(data_user[3:])
    elif "$d$" in data_user:
        model.delit(data_user[3:])
    elif "$ch$" in data_user:
        model.change(data_user[4:])
    
   



