# =================================================================================================================
# Student Score List Application
# By Fawwaz Muhammad Tsani in 2024
# Job Connector Data Science and Machine Learning Purwadhika BSD
# =================================================================================================================
from copy import deepcopy

# Data awal
student_profile_data = {
    "10000001": {"full name": "Ahmad Tahir", "class": "9A", "gender": "Male"},
    "10000002": {"full name": "Budi Santoso", "class": "9A", "gender": "Male"},
    "10000003": {"full name": "Cindy Putri", "class": "9A", "gender": "Female"},
    "10000004": {"full name": "Dewi Lestari", "class": "9B", "gender": "Female"},
    "10000005": {"full name": "Eko Prabowo", "class": "9B", "gender": "Male"},
    "10000006": {"full name": "Fani Wijaya", "class": "9B", "gender": "Female"},
    "10000007": {"full name": "Gita Permata", "class": "9C", "gender": "Male"},
    "10000008": {"full name": "Hadi Surya", "class": "9C", "gender": "Male"},
    "10000009": {"full name": "Indra Gunawan Putra", "class": "9C", "gender": "Male"},
}


student_score_data = {
    "10000001": {"math": 86, "indonesian": 70, "english": 87, "science": 87, "social science": 85},
    "10000002": {"math": 89, "indonesian": 88, "english": 84, "science": 92, "social science": 84},
    "10000003": {"math": 88, "indonesian": 87, "english": 86, "science": 89, "social science": 83},
    "10000004": {"math": 90, "indonesian": 86, "english": 85, "science": 93, "social science": 80},
    "10000005": {"math": 77, "indonesian": 88, "english": 84, "science": 88, "social science": 85},
    "10000006": {"math": 78, "indonesian": 84, "english": 88, "science": 91, "social science": 86},
    "10000007": {"math": 75, "indonesian": 83, "english": 89, "science": 85, "social science": 87},
    "10000008": {"math": 60, "indonesian": 85, "english": 85, "science": 84, "social science": 89},
    "10000009": {"math": 77, "indonesian": 84, "english": 84, "science": 90, "social science": 88},
}

class_data = ["9A", "9B", "9C"]

subject_data = [
    "math", "indonesian", "english", "science", "social science"
]


# Help Function
# Sorting the subjects in student_score_data based on the subject names.
def sort_student_score_data():
    global student_score_data
    for id_code in student_score_data:
        student_score_data[id_code] = dict(sorted(student_score_data[id_code].items()))


def sort_student_profile_data():
    global student_profile_data
    data_tmp = student_profile_data
    student_profile_data = dict(sorted(data_tmp.items(), key=lambda x: (x[1]["class"], x[1]["full name"])))


# Getting keys from dictionary values.
def get_keys_in_dict_values(object_data):
    return list(list(object_data.values())[0].keys())


# Getting the length of keys in dictionary values.
def get_len_key_in_dict_values(object_data):
    key_list = get_keys_in_dict_values(object_data)
    key_len_dict = {}
    for key in key_list:
        key_len_dict[key] = len(key)
    return key_len_dict


# Printing a table.
def print_table(main_table, key_name):
    column_len_obj = get_len_key_in_dict_values(main_table)
    
    for key in main_table:
        for column_name in column_len_obj:
            value_len = len(str(main_table[key][column_name]))
            if value_len > column_len_obj[column_name]:
                column_len_obj[column_name] = value_len
    
    print(" | ".join([key_name.ljust(8)] + [column_name.title().ljust(column_len_obj[column_name]) for column_name in column_len_obj]))
    for key in main_table:
        tmp_arr = [key.ljust(8)]
        for column_name in column_len_obj:
            value = str(main_table[key][column_name]).ljust(column_len_obj[column_name])
            tmp_arr.append(value)
        print(" | ".join(tmp_arr))


# Printing menu options.
def print_menu(option_menu):
    for i, menu in enumerate(option_menu):
        print(f"{i + 1}. {menu}")


