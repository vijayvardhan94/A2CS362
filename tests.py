import unittest
from check_pwd import check_pwd

class check_pwd_tests(unittest.TestCase):
  
  def test1(self):
    input = 'seven+7'
    self.assertFalse(check_pwd(input), msg=None)

  def test2(self):
    input = 'twenty@twenty_TWENTY-twenty1'
    self.assertFalse(check_pwd(input), msg=None)
    
  def test3(self):
    input = '1aB@mmmm'
    self.assertTrue(check_pwd(input), msg=None)
    
  def test3A(self):
    input = '~`!@#$%^&*()_+-='
    self.assertFalse(check_pwd(input), msg=None)
    
  def test4(self):
    input = 'alllowercaseletters'
    self.assertFalse(check_pwd(input), msg=None)
    
  def test5(self):
    input = 'ALLCAPLETTERS'
    self.assertFalse(check_pwd(input), msg=None)
    
  def test6(self):
    input = '1234567890'
    self.assertFalse(check_pwd(input), msg=None)
    
  def test7(self):
    input = 'NOLOWER@$90'
    self.assertFalse(check_pwd(input), msg=None)
  
  def test8(self):
    input = 'nouppr*()10'
    self.assertFalse(check_pwd(input), msg=None)
    
  def test9(self):
    input = 'no#$ANYWHERE'
    self.assertFalse(check_pwd(input), msg=None)
    
  def test10(self):
    input = 'NOsymbols321'
    self.assertFalse(check_pwd(input), msg=None)
  
  def test11(self):
    input = '$mF0!gK89'
    self.assertTrue(check_pwd(input), msg=None)
    
  def test12(self):
    input = '!@34ajK'
    self.assertFalse(check_pwd(input), msg=None)
    
  def test13(self):
    input = '@$tr0NAUT3opp8*cow4dinner'
    self.assertFalse(check_pwd(input), msg=None)
    
  def test14(self):
    input = '$@$cookNOW03'
    self.assertTrue(check_pwd(input), msg=None)
if __name__ == '__main__':
  unittest.main()
