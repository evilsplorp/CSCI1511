
import w3_particip2_fun as w3

def print_student_names(data):
    """
    Obtains the name value from the list of pythoners 
    and displays the first name (or only name). Also
    checks for nickname, as one student used that key.
    Will also bypass users without that key.
    Secondary, added the rest of the students who did
    not provide responses.
    """
    responses_list = data.get("responses", []) # gets the dictionary
    # response is the key, the values are a list in another dictionary
    extracted_names = [] # empty list for the name values
    
    for record in responses_list: # for each matching record in response_list
        # check for nickname and name values
        chosen_identifier = record.get("nickname", "") or record.get("name", "")
        
        # look for a space to separate name; chapter 10
        words = chosen_identifier.split()
        
        if len(words) > 0: 
            # make sure there's at least one name
            extracted_names.append(words[0]) 
            # grab the first listed nickname/name and put it
            # in the extracted_names list
        else:
            continue

    if extracted_names: 
        names_string = ", ".join(extracted_names) 
        # take all the names and separate them by commas
        # found this on Google. 
        print(f"The Pythoners are: {names_string}") 
        # print the list of names
    else:
        print("No names found to print.")

    print("And the rest:", ", ".join(w3.pythoners["new_users"]))
    # takes the other names in the file, under new_users
    # and prints them as well

# Call the function using the alias
print_student_names(w3.pythoners) 

