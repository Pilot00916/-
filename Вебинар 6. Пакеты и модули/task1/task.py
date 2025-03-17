number = 1
string = 'Hello'


def global_changes():
    global number, string
    number = 5
    string = "Hello, dear friend"
    return number, string
