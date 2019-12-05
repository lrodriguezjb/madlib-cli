
# File Reader Function

try:
    def fileReader(path):
        with open(path, 'r') as madscript:
            return madscript.read()

except IOError:
    print("Could not Read File")


# Function that Creates a File
def file_writer(path, value):
    with open(path, 'w') as madscomplete:
        return madscomplete.write(value)

# Function that replaces all the fillers for {}


def replacer():
    scriptcontent = fileReader('madlib.txt')
    cleanscript = scriptcontent.replace("{Adjective}", "{}").replace("{A First Name}", "{}").replace("{Plural Noun}", "{}").replace("{Past Tense Verb}", "{}").replace(
        "{Large Animal}", "{}").replace("{Small Animal}", "{}").replace("{A Girl's Name}", "{}").replace("{Number}", "{}").replace("{First Name's}", "{}")
    return cleanscript


# Function that sets all the parameters for the questions
def strinserter(adjective_one, adjective_two, first_name, past_tense, second_name, adjective_three, adjective_four, plural_noun, large_animal, small_animal, girls_name,
                adjective_five, second_plural, adjective_six, third_plural, number, another_name, second_number, fourth_plural, third_number, last_plural):
    cleanscript = replacer()
    formattedscript = cleanscript.format(adjective_one, adjective_two, first_name, past_tense, second_name, adjective_three, adjective_four, plural_noun, large_animal,
                                         small_animal, girls_name, adjective_five, second_plural, adjective_six, third_plural, number, another_name, second_number, fourth_plural, third_number, last_plural)
    print(formattedscript)
    file_writer('gamecomplete.txt', formattedscript)
    return formattedscript


print("*" * 42)
print("**    Welcome to the Game of Madlibs!   **")
print("**You will be asked some questions below**")
print("**    Once you are done answering       **")
print("** the questions you will see a story :)**")
print("*" * 42)


def inputfunction():
    while True:
        adjective_one = input('Please Enter an Adjective: ')
        adjective_two = input('Please Enter a Second Adjective: ')
        first_name = input('Please Enter a First Name:')
        past_tense = input('Please Enter a Past Tense Verb: ')
        second_name = input('Please Enter a Second Name: ')
        adjective_three = input('Please Enter a Third Adjective: ')
        adjective_four = input('Please Enter a Fourth Adjective: ')
        plural_noun = input('Please Enter a Plural Noun: ')
        large_animal = input('Please Enter a Large Animal: ')
        small_animal = input('Please Enter a Small Animal: ')
        girls_name = input('Please Enter a Girls Name: ')
        adjective_five = input('Please Enter a Fifth Adjective: ')
        second_plural = input('Please Enter a Second Plural Noun: ')
        adjective_six = input("Please Enter a Sixth Adjective: ")
        third_plural = input('Please Enter a Third Plural Noun: ')
        number = input("Please Enter a Number from 1-50: ")
        another_name = input('Please Enter another Name: ')
        second_number = input("Please Enter a Second Number: ")
        fourth_plural = input('Please Enter a Fourth Plural: ')
        third_number = input('Please Enter a Third Number: ')
        last_plural = input('Please Enter a fifth Plural')
        print("*" * 42)
        strinserter(adjective_one, adjective_two, first_name, past_tense, second_name, adjective_three, adjective_four, plural_noun, large_animal, small_animal,
                    girls_name, adjective_five, second_plural, adjective_six, third_plural, number, another_name, second_number, fourth_plural, third_number, last_plural)
        break


inputfunction()
