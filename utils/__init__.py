import numpy as np
import random
import torch

def setSeed(seed):
    # for random seed
    np.random.seed(seed)
    random.seed(seed)    
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def cprint(str, bold=False, underline=False, color=''):
    color_encoding = ''
    if color == 'blue':
        color_encoding = bcolors.OKBLUE
    elif color == 'cyan':
        color_encoding = bcolors.OKCYAN
    elif color == "orange":
        color_encoding = bcolors.WARNING
    elif color == 'red':
        color_encoding = bcolors.FAIL
    bold_encoding = bcolors.BOLD if bold else ''
    underline_encoding = bcolors.UNDERLINE if underline else ''
    print(bold_encoding + underline_encoding + color_encoding + str + bcolors.ENDC)
