import re

extract = ()
user_words = ()
read_text = ""
file_path = ""

# Welcome Function
def welcome():
    """
    This function prints out the welcome message and game explination to the user.
    """

    print(
    """
    Welcome to Madlib game!

    To play, read the story, then simply input words matching the description inside the {Brackets} with the same exact order
    and the game will convert it to your own version of the story!

    """
    )


def read_template(path):
    """
    This Function Reads the Story text file.    
    """

    global file_path
    file_path = path
    try:
        with open(file_path, "r") as f:
            global read_text
            read_text = f.read()
            return (read_text)
    except:
        raise FileNotFoundError


def parse_template(input_text):
    """
    This Function prepares the story text for user inputs.
    """
    pattern = r"{([A-Za-z0-9\s'-]+)}"
    global extract
    global read_text
    input_text = read_text
    extract = re.findall(pattern, input_text)
    
    with open(file_path, "r") as fin, open("assets/bare_template.txt", "w+") as fout:
        for line in fin:
            for word in extract:
                line = line.replace(word, "")
            fout.write(line)
      
    return (read_template("assets/bare_template.txt"), tuple(extract))


def prompt_user(path):
    """
    This function stores user inputs.
    """

    """
    """
    print (
     """
    Tell your own version of the story!
    """
    )

    print(
        read_template(path)
    )

    for word in extract:
        print()
        user_word = input(f"Replace the word {word}: > ")
        global user_words
        user_words += (user_word,)


def merge(bare_text, user_inputs):
    """
    This Function Merges user inputs with the story-line and prints it out.
    """
    user_inputs = list(user_inputs)
    with open("assets/bare_template.txt", "r") as fin, open("assets/filled_template.txt", "w+") as fout:
        for line in fin:
            for character in line:
                if character == "{":
                    character = user_inputs[0]
                    user_inputs.pop(0)
                if character == "}":
                    character = ""
                fout.write(character)
                 

    filled_story =(read_template("assets/filled_template.txt"))
    print (filled_story)
    return (filled_story)




if __name__ == "__main__":
    # file_path = "assets/dark_and_stormy_night_template.txt"
    # welcome()
    # read_template(file_path)
    # parse_template(read_template(file_path))
    # prompt_user(file_path)
    # merge(read_template("assets/bare_template.txt"), user_words)

    path = "assets/make_me_a_video_game_template.txt"
    welcome()
    read_template(path)
    parse_template(read_text)
    prompt_user(path)
    merge(read_template("assets/bare_template.txt"), user_words)

    