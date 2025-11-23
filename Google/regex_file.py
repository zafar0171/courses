#! /usr/bin/env python



import re
#print("new_step")

log = "July 31 07:51:48 mycomputer bad_process[12354645]: ERROR Performing package upgrade"



index = log.index("[")

#print(log[index+1:index+6])


regex = r"\[(\d+)\]"      #This regular expression matches a string enclosed in square brackets followed by one or more digits.
result = re.search(regex,log)

#print(result[1])


                #Simple matching in python


result = re.search(r"aza","plaza")
print(result)

result = re.search(r"aza","bazaar")
print(result)



result = re.search(r"aza", "maze")
print(result)

print(re.search(r"^x","Xenon",re.IGNORECASE))



print(re.search(r"p.ng","penguin"))
print(re.search(r"n$", "penguin"))


print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng","sponge"))



                #Wildcards and Character classes


print(re.search(r"[Pp]ython", "Python"))


print(re.search(r"[a-z]way", "The end of highway"))
print(re.search(r"[a-z]way","what a way to go"))
print(re.search(r"cloud[a-zA-Z]", "cloudy"))
print(re.search(r"cloud[a-zA-Z0-9]",'cloud9'))



print(re.search(r"[^a-zA-Z]", "This is a sentence with whitespaces"))
print(re.search(r"[^a-zA-Z ]", "this is a sentence with whitespaces"))



                #Repetition Qualifiers

#         "*", "+", "?" --- They are repetition Qualifiers.

print(re.search(r"Py.*n", "Python"))
print(re.search(r"Py.*n", "Python Programming"))


print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))


print(re.search(r"o+l+", "Goldfish"))
print(re.search(r"o+l+", "wooly"))
print(re.search(r"o+l+", 'boil'))               #characters aren't continued in "boil", so result will be NOne


print(re.search(r"p?each", " To each thier own"))
print(re.search(r"P?each", " I like peaches"))



                #Escaping characters 



print(re.search(r".com", "welcome"))
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))


print(re.search(r"\w+", 'This_is_an_example',re.IGNORECASE))
print(re.search(r"\w*", "this_is_another_example"))
print(re.search(r"\w?", "this_is_another_one"))



                #Examples


print(re.search(r"A.*a","Argentina"))
print(re.search(r"A.*a", "Azerbaijan"))
print(re.search(r"^A.*a$", "Australia" ))



#<MOre



num = "111-222-3333"

print(re.search(r"\d{3}-\d{3}-\d{4}",num))