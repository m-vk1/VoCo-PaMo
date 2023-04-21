import speech_recognition as sr
import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Style
import pandas as pd
import os
import pyttsx3


########## Voice Recognition ##########

def start_listening(df,excel_path):
    '''
    Takes in the excel file path and the dataframe
    Listens to the user's voice command
    Converts the voice command to text
    Extracts the parameters from the excel file
    Checks if the command contains any of the parameters
    If yes, then updates the excel file
    '''
    r = sr.Recognizer()
    
    # Prompt user to give a command
    with sr.Microphone() as source:
        print("Please give a command:")
        audio = r.listen(source)
        try:
            command_text = r.recognize_google(audio,language="en-IN")
        except sr.UnknownValueError:
            print("Could not understand audio")
            result = None
            command_text = None
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            result = None
            command_text = None

    # Extract the parameters from the excel file
    params = parameter_extracter(excel_path)

    # Check if the command contains any of the parameters
    if command_text is not None:
        for i in range(len(params)):
            # update the excel file if the command contains a parameter
            if params[i].casefold() in command_text:
                change = params[i]
                ind = df[df["Parameter"] == params[i]].index.values[0]
                number = df.at[ind, "Value"]
                result = voice_command(command_text=command_text, number=number)
                df.at[ind, "Value"] = result
                df.to_excel(excel_path, index = False)
    elif command_text is None:
        print("Invalid command")
        result = None
    
    # Update the GUI and say the result
    if result is not None:
        text.config(text = f"The new {change} is {result}")
        cost = round((df.at[0, "Value"]*1.2 + df.at[1, "Value"]*4.5 + df.at[2, "Value"]*2.3)/100,2)
        output = f"The new {change} is {result} and The new cost is {cost} million dollars"
        engine = pyttsx3.init()
        engine.say(output)
        engine.runAndWait()
    elif result is None or command_text is None:
        text.config(text = "Please try again :(")


################ Interpreting Voice Commands ################

def voice_command(command_text, number):
    '''
    Takes in the voice command transcript and the number to be changed to
    Interprets the voice command
    Returns the result
    '''
    if 'double' in command_text:
        result = number * 2
    elif 'increase' in command_text:
        increase_by = float(command_text.split()[-1])
        result = number + increase_by
    elif ('time' or 'times' or 'x' or '*') in command_text:
        times_by = float(command_text.split()[0])
        result = number * times_by
    elif 'decrease' in command_text:
        decrease_by = float(command_text.split()[-1])
        result = number - decrease_by
    elif 'triple' in command_text:
        result = number * 3
    elif 'half' in command_text:
        result = number / 2
    elif 'change' in command_text:
        new_number = float(command_text.split()[-1])
        result = new_number 
    else:
        print("Invalid command")
        result = number
    print(result)
    return result

#################### Miscelaneous ####################

def extract_file_path(file_name):
    '''
    Extracts the file path from the dynamo file
    '''
    with open(file_name, "r") as file:
        content = file.read()
        index_1 = content.find("HintPath")
        index_2 = content.find("InputValue")

        start = index_1 + len("HintPath") + 4
        end = index_2 - 10
        x = content[start:end]
    x = str(x)
    x = os.path.normpath(x)
    return x

def parameter_extracter(excel_path):
    '''
    Extracts the parameters from the excel file
    '''
    parameter_list = []
    df = pd.read_excel(excel_path)
    for i in range(len(df)):
        parameter_list.append(df.at[i, "Parameter"])
    return parameter_list

######################################################

########### GUI #############

def close_window():
    root.destroy()

def load_dynamo_file():
    root.filename1 = filedialog.askopenfilename(title = "Select a Dynamo File", filetypes = (("Dynamo files", "*.dyn"), ("all files", "*.*")))
    global excel_filepath
    global df
    excel_filepath = extract_file_path(root.filename1)
    params = parameter_extracter(excel_filepath)
    #text.config(text = f"Please give a command containing \nany of the following parameters:")
    text.config(text= f"\n".join(params))
    df = pd.read_excel(excel_filepath)
    listen_button.config(state = "normal")
    


root = tk.Tk()
root.geometry("375x180")
root.title("VoCo PaMo")
style = Style()
style.theme_use("alt")

text = tk.Label(root, text = "Select a dynamo file and then, \nclick on the mic button \neverytime you want to give an instruction.", font = ("Segoe UI", 10))
dynamo_button = tk.Button(root, text = "Load Dynamo File", command = load_dynamo_file, relief=tk.RAISED)
listen_button = tk.Button(root, text="\U0001F3A4", font=("Segoe UI Emoji", 20), state="disabled", command = lambda: start_listening(df,excel_filepath) , relief=tk.RAISED)
close_button = tk.Button(root, text = "Close", command = close_window, relief=tk.RAISED)

text.place(relx = 0.5, rely = 0.2, anchor = "center")
dynamo_button.place(relx = 0.18, rely = 0.9, anchor = "center")
listen_button.place(relx = 0.5, rely = 0.6, anchor = "center")
close_button.place(relx = 0.90, rely = 0.9, anchor = "center")

root.mainloop()