class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
    
class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
  
  def __repr__(self):
    return 'This restaurant is located at ' + self.address
  
  def available_menus(self, time):
    available_menu = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menu.append(menu)
    return available_menu
  
class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name 
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    
  def __repr__(self):
    if self.start_time <= 1200:
    	start_daytime = 'am'
    else:
      start_daytime = 'pm'
    if self.end_time <= 1200:
    	end_daytime = 'am'
    else:
      end_daytime = 'pm'
    return self.name + ' is a available from ' + str(int(self.start_time / 100)) + start_daytime + ' to ' + str(int(self.end_time / 100)) + end_daytime
  
  def calculate_bill(self, purchased_items):
    bill = 0
    for purshased_item in purchased_items:
      if purshased_item in self.items:
        bill += self.items[purshased_item]
    return bill
  
  pass

#brunch_items
brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

#early_bird_items
early_bird_items =  {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00}

#diner_items
dinner_items = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00}

#kids_items
kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

# Take a Arepa_items
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