# Validating input.
def try_input(input_text, input_type, data_validation, str_method=None):
    while True:
        input_data_ori = input(f"{input_text}: ")
        
        try:
            input_data = input_type(input_data_ori)
            
            if str_method != None and input_type == str:
                if str_method == "upper":
                    input_data = input_data.upper()
                elif str_method == "capitalize":
                    input_data = input_data.capitalize()
                    data_validation = [item.capitalize() for item in data_validation]
            
            if input_data not in data_validation:
                print("INFO: Invalid input. Please try again!")
                continue
            else:
                return input_data
        except ValueError:
            print("INFO: Invalid input. Please try again!")
            continue


# Calculating average points.
def calculate_average_points(score_object):
    average_obj = {}
    for nis in score_object:
        score_list = list(score_object[nis].values())
        average_obj[nis] = round(sum(score_list) / len(score_list), 2)
    return average_obj


# Creating a dictionary of scores for all students.
def create_scores_dict_all_students():
    sort_student_profile_data()
    full_data_tmp = deepcopy(student_profile_data)
    average_points_data = calculate_average_points(student_score_data)
    for id_code in student_profile_data:
        full_data_tmp[id_code].update(student_score_data[id_code])
        full_data_tmp[id_code].update({"average": average_points_data[id_code]})
    
    return full_data_tmp


# Validating ID Code Input.
def input_validate_id_code(input_message):
    while True:
        id_code = input(f"{input_message}: ")
        str_tmp = ""
        
        if len(id_code) != 8:
            str_tmp += "INFO: ID code must be 8 characters long. Please try again!\n"
        
        if not id_code.isdigit():
            str_tmp += "INFO: ID code must contain only numbers.\n"
        
        if id_code in student_profile_data:
            str_tmp += "INFO: ID code is already in use. Please try again with an ID code that has not been used!\n"
        
        if str_tmp != "":
            print(str_tmp)
            continue
        
        return id_code


# Validating Subject Input.
def input_validate_subject():
    while True:
        subject = input("Enter subject: ")
        
        str_tmp = ""
        
        if subject.lower() in subject_data:
            str_tmp += "INFO: Subject is already exist. Please try again with different subject!\n"
        
        if subject.isdigit():
            str_tmp += "INFO: The subject cannot consist only of numbers.\n"
        
        if str_tmp != "":
            print(str_tmp)
            continue

        return subject.lower()

# Validating Class Input.
def input_validate_class(input_message):
    while True:
        class_name = input(f"{input_message}: ")
        
        str_tmp = ""
        
        if class_name.upper() in class_data:
            str_tmp += "INFO: Class is already exist. Please try again with different class!\n"
        
        if str_tmp != "":
            print(str_tmp)
            continue

        return class_name.upper()


sort_student_score_data()
subject_data.sort()


# -----------------------------------------------------------------------------------------------------------------
# 1. Show Student Profiles and Scores
# -----------------------------------------------------------------------------------------------------------------
def show_score():
    print("\n1. Show Student Profiles and Scores")
    option_menu = ["All Classes", "Specific Class", "Back to Main Menu"]
    print("Menu options:")
    print_menu(option_menu)
    
    input_option = try_input("Enter options", int, range(1, len(option_menu) + 1)) - 1
    if input_option == 0:
        show_score_all_classes()
        show_score()
    elif input_option == 1:
        show_score_specific_class()
        show_score()
    elif input_option == 2:
        main()


def show_score_all_classes():
    print("\n1. Show Student Profiles and Scores")
    print("1.1 All Classes")
    
    print("\n# Score All Classes")
    
    full_data_tmp = create_scores_dict_all_students()
    
    if len(full_data_tmp) == 0:
        print("Data does not exist")
    else:
        print_table(full_data_tmp, "ID Code")


def show_score_specific_class():
    print("\n1. Show Student Profiles and Scores")
    print("1.2 Specific Class")
    
    full_data_tmp = create_scores_dict_all_students()
    
    if len(full_data_tmp) == 0 or len(class_data) == 0:
        print("Data does not exist")
    else:
        print("\nClass choice: ")
        print_menu(class_data)
        
        input_class = try_input("Select a class", int, range(1, len(class_data) + 1)) - 1
        id_code_filtered_by_class = filter(lambda id_code: full_data_tmp[id_code]["class"] == class_data[input_class], full_data_tmp)
        filtered_table = {id_code: full_data_tmp[id_code] for id_code in id_code_filtered_by_class}
        
        print(f"\n# Score Class {class_data[input_class]}")
        if len(filtered_table) == 0:
            print("Data does not exist")
        else:
            print_table(filtered_table, "ID Code")


