def check_number(number):
    number_length = len(number)
    if number_length == 9 or (number_length == 13 and number[:4] == "+420"):
        return True
    else: 
        return False
    
def count_message_price(message):
    message_length = len(message)
    paid_message_length = 180
    message_price_count = 0

    if message_length > 0:
    
        should_count = True
        while(should_count):
            message_price_count += 1
            message_length -= paid_message_length
            if message_length < 1:
                should_count = False
        print(f"Message price: {message_price_count*3}")
    else:
        print("Cannot send empty message")


print("Please enter the number: ")
number_input = input()

if check_number(number_input):
    print("Please enter the message: ")
    message_input = input()
    count_message_price(message_input)
else:
    print("Please enter number in right format") 
    


