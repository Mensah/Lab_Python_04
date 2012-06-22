#question 1
groceries = ['bananas', 'strawberries', 'apples', 'bread']

# adding champagne
groceries.insert(4, 'champagne')

print "-----------"

#removing bread
groceries.remove('bread')

print "-----------"

#looking for apples and strawberries
aisle = ['a', 'b', 'c', 's']

#sorting both aisle and groceries into alphabetical order
aisle.sort()
groceries.sort()

#arranging the items within their aisle where an alphabet example a represents all things in aisle a
a = {}
for index in range(4):
    res={aisle[index]:grocer[index]}
    a[aisle[index]] = grocer[index]

print a


print "-----------"
#question 2
#Would use list dictionaries to design the catalog because it would allow me to easily change information in the catalog easily if i have to.

item = ['Apple', 'Bananas', 'Bread', 'Carrots', 'Champagne','Strawberries']
prices = [7.3, 5.5, 1.0, 10.0, 20.90, 32.6]
catalog = {}
for index in range(len(items)):
    r = {item[index]:prices[index]}
    catalog[item[index]] = prices[index]
print catalog


 catalog['Strawberries']=63.43
 catalog['Chicken'] = 6.5

 
#question 3
 #list for the CEO
 in_stock = ['Apples', 'Bananas', 'Bread', 'Carrots', 'Champagne', 'Strawberries']
 always_in_stock = (in_stock)

print "Come to shoprite! We always sell:"
for c in range(len(alway_in_stock)):
    print always_in_stock[c]


 