# -----------------------------------------------------------------------------------------------------------------
# 2. Show Rankings
# -----------------------------------------------------------------------------------------------------------------
def show_ranking():
    print("\n2. Show Rankings")
    
    option_menu = ["All Classes", "Specific Class", "Back to Main Menu"]
    print("Menu options:")
    print_menu(option_menu)
    
    input_option = try_input("Enter options", int, range(1, len(option_menu) + 1)) - 1
    if input_option == 0:
        show_ranking_all_classes()
        show_ranking()
    elif input_option == 1:
        show_ranking_specific_class()
        show_ranking()
    elif input_option == 2:
        main()


def show_ranking_all_classes():
    print("\n2. Show Rankings")
    print("2.1 All Classes")
    
    avg_score = calculate_average_points(student_score_data)
    print("\n# Ranking for All Classes")
    if len(avg_score) == 0:
        print("Data does not exist")
    else:
        sorted_avg_score_tmp = sorted(avg_score.items(), key=lambda x:x[1], reverse=True)
        converted_dict = dict(sorted_avg_score_tmp)
        
        tmp_obj = {}
        for i, id_code in enumerate(converted_dict):
            tmp_obj[id_code] = {"full name": student_profile_data[id_code]["full name"], "class": student_profile_data[id_code]["class"], "average": converted_dict[id_code], "Ranking": i+1}
        
        print_table(tmp_obj, "ID Code")


def show_ranking_specific_class():
    print("\n2. Show Rankings")
    print("2.2 Specific Class")
    
    print("\nClass choice: ")
    print_menu(class_data)
    
    avg_score = calculate_average_points(student_score_data)
    
    if len(avg_score) == 0 or len(class_data) == 0:
        print("Data does not exist")
    else:
        input_class = try_input("Select a class", int, range(1, len(class_data) + 1)) - 1
        
        id_code_filtered_by_class = filter(lambda id_code: student_profile_data[id_code]["class"] == class_data[input_class], student_profile_data)
        filtered_avg_score = {id_code: avg_score[id_code] for id_code in id_code_filtered_by_class}
        sorted_avg_score_tmp = sorted(filtered_avg_score.items(), key=lambda x:x[1], reverse=True)
        converted_dict = dict(sorted_avg_score_tmp)
        
        if len(converted_dict) == 0:
            print("Data does not exist")
        else:
            tmp_obj = {}
            for i, id_code in enumerate(converted_dict):
                tmp_obj[id_code] = {"full name": student_profile_data[id_code]["full name"], "average": converted_dict[id_code], "Ranking": i+1}
            
            print(f"\n# Ranking for Class {class_data[input_class]}")
            print_table(tmp_obj, "ID Code")


# -----------------------------------------------------------------------------------------------------------------
# 3. Show Subjects
# -----------------------------------------------------------------------------------------------------------------
def show_subject():
    print("\n3. Show Subjects")
    
    print("\n# All Subjects")
    for subject in subject_data:
        print(f"- {subject.title()}")


# -----------------------------------------------------------------------------------------------------------------
# 4. Show Class
# -----------------------------------------------------------------------------------------------------------------
def show_class():
    print("\n4. Show Class")
    
    print("\n# All Classes")
    for class_name in class_data:
        print(f"- {class_name.upper()}")


