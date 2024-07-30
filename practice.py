# def my_function():
#     result = 5 * 2
#     return result

# output = my_function()

# print(output)

def formated_name(fname, lname):
    formated_f_name = fname.title()
    formated_l_name = lname.title()
    return f"{formated_f_name} {formated_l_name}"

formatted_string = formated_name("Brian", "HDZ")

print(formatted_string)
    
