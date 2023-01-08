#function to take integer and change to binary nunmber, but in reverse order
def int_to_reverse_binary(integer_value):
  result = ""
  
  while integer_value > 0:
    remainder = integer_value % 2
    result = result + str(remainder)
    integer_value = integer_value //2
  return result;
  
#function that reverses binary number in the correct way
def string_reverse(result):
  return result[::-1];
  
#main body of script
if __name__ == '__main__':
  #gets user input as an integer
  integer_value = int(input())
  
  #replays user input to int_to_reverse_binary function
  input_string = int_to_reverse_binary(integer_value)
  #relays input_string to string_reverse function to get actual binary number
  correct_binary_value = string_reverse(input_string)
  
  #prints final binary number obtained from string_reverse function
  print(correct_binary_value)
