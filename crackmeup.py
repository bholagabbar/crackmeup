from randomjoke_dot_com import all_categories
import random

categories = {'Random':'haha', 'One Liners':'oneliners', 'True Stories':'news',
'Signs of Our Times':'signs', 'Nerdy Jokes':'nerd','Quotes':'quotes',
'Professional':'professional', 'Light Bulb':'lightbulb', 
'Gender Battles':'couples', 'Riddles':'riddles', 'Religion':'religion',
'Gross':'gross', 'Blondes':'blonde', 'Politics':'politics', 'Just do it':'doit',
'Laws':'laws', 'PG 13':'dirty', 'Racist':'ethnic'}

random_category = categories[random.choice(categories.keys())]

print all_categories.getJoke(random_category)