# -----------------------------------------------------------------------------------------------------------------
# 5. Add Student Profiles and Scores
# -----------------------------------------------------------------------------------------------------------------
def add_student_profiles_and_scores():
    global student_profile_data, student_score_data
    
    print("\n5. Add Student Profiles and Scores")
    input_id_code = input_validate_id_code("Enter student ID code")
    input_full_name = input("Enter Full Name : ")
    
    print("\nClass choice: ")
    print_menu(class_data)
    
    input_class = try_input("Select a class", int, range(1, len(class_data) + 1)) - 1
    input_gender = try_input("Select gender (Male/Female)", str, ["male", "female"], "capitalize")
    
    profile_data_tmp = {input_id_code: {"full name": input_full_name, "class": class_data[input_class], "gender": input_gender}}
    score_data_tmp = {input_id_code: {}}
    full_data_tmp = deepcopy(profile_data_tmp)
    
    print("Enter subject scores:")
    for subject in subject_data:
        input_value = try_input(f"- {subject.title()} (0 - 100) ", int, range(0,101))
        score_data_tmp[input_id_code].update({subject: input_value})
    
    full_data_tmp[input_id_code].update(score_data_tmp[input_id_code])
    
    print("\nData to be added:")
    print_table(full_data_tmp, "ID Code")
    print("\nNote: Subject scores can be updated in \'Update Score\' menu.")
    
    print()
    confirm_add_data = try_input("Are you sure you want to add that data? (Yes/No)", str, ["yes", "no"], "capitalize")
    
    if confirm_add_data == "Yes":
        print("Data added successfully.")
        
        student_profile_data.update(profile_data_tmp)
        student_score_data.update(score_data_tmp)
        sort_student_profile_data()
        
        update_score_data_tmp = {}
        
        for id_code in student_profile_data:
            update_score_data_tmp[id_code] = student_score_data[id_code]
        
        student_score_data = update_score_data_tmp
        
    else:
        print("Data is not added.")


# -----------------------------------------------------------------------------------------------------------------
# 6. Add Subject
# -----------------------------------------------------------------------------------------------------------------
def add_subject():
    print("\n6. Add Subject")
    
    input_subject = input_validate_subject()
    
    print("\nData to be added:")
    print(f"- {str(input_subject).title()}")
    print("\nNote: The subject will be added and its score will be set to 0. Subject scores can be updated in \'Update Score\' menu.\n")
    
    confirm_add_data = try_input("Are you sure you want to add that data? (Yes/No)", str, ["yes", "no"], "capitalize")
    
    if confirm_add_data == "Yes":
        subject_data.append(input_subject)
        subject_data.sort()
    
        for id_code in student_score_data:
            student_score_data[id_code][input_subject] = 0
        sort_student_score_data()
        
        print("Subject added successfully.")
    else:
        print("Data is not added.")


# -----------------------------------------------------------------------------------------------------------------
# 7. Add Class
# -----------------------------------------------------------------------------------------------------------------
def add_class():
    global class_data
    
    print("\n7. Add Class")
    
    input_class = input_validate_class("Enter class")
    
    print("\nData to be added:")
    print(f"- {str(input_class).title()}")
    print()
    
    confirm_add_data = try_input("Are you sure you want to add that data? (Yes/No)", str, ["yes", "no"], "capitalize")
    
    if confirm_add_data == "Yes":
        class_data.append(input_class)
        class_data.sort()
        print("Class added successfully.")
    else:
        print("Data is not added.")


