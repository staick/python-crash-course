messages = ['hello', 'world', 'staick', 'github', 'stackoverflow', 'twitter']

def show_messages(messages):
    for message in messages:
        print(message, end=' ')
    print()

def send_messages(messages):
    sent_messages = []
    while messages:
        current_message = messages.pop()
        print(f"{current_message.title()} is sending.")
        sent_messages.append(current_message)
    return sent_messages

sent_messages = send_messages(messages[:])
print("\nsend_messages: ", end='')
show_messages(sent_messages)
print("messages: ", end='')
show_messages(messages)
  