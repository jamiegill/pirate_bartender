import random
def preferences():
    """Prompt the user for yes/no answers on what drink types they prefer"""
    choices = {}
    questions = {
        "strong": "Do ye like yer drinks strong?",
        "salty": "Do ye like it with a salty tang?",
        "bitter": "Are ye a lubber who likes it bitter?",
        "sweet": "Would ye like a bit of sweetness with yer poison?",
        "fruity": "Are ye one for a fruity finish?",
    }
    print("Please answer 'yes' or 'no' ONLY to the following drink preferences:")
    for question in questions:
        prompt = input("{} ".format(questions[question]))
        if "yes" in prompt:
            choices[question] = True
        elif "no" in prompt:
            choices[question] = False
        else:
            print("you did not enter 'yes' or 'no'...'no' is assumed")
            choices[question] = False
    return choices
def create_drink(choices):
    """Using the return output from preferences(), randomly choose ingredients based on preferences"""
    ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
    }
    print("\n\nBelow arrrrr ye ingedients:")
    for choice in choices:
        if choices[choice] == True:
            print(random.choice(ingredients[choice]))
            
if __name__ == '__main__':    
    create_drink( preferences() )
    while True:
        prompt = input("Enter yes/no - would you like to buy another drink?")
        if "yes" in prompt:
            create_drink( preferences() )
        else:
            print("Buy another drink some other time, goodbye!")
            break
