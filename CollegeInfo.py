import pandas as pd

df = pd.read_excel("C:\\CollegeRanking.xlsx")
pd.set_option('display.max_columns', None)

name = input("Hi, my name is John. What is your name? ")

school_decided = input("Hi {}, have you decided where you'll be going to school yet? ".format(name))

if school_decided.lower() in ["yes", "yup", "I think so", "sure"]:
    school_name = input("Great! What's the name of the school you'll be studying at? ")
    school_df = df[df['Institution'].str.contains(school_name, case=False)]
    if len(school_df) > 0:
        print("That's a great school. Here are some additional details:")
        print(school_df[['Institution', 'Country', 'State', 'Tuition ', 'Acceptance Rate', 'Education Rank', 'Employability Rank']])
    else:
        print("I couldn't find any schools matching your input. Please make sure to spell the school name correctly.")
else:
    country = input("In which country are you looking to study? ")
    tuitionBudget = float(input("What's your maximum tuition budget in USD? Please enter a numerical value : "))
    filtered_df = df[(df['Country'].str.lower() == country.lower()) & (df['Tuition '] <= tuitionBudget)]

    if len(filtered_df) > 0:
        print("Here are some schools in {} within your tuition budget:".format(country))
        formatted_tuition = filtered_df['Tuition '].apply(lambda x: "${:,.2f}".format(x))
        filtered_df['Formatted Tuition'] = formatted_tuition
        print(filtered_df[['Institution', 'Formatted Tuition']])
    else:
        print("I couldn't find any schools in {} within your tuition budget.".format(country))
