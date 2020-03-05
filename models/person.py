class Person():
  name: None
  nick_name: None
  email_address: None
  mobile_number: None

  def toString(self):
    return self.name + "\t" + self.email_address + "\t" + self.mobile_number

  def fromString(self, text):
    parts = text.split("\t")
    self.name = parts[0]
    self.email_address = parts[1]
    self.mobile_number = parts[2]