# -----------------------------------------------------------------------------------------------------------------
# 8. Update Student
# -----------------------------------------------------------------------------------------------------------------
def update_student():
    global student_profile_data, student_score_data
    
    print("\n8. Update Student")
    
    input_id_code = input("Enter student ID code : ")
    
    if input_id_code in student_profile_data:
        print("\nStudent:")
        print_table({input_id_code: student_profile_data[input_id_code]}, "ID Code")
        print()
        
        input_confirm_continue_update = try_input("Continue update? (Yes/No)", str, ["yes", "no"], "capitalize")
    
        if input_confirm_continue_update == "Yes":
            while True:
                option_menu = [f"ID Code: {input_id_code}"]
                option_menu.extend([item[0].title() + ": " + str(item[1]) for item in student_profile_data[input_id_code].items()])
                
                print("\nOption Profile Student to Update:")
                print_menu(option_menu)
                
                print()
                input_option = try_input("Enter options", int, range(1, len(option_menu) + 1)) - 1
                
                option_key = ["ID Code"] + list(student_profile_data[input_id_code].keys())
                key_to_change = option_key[input_option]
                if input_option == 0:
                    print("\nChange ID Code")
                else:
                    print(f"\nChange {key_to_change.title()}")
                
                if input_option == 0: # ID Code
                    input_new_id_code = input_validate_id_code("Enter new ID code of student")
                    
                    print(f"\n\'{input_id_code}\' will be changed to \'{input_new_id_code}\'.\n")
                    confirm_update_data = try_input("Update Data? (Yes/No)", str, ["yes", "no"], "capitalize")
                    if confirm_update_data == "Yes":
                        dict_value_tmp1 = student_profile_data[input_id_code]
                        student_profile_data[input_new_id_code] = dict_value_tmp1
                        student_profile_data.pop(input_id_code)
                        sort_student_profile_data()
                        
                        dict_value_tmp2 = student_score_data[input_id_code]
                        student_score_data[input_new_id_code] = dict_value_tmp2
                        student_score_data.pop(input_id_code)
                        
                        update_score_data_tmp = {}
                        for id_code in student_profile_data:
                            update_score_data_tmp[id_code] = student_score_data[id_code]
                        student_score_data = update_score_data_tmp
                        
                        input_id_code = input_new_id_code
                        
                        print("Data succesfully updated.")
                    else:
                        print("Data is not updated.")
                elif input_option == 1: # Full Name
                    input_value = input("Enter new full name: ")
                elif input_option == 2: # Class
                    print("\nClass choice: ")
                    
                    print_menu(class_data)
                    input_idx = try_input("Select a new class", int, range(1, len(class_data) + 1)) - 1
                    input_value = class_data[input_idx]
                elif input_option == 3: # Gender
                    input_value = try_input("Select gender (Male/Female)", str, ["male", "female"], "capitalize")
                
                if input_option != 0:
                    print(f"\n\'{student_profile_data[input_id_code][key_to_change]}\' will be changed to \'{input_value}\'.\n")
                    confirm_update_data = try_input("Update Data? (Yes/No)", str, ["yes", "no"], "capitalize")
                
                if confirm_update_data == "Yes":
                    if input_option != 0:
                        student_profile_data[input_id_code][key_to_change] = input_value
                    
                        print("Data succesfully updated.")
                    
                    print()
                    confirm_update_again = try_input("Update other options in the profile? (Yes/No)", str, ["yes", "no"], "capitalize")
                    print()
                    
                    if confirm_update_again == "Yes":
                        continue
                    else:
                        break
                else:
                    print("Data is not updated.")
                    break
    
    else:
        print("INFO: The data you are looking for doesn't exist.")


# -----------------------------------------------------------------------------------------------------------------
# 9. Update Score
# -----------------------------------------------------------------------------------------------------------------
def update_score():
    global student_score_data
    
    print("\n9. Update Score")
    
    full_data_tmp = create_scores_dict_all_students()
    
    input_id_code = input("Enter student ID code : ")
    
    if input_id_code in student_score_data:
        print("\nStudent:")
        data_student_tmp = full_data_tmp[input_id_code]
        data_student_tmp.pop("class")
        data_student_tmp.pop("gender")
        data_student_tmp.pop("average")
        
        print_table({input_id_code: data_student_tmp}, "ID Code")
        print()
        
        input_confirm_continue_update = try_input("Continue update? (Yes/No)", str, ["yes", "no"], "capitalize")
    
        if input_confirm_continue_update == "Yes":
            while True:
                option_menu = [item[0].title() + ": " + str(item[1]) for item in list(student_score_data[input_id_code].items())]
                print("\nOption Subject Score to Update:")
                print_menu(option_menu)
                
                print()
                input_option = try_input("Enter options", int, range(1, len(option_menu) + 1)) - 1
                
                key_to_change = list(student_score_data[input_id_code].keys())[input_option]
                print(key_to_change)
                
                print("\nChange Score")
                input_value = try_input(f"{key_to_change.title()} (0 - 100) ", int, range(0,101))
                
                confirm_update_data = try_input("Update Data? (Yes/No)", str, ["yes", "no"], "capitalize")
                
                if confirm_update_data == "Yes":
                    student_score_data[input_id_code][key_to_change] = input_value
                    print("Data succesfully updated.")
                    
                    print()
                    confirm_update_again = try_input("Update scores for other subjects? (Yes/No)", str, ["yes", "no"], "capitalize")
                    
                    if confirm_update_again == "Yes":
                        continue
                    else:
                        break
                else:
                    print("Data is not updated.")
                    break
        else:
            print("Data is not updated.")
    else:
        print("INFO: The data you are looking for doesn't exist.")


