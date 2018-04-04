# https://www.interviewcake.com/question/python/reverse-words?utm_source=weekly_email&utm_source=drip&utm_campaign=weekly_email&utm_campaign=Interview%20Cake%20Weekly%20Problem%20%23185:%20Reverse%20Words&utm_medium=email&utm_medium=email
# You're working on a secret team solving coded transmissions.

# Your team is scrambling to decipher a recent message, worried it's a plot to break into a major European National Cake Vault. The message has been mostly deciphered, but all the words are backwards! Your colleagues have handed off the last step to you.

# Write a function reverse_words() that takes a message as a list of characters and reverses the order of the words in-place. ↴
# When writing your function, assume the message contains only letters and spaces, and all words are separated by one space.

message = [ 'c', 'a', 'k', 'e', ' ',
        'p', 'o', 'u', 'n', 'd', ' ',
        's', 't', 'e', 'a', 'l' ]


def reverse_words(msg):
    words = []
    # Break message into words
    words = str().join(msg).split(' ')
    # Reverse the order of the words
    words.reverse()
    # Put the new order words into list format
    words = list(str().join(words))
    # Assign the message to the new order
    msg[:] = words

if __name__ == "__main__":
    reverse_words(message)
    print("{}".format(message))
    