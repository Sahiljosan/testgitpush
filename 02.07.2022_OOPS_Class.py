class person:

    def __init__(self,name, surname, emailid, year_of_birth):  # u can use any name in place of self
        self.sah = name
        self.surname = surname
        self.emailid = emailid
        self.year_of_birth = year_of_birth


anuj_var = person("anuj" , "bhandari", "anuj@gmail.com", 1994)
sahil = person("sahil " , "josan", "sahil @gmail.com", 1992)
gargi = person("gargi", "xyx", "gargi@gmail.com", 1994)
print(anuj_var.sah)
print(sahil.sah)
print(sahil.sah + sahil.surname)
print(anuj_var.emailid)
print(gargi.emailid)

print(type(sahil))