# -----------------------------------------------------------------------------------------------------------------
# 10. Update Subject
# -----------------------------------------------------------------------------------------------------------------
def update_subject():
    global student_score_data
    
    print("\n10. Update Subject")
    
    input_subject = input("Enter subject name : ").lower()
    
    if input_subject in subject_data:
        print(f"Subject found: {input_subject.title()}")
        
        print()
        input_confirm_continue_update = try_input("Continue update? (Yes/No)", str, ["yes", "no"], "capitalize")
    
        if input_confirm_continue_update == "Yes":
            print("\nChange Subject Name")
            input_new_subject = input("Enter new subject name : ").lower()
            while input_subject == input_new_subject:
                print("\nThe old subject name cannot be the same as the new one.")
                input_new_subject = input("Enter new subject name : ")
            
            print(f"\n\'{input_subject.title()}\' will be changed to \'{input_new_subject.title()}\'.\n")
            
            confirm_update_data = try_input("Update Data? (Yes/No)", str, ["yes", "no"], "capitalize")
            
            if confirm_update_data == "Yes":
                idx_subject = subject_data.index(input_subject)
                subject_data[idx_subject] = input_new_subject
                
                for id_code in student_score_data:
                    for subject in student_score_data[id_code]:
                        if subject == input_subject:
                            student_score_data[id_code][input_new_subject] = student_score_data[id_code][subject]
                            student_score_data[id_code].pop(subject)
                            break
                
                sort_student_score_data()
                subject_data.sort()
                
                print("Data succesfully updated.")            
        else:
            print("Data is not updated.")
        
    else:
        print("INFO: The data you are looking for doesn't exist.")


# -----------------------------------------------------------------------------------------------------------------
# 11. Update Class
# -----------------------------------------------------------------------------------------------------------------
def update_class():
    global student_profile_data
    
    print("\n11. Update Class")
    
    input_class = input("Enter class name : ").upper()
    
    if input_class in class_data:
        print(f"Class found: {input_class}")
        
        print()
        input_confirm_continue_update = try_input("Continue update? (Yes/No)", str, ["yes", "no"], "capitalize")
    
        if input_confirm_continue_update == "Yes":
            print("\nChange Class Name")
            input_new_class = input_validate_class("Enter new class name")
            
            print(f"\n\'{input_class.title()}\' will be changed to \'{input_new_class.title()}\'.\n")
            
            confirm_update_data = try_input("Update Data? (Yes/No)", str, ["yes", "no"], "capitalize")
            
            if confirm_update_data == "Yes":
                idx_class = class_data.index(input_class)
                class_data[idx_class] = input_new_class
                
                for id_code in student_profile_data:
                    if student_profile_data[id_code]["class"] == input_class:
                        student_profile_data[id_code]["class"] = input_new_class
                
                print("Data succesfully updated.")            
        else:
            print("Data is not deleted.")
        
    else:
        print("INFO: The data you are looking for doesn't exist.")


# -----------------------------------------------------------------------------------------------------------------
# 12. Delete Student Profiles and Scores
# -----------------------------------------------------------------------------------------------------------------
def delete_student_profiles_and_scores():
    global student_profile_data, student_score_data
    
    print("\n12. Delete Student Profiles and Scores")
    
    input_id_code = input("Enter student ID code : ")
    
    if input_id_code in student_profile_data:
        print("\nStudent:")
        
        full_data_tmp = create_scores_dict_all_students()
        data_student_tmp = full_data_tmp[input_id_code]
        data_student_tmp.pop("average")
        
        print_table({input_id_code: student_profile_data[input_id_code]}, "ID Code")
        
        print()
        input_confirm_continue_delete = try_input("Continue delete? (Yes/No)", str, ["yes", "no"], "capitalize")
    
        if input_confirm_continue_delete == "Yes":
            student_profile_data.pop(input_id_code)
            student_score_data.pop(input_id_code)
            
            print("Data succesfully deleted.")
        else:
            print("Data is not deleted.")
    
    else:
        print("INFO: The data you are looking for doesn't exist.")


