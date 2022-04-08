import sys

def use_args():
    if sys.argv[1] =='-l':
        print('I use a line of a song')
    elif sys.argv[1] == '-f':
        print(f'I use lyrics from the text file {sys.argv[2]}')



if __name__ == '__main__':  # this is for defining things
    use_args()
