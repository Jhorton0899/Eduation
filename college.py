import pandas as pd

name = input("Hi, my name is John. What is your name? ")
locationCountry = input("Hi {}, have you decided where you'll be going to school yet? ".format(name))
CountryChoice = ''
if locationCountry.lower() in ["yes", "yup", "I think so", "sure"]:
  where = input("if you know what school your studying at you can list it if not lets start with country where would you like to go ? ".format(name))
  if "usa" in where.lower() or "United States" in where.lower():
    tuitionQuestion = input("The USA is a great place to start. Do you have a budget in mind for tuition, {}? ".format(name))
    if tuitionQuestion.lower() in ["yes", "ya", "kind of", "somewhat"]:
        tuitionBudget = float(input("Please enter a numerical value for your tuition budget similar to 000.00: "))
        filtered_df = df[(df['Country'] == 'USA') & (df['Tuition '] <= tuitionBudget)]

        if len(filtered_df) > 0:
            print("Here are some schools in the USA within your tuition budget:")
            formatted_tuition = filtered_df['Tuition '].apply(lambda x: "${:,.2f}".format(x))
            filtered_df['Formatted Tuition'] = formatted_tuition
            print(filtered_df[['Institution', 'Formatted Tuition']])
        else:
            print("I couldn't find any schools in the USA within your tuition budget.")
  else:
    school_df = df[df['Institution'].str.contains(where, case=False)]
    if len(school_df) > 0:
        print("Thats a great school its ranked inside the top 100 world wide for 2023 here are some additional details regarding {}".format(where))
        print(school_df[['Institution', 'Country', 'Tuition ']])
    else:
        print("I couldn't find any schools matching your input. Please make sure to spell the school name correctly.")

    
    
    
    
    
    
    
            
specificLocation = ''
if locationCountry.lower() in ["no", "can't decide", "haven't decided", "still looking"]:
    CountryChoice = input("That's okay, {}, it can be a bit overwhelming. What would you say is most important to you when deciding? ".format(name))
    if CountryChoice.lower().strip() == "location":
        specificLocation = input("Can you be more particular? Are you looking for somewhere with an active nightlife or maybe somewhere with a diverse culture? ")
if specificLocation.lower() in ["nightlife", "excitement", "food", "people"]:
  suggestion = input("I think you'd enjoy New York, California or Florida all of which are in the USA. Can I send you some schools from the area? ")
  if suggestion.lower() in ["yes", "sure", "sounds good"]:
    NewYork = df[(df['State'].str.contains('New York', case=False)) | (df['State'].str.contains('New Jersey', case=False)) | (df['State'].str.contains('Florida', case=False)) | (df['State'].str.contains('California', case=False))]
    if len(NewYork) > 0:
        NewYork['Formatted Tuition'] = NewYork['Tuition '].apply(lambda x: "${:,.2f}".format(x))
        print("Here are some schools from the states discussed:")
        print(NewYork[['Institution', 'Formatted Tuition']])
    else:
        print("I couldn't find any schools in New York or the other schools mentioned.")
elif CountryChoice.lower() in ["price", "cost", "total", "afford"]:
    query = input("Schools outside of the United States tend to be less expensive and rank fairly high in the world rankings. Should I provide you with some? ")
    if query.lower() in ["yes", "yeah", "sure"]:
        SchoolsNotInUSA = df[df['Country'] != 'USA']
        if len(SchoolsNotInUSA) > 0:
          SchoolsNotInUSA['Formatted Tuition'] = SchoolsNotInUSA['Tuition '].apply(lambda x: "${:,.2f}".format(x))
          print("Here are some schools outside the USA along with their tuition prices:")
          print(SchoolsNotInUSA[['Institution', 'Country', 'Formatted Tuition']])
        else:
            print("I couldn't find any schools outside the USA.")
    else:
        print("No problem! Let me know if you need any further assistance.")
else:
    print("I understand. Take your time to decide!")
