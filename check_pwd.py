def check_pwd(input):
  signs = '~`!@#$%^&*()_+-='
  if len(input) < 8 or len(input) > 20:
      return False
  lowercase_letters = [lwrcse for lwrcse in input if lwrcse.islower()]
  uppercase_letters = [uprcse for uprcse in input if uprcse.isupper()]
  digits = [dig for dig in input if dig.isdigit()]
  sign = [sign for sign in input if sign in signs]
  if len(lowercase_letters) > 0 and len(uppercase_letters) > 0 and len(digits) > 0 and len(signs) > 0:
      return True
  else:
      return False