# -----------------------------------------------------------------------------------------------------------------
# 13. Delete Subject
# -----------------------------------------------------------------------------------------------------------------
def delete_subject():
    global student_score_data, subject_data
    
    print("\n14. Delete Subject")
    
    input_subject = input("Enter subject : ").lower()
    
    if input_subject in subject_data:
        print(f"Subject found: {input_subject.title()}")
        
        print()
        input_confirm_continue_delete = try_input("Continue delete? (Yes/No)", str, ["yes", "no"], "capitalize")
    
        if input_confirm_continue_delete == "Yes":
            subject_data.remove(input_subject)
            
            for id_code in student_score_data:
                for subject in list(student_score_data[id_code]):
                    if subject == input_subject:
                        student_score_data[id_code].pop(input_subject)
            
            print("Data succesfully deleted.")
        else:
            print("Data is not deleted.")
    
    else:
        print("INFO: The data you are looking for doesn't exist.")


# -----------------------------------------------------------------------------------------------------------------
# 14. Delete Class
# -----------------------------------------------------------------------------------------------------------------
def delete_class():
    global student_profile_data, student_score_data, class_data
    
    print("\n14. Delete Class")
    
    input_class = input("Enter class : ").upper()
    
    print("Class:")
    if input_class in class_data:
        print(f"- {input_class}")
        
        print()
        input_confirm_continue_delete = try_input("Continue delete? (Yes/No)", str, ["yes", "no"], "capitalize")
    
        if input_confirm_continue_delete == "Yes":
            id_code_filtered_by_class = filter(
                lambda id_code: student_profile_data[id_code]["class"] == input_class, 
                student_profile_data
            )
            
            idx_class = class_data.index(input_class)
            class_data.pop(idx_class)
            
            
            for id_code in list(id_code_filtered_by_class):
                student_profile_data.pop(id_code)
                student_score_data.pop(id_code)
            
            print("Data succesfully deleted.")
        else:
            print("Data is not deleted.")
    
    else:
        print("INFO: The data you are looking for doesn't exist.")


# -----------------------------------------------------------------------------------------------------------------
# MAIN
# -----------------------------------------------------------------------------------------------------------------
def main():
    print("\n### Aplikasi Daftar Nilai Siswa ###\n")
    
    option_menu = [
        "Show Student Profiles and Scores", "Show Rankings", "Show Subjects", "Show Class",
        "Add Student Profiles and Scores", "Add Subject", "Add Class",
        "Update Student", "Update Score", "Update Subject", "Update Class",
        "Delete Student Profiles and Scores", "Delete Subject", "Delete Class",
        "Exit"
        ]
    
    print("Menu options:")
    print_menu(option_menu)
    
    input_option = try_input("Enter options", int, range(1, len(option_menu) + 1)) - 1
    
    # 1. Show Student Profiles and Scores
    if input_option == 0:
        show_score()
        main()
        
    # 2. Show Rankings
    elif input_option == 1:
        show_ranking()
        main()
        
    # 3. Show Subjects
    elif input_option == 2:
        show_subject()
        main()
    
    # 4. Show Class
    elif input_option == 3:
        show_class()
        main()
        
    # 5. Add Student Profiles and Scores
    elif input_option == 4:
        add_student_profiles_and_scores()
        main()
        
    # 6. Add Subject
    elif input_option == 5:
        add_subject()
        main()
        
    # 7. Add Class
    elif input_option == 6:
        add_class()
        main()
        
    # 8. Update Student
    elif input_option == 7:
        update_student()
        main()
        
    # 9. Update Score
    elif input_option == 8:
        update_score()
        main()
        
    # 10. Update Subject
    elif input_option == 9:
        update_subject()
        main()
        
    # 11. Update Class
    elif input_option == 10:
        update_class()
        main()
        
    # 12. Delete Student Profiles and Scores
    elif input_option == 11:
        delete_student_profiles_and_scores()
        main()
        
    # 13. Delete Subject
    elif input_option == 12:
        delete_subject()
        main()

    # 14. Delete Class
    elif input_option == 13:
        delete_class()
        main()
    
    # 15. "Exit"
    elif input_option == 14:
        print("\nThank you for using the application. Have a Nice Day.")
        exit()

main()