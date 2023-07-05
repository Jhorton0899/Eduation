import pandas as pd

df = pd.read_excel("C:\\\\\\\\CollegeRanking.xlsx")
pd.set_option('display.max_columns', None)

name = input("Hi, my name is John. What is your name? ")
locationCountry = input("Hi {}, have you decided where you'll be going to school yet? ".format(name))

if locationCountry.lower() in ["yes", "yup", "I think so", "sure"]:
    where = input("If you know what school you're studying at, you can list it below. If not, we can narrow it down. Let's start with which country you'd prefer to study in? ".format(name))
    
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
            print("That's a great school. It's ranked inside the top 100 worldwide for 2023. Here are some additional details regarding {}".format(where))
            print(school_df[['Institution', 'Country', 'State', 'Tuition ', 'Acceptance Rate', 'Education Rank', 'Employability Rank']])
        else:
            print("I couldn't find any schools matching your input. Please make sure to spell the school name correctly.")












elif locationCountry.lower() in ["no", "can't decide", "haven't decided", "still looking"]:
    preference = input("That's okay, {}, it can be a bit overwhelming. What would you say is most important to you when deciding?   ".format(name))

    if preference.lower().strip() in ["location", "nightlife", "excitement", "food", "people"]:
        nightlife_suggestion = input("I think you'd enjoy New York, California, or Florida. All are beautiful locations. Can I send you some schools from the area? ")
        
        if nightlife_suggestion.lower() in ["yes", "sure", "sounds good"]:
            states_df = df[df['State'].str.contains('New York|New Jersey|Florida|California', na=False, case=False)]
            states_df['Formatted Tuition'] = states_df['Tuition '].apply(lambda x: "${:,.2f}".format(x))
            print("Here are some schools in the states discussed:")
            print(states_df[['Institution', 'Formatted Tuition']])
        else:
            print("Okay, let's find another option.")
    elif preference.lower().strip() in ['history','diversity', 'culture', 'historic significance']:
        history_suggestion = input("Israel, is known for its culture and historic value, along with both Japan and the United Kingdom all which have tons of diversity?  ")
        
        if history_suggestion.lower() in ["yes", "sure", "sounds good"]:
            countries_df = df[df['Country'].str.contains('Israel|United Kingdom|Japan', na=False, case=False)]
            countries_df['Formatted Tuition'] = countries_df['Tuition '].apply(lambda x: "${:,.2f}".format(x))
            print("Here are some schools in the countries we discussed.")
            print(countries_df[['Institution', 'Formatted Tuition']])
        else:
            print("Okay, let's find another option.")
    elif preference.lower().strip() in ["price", "cost", "total", "afford"]:
        price_query = input("Schools outside of the United States tend to be less expensive, but there are some options within the United States. Do you have a budget in mind? ")
        
        if price_query.lower() in ["yes", "yeah", "sure"]:
            try:
                tuitionBudget = float(input("Please enter a numerical value for your tuition budget similar to 000.00: "))
                filtered_df = df[(df['Country'] == 'USA') & (df['Tuition '] <= tuitionBudget)]

                if len(filtered_df) > 0:
                    print("Here are some schools in the USA within your tuition budget:")
                    formatted_tuition = filtered_df['Tuition '].apply(lambda x: "${:,.2f}".format(x))
                    filtered_df['Formatted Tuition'] = formatted_tuition
                    print(filtered_df[['Institution', 'Formatted Tuition']])
                else:
                    print("Unfortunately, there are no schools in the USA within your budget.")
            except ValueError:
                print("Please provide a valid numerical value for your budget.")
        else:
            non_us_df = df[df['Country'] != 'USA']
            non_us_df['Formatted Tuition'] = non_us_df['Tuition '].apply(lambda x: "${:,.2f}".format(x))
            print("Here are some schools outside the USA along with their tuition prices:")
            print(non_us_df[['Institution', 'Country', 'Formatted Tuition']])
    elif preference.lower().strip() in ["private", "public", "acceptance", "gpa", "rate", "education"]:
        acceptance = input("Can you list an acceptance rate that you'd consider using the 00.00% format? ")
        
        try:
            acceptance = float(acceptance.strip('%')) / 100.0
            df['Acceptance Rate'] = df['Acceptance Rate'].replace('NULL', '-1')  # replace 'NULL' with -1
            df['Acceptance Rate'] = df['Acceptance Rate'].str.replace(',', '.')  # replace comma with decimal point
            df['Acceptance Rate'] = df['Acceptance Rate'].str.rstrip('%').astype('float') / 100.0  # convert percentages to decimal
            filtered_df = df[(df['Country'] == 'USA') & (df['Acceptance Rate'] <= acceptance)]
            
            if len(filtered_df) > 0:
                print("Here are some schools in the USA with your desired acceptance rate:")
                print(filtered_df[['Institution', 'Acceptance Rate']])
            else:
                print("I couldn't find any schools in the USA with your desired acceptance rate.")
        except ValueError:
            print("Please provide a valid acceptance rate in the format 00.00%.")
else:
    print("I understand. Take your time to decide!")
