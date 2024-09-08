"""
We want you to write a function, organizeItems, that organizes items by category. The argument to the function is an array of item objects. Each item object has 3 properties, category (string), itemName (string), and onSale (Boolean).
Here's an example:
var itemData = [
  { category: 'fruit',  itemName: 'apple', onSale: false },
  { category: 'canned', itemName: 'beans', onSale: false },
  { category: 'canned', itemName: 'corn',  onSale: true  },
  { category: 'frozen', itemName: 'pizza', onSale: false },
  { category: 'fruit',  itemName: 'melon', onSale: true  },
  { category: 'canned', itemName: 'soup',  onSale: false },
];
The return value should be an object with category properties. Each property value is an array of items that belong to that category.
Here's an example return object based on our example input:
{
  fruit:  ['apple', 'melon($)'],
  canned: ['beans', 'corn($)', 'soup'],
  frozen: ['pizza']
};
Note that items having onSale set to true should have '($)' appended to their item name.

Please complete the function organizeItems and validate it is working by running the tests.Your function should work for any similarly formatted input data, not just the example data we've provided.
"""

# I am going to solve this question in Python. The recommended time is 20 minutes. If I go over it, I fail.