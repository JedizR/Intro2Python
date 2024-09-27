"""
AI Training Simulator

This game simulates the process of training an AI model for image 
classification. Users will label images, select a model architecture, 
choose hyperparameters, and simulate training with random factors 
influencing accuracy and loss.
"""

import sys
import termios
import tty
import os
import random

# Constants
DEFAULT_EPOCHS = 5
STARTING_ACCURACY = 50  # in percentage
INITIAL_LOSS_MIN = 0.5
INITIAL_LOSS_MAX = 1.0
MODEL_EFFECTS = {
    'VGG16': 1.2,
    'ResNet50': 1.4,
    'MobileNetV2': 1.1,
}
LOSS_FUNCTION_EFFECTS = {
    'CrossEntropyLoss': 0.8,
    'BCEWithLogitsLoss': 0.85,
    'NLLLoss': 0.9,
    'BCELoss': 0.95,
}
LEARNING_RATE_EFFECTS = {
    0.001: 20.0,
    0.005: 4.0,
    0.01: 2.0,
    0.05: 0.4,
    0.1: 0.2,
}

# Global variables for user choices and their effects
learning_rate = None
learning_rate_effect = None
model_architecture = None
model_architecture_effect = None
loss_function_choice = None
loss_function_effect = None

# MNIST-like dataset: 32x32 ASCII images of handwritten digits
mnist_dataset = [
    {'label': '',
     'image': '''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@#+=#@@@@@@@@@@@@@
@@@@@@@@@@@@@#-...:+@@@@@@@@@@@@
@@@@@@@@@@@@#-. ...*@@@@@@@@@@@@
@@@@@@@@@@@@*...:..=%@@@@@@@@@@@
@@@@@@@@@@@#-.:#%+:.-#@@@@@@@@@@
@@@@@@@@@@%+..=@@@%+.-@@@@@@@@@@
@@@@@@@@@@%=.-%@@@@#-.=@@@@@@@@@
@@@@@@@@@@%=.-@@@@@%=.:%@@@@@@@@
@@@@@@@@@@%=.-@@@@@%=..+@@@@@@@@
@@@@@@@@@@%=.-@@@@@#-.:#@@@@@@@@
@@@@@@@@@@@=.-@@@@#-..-@@@@@@@@@
@@@@@@@@@@@=.:*#+-..:+%@@@@@@@@@
@@@@@@@@@@@%*======+#@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''},
    {'label': '',
     'image': '''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@+:..-*@@@@@@@@@@
@@@@@@@@@@@@@@@@:...:*@@@@@@@@@@
@@@@@@@@@@@@@@@%:...-#@@@@@@@@@@
@@@@@@@@@@@@@@@%:..:*@@@@@@@@@@@
@@@@@@@@@@@@@@@-...=%@@@@@@@@@@@
@@@@@@@@@@@@@%+...=#@@@@@@@@@@@@
@@@@@@@@@@@@%+....*@@@@@@@@@@@@@
@@@@@@@@@@@@%-...:*@@@@@@@@@@@@@
@@@@@@@@@@@%=...:*@@@@@@@@@@@@@@
@@@@@@@@@@@*....@@@@@@@@@@@@@@@@
@@@@@@@@@@@*:...%@@@@@@@@@@@@@@@
@@@@@@@@@@@%+:..#@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''},
    {'label': '',
     'image': '''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@%*=-==-=++*%@@@@@@@@@@
@@@@@@%+:.:=+#@@@@@#=.:*@@@@@@@@
@@@@@@*-=*%@@@@@@@@@*..+@@@@@@@@
@@@@@@@@@@@@@@@@@@@@+...#@@@@@@@
@@@@@@@@@@@@@@@@@@@*-..+@@@@@@@@
@@@@@@@@@@@@@@@@@@+:.:=%@@@@@@@@
@@@@@@@@@@@@@@%#*-..:=%@@@@@@@@@
@@@@@@@@@#=-:......:-:::-*%@@@@@
@@@@@@#+:.......:=*%@@@%+-:=#@@@
@@@@@#........:*@@@@@@@@@@*=*@@@
@@@@@@%*+=+*#%@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''},
    {'label': '',
     'image': '''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@%%#*+==:.:==+%@@@@@@@
@@@@@@@@@@#-.......::::.:#@@@@@@
@@@@@@@@@@%++**#%%@@%+:.:%@@@@@@
@@@@@@@@@@@@@@@@%*=:...-%@@@@@@@
@@@@@@@@@@@@%+-:....-*%@@@@@@@@@
@@@@@@@@@@@@*..::--.:+%@@@@@@@@@
@@@@@@@@@@@@@%%@@@@%+:-@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@%+.%@@@@@@@@
@@@@%++%@@@@@@@@@@@%=.-%@@@@@@@@
@@@%=:*@@@@@@@@@@%=..-%@@@@@@@@@
@@@@*..::----==-:..-*%@@@@@@@@@@
@@@@@#=-::....:-=+%@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''},
    {'label': '',
     'image': '''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@*-..*@@@@@@@@
@@@@@@@@@@@@@@@@@@=...:#@@@@@@@@
@@@@@@@@@@@@@@@@#-....:@@@@@@@@@
@@@@@@@@@@@@@@@*.:+#+.-@@@@@@@@@
@@@@@@@@@@@@%+..=%@*-:#@@@@@@@@@
@@@@@@@@@@#+::+%@@#-:+@@@@@@@@@@
@@@@@@@@%=..=@@@@#-.-#%+:=%@@@@@
@@@@@@%-.::.:=**+:...::+#@@@@@@@
@@@@@%::+%@#=-:...=*%@@@@@@@@@@@
@@@@@@%@@@@@@%-..#@@@@@@@@@@@@@@
@@@@@@@@@@@@%=..#@@@@@@@@@@@@@@@
@@@@@@@@@@@@*.:*@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''},
    {'label': '',
     'image': '''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@%#+++*%@@@
@@@@@@@@@@@@@@%###*=:...----+@@@
@@@@@@@@@@@%+:......:=*@@@@@@@@@
@@@@@@@@@@@#-..+%%@@@@@@@@@@@@@@
@@@@@@@@@@@+..-%@@@@@@@@@@@@@@@@
@@@@@@@@@@+:...:::::-*@@@@@@@@@@
@@@@@@@@@@#=::::-=-..-%@@@@@@@@@
@@@@@@@@@@@@@@@@@@+:.-%@@@@@@@@@
@@@@@@@@@@@@@@@@@#-..=@@@@@@@@@@
@@@@@@@@@%@@@@@@#-..-%@@@@@@@@@@
@@@@@@@+..=#@@#:...-*@@@@@@@@@@@
@@@@@@@*.........:+%@@@@@@@@@@@@
@@@@@@@@@#+===+#@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''},
    {'label': '',
     'image': '''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@#+-.:+@@@@@@@@@@
@@@@@@@@@@@@@@%=....:*@@@@@@@@@@
@@@@@@@@@@@@@#...::=#@@@@@@@@@@@
@@@@@@@@@@@%+:.:#%@@@@@@@@@@@@@@
@@@@@@@@@@%=..-@@@@@@@@@@@@@@@@@
@@@@@@@@@%-..-@@@@@@@@@@@@@@@@@@
@@@@@@@@@%-.:+@@@@@@@@@@@@@@@@@@
@@@@@@@@@=..-%@@@*-...:#@@@@@@@@
@@@@@@@@@+:.:=*-:.:--:..#@@@@@@@
@@@@@@@@@%-....:=#@@%=. -%@@@@@@
@@@@@@@@@@%=....:-=*+...#@@@@@@@
@@@@@@@@@@@@#+=-.....-*@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''},
    {'label': '',
     'image': '''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@%%@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@-..:-=*%@%%%#+-+@@@@@@@@@
@@@@@@@%**+-:.........-@@@@@@@@@
@@@@@@@@@@@@@@%#%@@*-:+@@@@@@@@@
@@@@@@@@@@@@@@@@@@#-.-%@@@@@@@@@
@@@@@@@@@@@@@@@@@@+::*@@@@@@%%@@
@@@@@@@@@+=------:...:------:=@@
@@@@@@@@@=-=====+:.:=*#%%%%@@@@@
@@@@@@@@@@@@@@@@+::*@@@@@@@@@@@@
@@@@@@@@@@@@@@@%:.=%@@@@@@@@@@@@
@@@@@@@@@@@@@@%:.-#@@@@@@@@@@@@@
@@@@@@@@@@@@@#:..*@@@@@@@@@@@@@@
@@@@@@@@@@@@@#:.-#@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''},
    {'label': '',
     'image': '''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@%%%%%@@@@@@@@@@@@
@@@@@@@@@@%*+-......=@@*:%@@@@@@
@@@@@@@#=::-=++****-=#=.*@@@@@@@
@@@@@@%:.:*@@@@@@@#*+:-@@@@@@@@@
@@@@@@@*:..:-*@@@@%=.=@@@@@@@@@@
@@@@@@@@@%*=:.:-**--*@@@@@@@@@@@
@@@@@@@@@@@@@%*-...+@@@@@@@@@@@@
@@@@@@@@@@@@@@@+::.-*@@@@@@@@@@@
@@@@@@@@@@@@@%=.+%+:=@@@@@@@@@@@
@@@@@@@@@@@@%+:*@@@=:*@@@@@@@@@@
@@@@@@@@@@@@*:+@@@%=:*@@@@@@@@@@
@@@@@@@@@@@%+:+**+-:=%@@@@@@@@@@
@@@@@@@@@@@@%=.  .=#@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'''},
    {'label': '',
     'image': '''@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@%*+==:-=+%@@@@@@@@
@@@@@@@@@@%*=::-=+*++=:.-*@@@@@@
@@@@@@@@%-:=*@@@@@@@@@@@+:=#@@@@
@@@@@@@*:+%@@@@@@@@@@%+:#*=*@@@@
@@@@@@*.-%@@@@@@@@%*=-.:%@@@@@@@
@@@@@@#.:*####%*-:....-@@@@@@@@@
@@@@@@@#=:....:=+#%+:-%@@@@@@@@@
@@@@@@@@@@@@@@@@@@#--%@@@@@@@@@@
@@@@@@@@@@@@@@@@@%-.=@@@@@@@@@@@
@@@@@@@@@@@@@@@@@*:-#@@@@@@@@@@@
@@@@@@@@@@@@@@@@#:.+@@@@@@@@@@@@
@@@@@@@@@@@@@@@@#:-#@@@@@@@@@@@@
@@@@@@@@@@@@@@@@%#%@@@@@@@@@@@@@'''},
]

MAIN_MENU_BANNER = r'''    _    ___   _____          _       _             
   / \  |_ _| |_   _| __ __ _(_)_ __ (_)_ __   __ _ 
  / _ \  | |    | || '__/ _` | | '_ \| | '_ \ / _` |
 / ___ \ | |    | || | | (_| | | | | | | | | | (_| |
/_/   \_\___|   |_||_|  \__,_|_|_| |_|_|_| |_|\__, |
   ____  _                 _       _          |___/ 
  / ___|(_)_ __ ___  _   _| | __ _| |_ ___  _ __    
  \___ \| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|   
   ___) | | | | | | | |_| | | (_| | || (_) | |      
  |____/|_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|      
  
  An Image Classification AI Training Simulator
                    
                    (S)tart
                    (Q)uit
  
'''


def getch():
    """
    Get a single character from standard input without waiting for a newline.
    
    :return: The character input by the user.
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def main_menu():
    """
    Display the main menu and handle user input to start the game or quit.
    """
    os.system('clear')
    print(MAIN_MENU_BANNER)
    key = getch().lower()
    if key == 's':
        data_labeling()
    elif key == 'q':
        exit(0)
    else:
        main_menu()


def data_labeling():
    """
    Loop through the dataset and prompt the user to label each image.
    """
    os.system('clear')
    for data in mnist_dataset:
        print('Let\'s label this image!\n')
        print(data["image"], '\n')
        while data["label"] == '':
            data["label"] = input('Enter label: ')
        print('\nDONE! Press ANY to Continue...')
        getch()
        os.system('clear')
    print('All images labeled! Press ANY to Continue...')
    getch()
    select_architecture()


def select_architecture():
    """
    Prompt the user to select a model architecture and set its effect.
    """
    os.system('clear')
    print('Choose a pretrained model')
    for i, choice in enumerate(MODEL_EFFECTS, 1):
        print(f'{i}. {choice}')

    valid_input = False
    while not valid_input:
        model_key = getch().lower()
        if model_key in ['1', '2', '3']:
            valid_input = True

    global model_architecture, model_architecture_effect
    model_architecture = list(MODEL_EFFECTS.keys())[int(model_key) - 1]
    model_architecture_effect = MODEL_EFFECTS[model_architecture]

    print(f'You chose {model_architecture} as a model')
    print('\nPress ANY to Continue...')
    getch()
    set_hyperparameters()


def select_loss_function():
    """
    Prompt the user to select a loss function and set its effect.
    """
    os.system('clear')
    print('Choose a loss function')
    print('Loss Function is the measure of how well the model performs')

    for i, choice in enumerate(LOSS_FUNCTION_EFFECTS, 1):
        print(f'{i}. {choice}')

    valid_input = False
    while not valid_input:
        loss_function_key = getch().lower()
        if loss_function_key in ['1', '2', '3', '4']:
            valid_input = True

    global loss_function_choice, loss_function_effect
    loss_function_keys = list(LOSS_FUNCTION_EFFECTS.keys())
    loss_function_choice = loss_function_keys[int(loss_function_key) - 1]
    loss_function_effect = LOSS_FUNCTION_EFFECTS[loss_function_choice]

    print(f'You chose {loss_function_choice} as a loss function')
    print('\nPress ANY to Continue...')
    getch()


def select_learning_rate():
    """
    Prompt the user to select a learning rate and set its effect.
    """
    os.system('clear')
    print('Choose a learning rate')
    print('Learning Rate is the step size at which the model learns')

    for i, rate in enumerate(LEARNING_RATE_EFFECTS, 1):
        print(f'{i}. {rate}')

    valid_input = False
    while not valid_input:
        lr_key = getch().lower()
        if lr_key in ['1', '2', '3', '4', '5']:
            valid_input = True

    global learning_rate, learning_rate_effect
    learning_rate = list(LEARNING_RATE_EFFECTS.keys())[int(lr_key) - 1]
    learning_rate_effect = LEARNING_RATE_EFFECTS[learning_rate]

    print(f'You chose {learning_rate} as the learning rate')
    print('\nPress ANY to Continue...')
    getch()


def set_hyperparameters():
    """
    Initiate the process of selecting hyperparameters for the model.
    """
    os.system('clear')
    print('Start specifying hyperparameters for your model!')
    print('\nPress ANY to Continue...')
    getch()
    select_loss_function()  # First Parameter: Loss Function
    select_learning_rate()  # Second Parameter: Learning Rate

    print(f'\nModel: {model_architecture}')
    print(f'Loss Function: {loss_function_choice}')
    print(f'Learning Rate: {learning_rate}')
    print('\nPress ANY to Start Training...')
    getch()
    training_simulation()


def training_simulation():
    """
    Simulate the training process over a set number of epochs, updating 
    accuracy and loss based on the selected hyperparameters and random 
    factors.
    """
    os.system('clear')
    print(f'Starting training simulation with {model_architecture}...')
    print(f'Using {loss_function_choice} loss function and learning '
          f'rate {learning_rate}...\n')

    accuracy = STARTING_ACCURACY
    loss = random.uniform(INITIAL_LOSS_MIN, INITIAL_LOSS_MAX)

    for epoch in range(1, DEFAULT_EPOCHS + 1):
        os.system('clear')
        print(f'Epoch {epoch}/{DEFAULT_EPOCHS}')

        accuracy_gain = calculate_accuracy_gain()
        loss_reduction = calculate_loss_reduction()

        accuracy = update_accuracy(accuracy, accuracy_gain)
        loss = update_loss(loss, loss_reduction)

        print(f'Accuracy: {accuracy:.2f}%')
        print(f'Loss: {loss:.4f}\n')

        print('Press ANY to Continue to Next Epoch...')
        getch()

    print(f'Training complete! Final accuracy: {accuracy:.2f}%, Final loss: '
          f'{loss:.4f}')
    print('\nPress ANY to Finish...')
    getch()
    main_menu()


def calculate_accuracy_gain():
    """
    Calculate the accuracy gain based on the selected hyperparameters 
    and random factors.
    
    :return: Accuracy gain value.
    """
    return random.uniform(2, 5) * model_architecture_effect * \
           loss_function_effect * learning_rate_effect


def calculate_loss_reduction():
    """
    Calculate the loss reduction based on the selected hyperparameters 
    and random factors.
    
    :return: Loss reduction value.
    """
    return random.uniform(0.05, 0.2) * model_architecture_effect * \
           loss_function_effect * learning_rate_effect


def update_accuracy(accuracy, gain):
    """
    Update the accuracy with a gain, clamping it between 0% and 100%.
    
    :param accuracy: Current accuracy.
    :param gain: Accuracy gain to be added.
    :return: Updated accuracy.
    """
    new_accuracy = accuracy + gain
    return max(0, min(100, new_accuracy))


def update_loss(loss, reduction):
    """
    Update the loss with a reduction, ensuring it does not go negative.
    
    :param loss: Current loss.
    :param reduction: Loss reduction to be subtracted.
    :return: Updated loss.
    """
    new_loss = loss - reduction
    return max(0, new_loss)


# Start the game by calling the main menu
main_menu()
