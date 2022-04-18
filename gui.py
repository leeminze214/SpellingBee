from tkinter import *
import random
from tkinter.messagebox import *

##uncomment line 90 to CHEAT and have answers printed :)

def change_difficulty_label(self):
    
    difficulty_scale_labels = ['easy','medium','hard']
    difficulty_choice= difficulty_scale_var.get()
    difficulty = difficulty_scale_labels[difficulty_choice]
    difficulty_scale.config(label = difficulty)



def get_list_of_difficulty_words(words,difficulty):
    
    final = []
    length_cutoff = None
    
    if difficulty == 0:
        length_cutoff = [1,5]
        
    elif difficulty == 1:
        length_cutoff = [4,10]
        
    else:
        length_cutoff = [8,20]
        
    for i in words:
            if len(i) >= length_cutoff[0] and len(i) <= length_cutoff[1]:
                final.append(i)
    
    return final


    
def get_list_of_words():
    
    global animals,countries,food,list_of_words
    
    theme =themes_option_var.get()
    difficulty =difficulty_scale_var.get()
    
    if theme == 'random':
        themes = ['ANIMALS','COUNTRIES','FOOD']
        random_theme = random.choice(themes)
        themes_option_var.set(random_theme)
        list_of_words = get_list_of_words()
        
    elif theme == 'ANIMALS':
        list_of_words =get_list_of_difficulty_words(animals,difficulty)

    elif theme == 'COUNTRIES':
        list_of_words = get_list_of_difficulty_words(countries,difficulty)      
        
    elif theme =='FOOD':
        list_of_words = get_list_of_difficulty_words(food,difficulty)
        
    if theme != 'random':
        themes_option_var.set(theme)
        
    return list_of_words



def set_word():
    
    global word,list_of_words
    
    words_left = len(list_of_words)
    
    if words_left == 0:
        showinfo('INFORMATION','WOW!\n You\'ve gone through every word in this theme+difficulty combination.')
        quit_or_not(force = True)
        
    else:
        word = list_of_words[random.randint(0,len(list_of_words)-1)]
        list_of_words.remove(word)
        final = []
        
        for i in range(len(word)):
            final.append([word[i],i])
            
        word =final
                
    ####UNCOMMENT THIS PRINT STATEMENT TO PRINT ANSWERS AND CHEAT :)
    ####print(''.join([i[0] for i in final]))
       


def clear_old_frame(new_theme = False):
    
    global list_of_check_boxes,user_word
    
    user_word = []
    user_word_var.set('')
    
    for i in list_of_check_boxes:
        i[0].grid_forget()
        
    if new_theme:
        score_var.set('Score: 0')

    list_of_check_boxes = []



def set_image():

    global countries_img,animals_img,food_img
    
    theme = themes_option_var.get()
    
    if theme == 'COUNTRIES':
        image.config(image=countries_img)
        
    elif theme == 'FOOD':
        image.config(image=food_img)
        
    elif theme == 'ANIMALS':
        image.config(image=animals_img)
        
    image.grid(row=3,column=2)


        
def create_new_check_boxes():
    
    global list_of_check_boxes,word
    
    for i in range(len(word)):
        letter = StringVar()
        tempcheck = Checkbutton(checkbox_group,text = 'temp',variable = letter, onvalue='temp',offvalue='temp',command = lambda letter = letter: update_user_word(letter))
        list_of_check_boxes.append([tempcheck,letter])


   
        
def create_letter_check_boxes():
    
    global list_of_check_boxes,word
    
    shuffle = random.sample(word,len(word))
    
    for i in range(len(word)):
        list_of_check_boxes[i][0].config(text = f'{shuffle[i][0]}',onvalue=shuffle[i],offvalue=shuffle[i][1])
        list_of_check_boxes[i][1].set(shuffle[i][1])
        list_of_check_boxes[i][0].grid(row=1,column=i)




def update_score():
    
    score = score_var.get().split()
    new_score =int(score[1])+1
    score_var.set(score[0]+' '+str(new_score))
    


def config_next_button(state):
    
    if state == 'normal':
        next_button.config(state = NORMAL)

    else:
        next_button.config(state = DISABLED)


        
def config_quit_button(state):
    
    if state == 'normal':
        quit_button.config(state = NORMAL)
        
    else:
        quit_button.config(state = DISABLED)


        
def config_check_boxes(state):
    
    global list_of_check_boxes
    
    if state == 'normal':
        for i in list_of_check_boxes:
            i[0].config(state = NORMAL)
            
    else:
        for i in list_of_check_boxes:
            i[0].config(state = DISABLED)



def config_settings(state):
    
    if state == 'normal':
        difficulty_scale.config(state = NORMAL)
        themes_option.config(state = NORMAL)
        timer_spin.config(state = 'readonly')
        play_button.config(state = NORMAL)
        easy_radio.config(state=NORMAL)
        medium_radio.config(state=NORMAL)
        hard_radio.config(state=NORMAL)
        
    else:
        difficulty_scale.config(state = DISABLED)
        themes_option.config(state = DISABLED)
        timer_spin.config(state = DISABLED)
        play_button.config(state = DISABLED)
        easy_radio.config(state=DISABLED)
        medium_radio.config(state=DISABLED)
        hard_radio.config(state=DISABLED)
  


def check_user_word(updated_word):
    
    global word
    
    word_string = ''
    
    for i in word:
        word_string+=i[0]

    if updated_word == word_string:
        update_score()
        config_next_button('normal')
        config_check_boxes('off')
        


def remove_letter_from_user_word(data):
    
    global user_word
    
    for i in user_word:
        
        if i[1] == data[0]:
            user_word.remove(i)



def update_user_word(letter):
    
    global user_word,list_of_check_boxes
    
    data = []
    data = letter.get().split()
    
    if len(letter.get()) == 5:
        data = [' ',letter.get()[4]]
        
    if len(data) == 1:
        updated_word = ''
        remove_letter_from_user_word(data)
        
        for i in user_word:
            updated_word += i[0]
            
        user_word_var.set(updated_word)
        
    else:
        user_word.append(data)
        updated_word = user_word_var.get()+data[0]
        user_word_var.set(updated_word)
        check_user_word(updated_word)



def quitting():
    
    config_settings('normal')
    config_next_button('off')
    config_quit_button('off')
    restartTimer()
    store_score()
    showinfo('RESULTS',f'You got {score_var.get().split()[1]} words correct!')
    update_scoreboard()
    clear_old_frame(new_theme = True)
    title_var.set('Press "PLAY" button to play')
    checkbox_group.grid_forget()
    image.grid_forget()
        
        
        
def quit_or_not(force = False):
    
    if force:
        quitting()
    else:
        result = askquestion('QUIT','Are you sur\ne you want to quit?')
        if result == 'yes':
            quitting()


        
def changeTimer():
    
    global AFTER
    
    time = int(timerVar.get().split()[1])

    time -= 1
    if time >= 0:
        timerVar.set(f'Timer: {time}')
        AFTER = root.after(1000, changeTimer)
        
    else:
        quit_or_not(force = True)


        
def startTimer():
    
    timer = timer_spin_var.get()
    if timer == '30 seconds':
        timerVar.set(f'Timer: 30')
        
    elif timer == '1 minute':
        timerVar.set(f'Timer: 60')
        
    elif timer == '3 minutes':
        timerVar.set(f'Timer: 180')
    
    changeTimer()

    
    
def restartTimer():
    
    global AFTER
    
    timerVar.set(f'Timer: NA')
    root.after_cancel(AFTER)

    
        
def store_score():
    
    global high_scores
    
    difficulty =difficulty_scale_var.get()
    timer = timer_spin_var.get()
    score = int(score_var.get().split()[1])
    group = high_scores[difficulty]
    
    group[0]+=score
    
    if timer == '30 seconds':
        group[1]+=score
        
    elif timer == '1 minute':
        group[2]+=score
        
    else:
        group[3]+=score


 
def update_scoreboard():
    
    global high_scores
    
    group = None
    difficulty = difficulty_highscore_var.get()
    
    if difficulty == 'Easy':
        group = high_scores[0]
        
    elif difficulty == 'Medium':
        group = high_scores[1]
        
    else:
        group = high_scores[2]
        
    total_var.set(f'Total: {group[0]}')
    thirty_var.set(f'30 seconds: {group[1]}')
    one_var.set(f'1 Minute1: {group[2]}')
    three_var.set(f'3 Minutes: {group[3]}')


        
def update_frame_new_word():
    
    set_image()
    title_var.set(themes_option_var.get())
    checkbox_group.grid(row=5,column=2,pady=30)
    config_settings('off')
    config_quit_button('normal')
    config_check_boxes('normal')
    config_next_button('off')
    set_word()
    clear_old_frame()
    create_new_check_boxes()
    create_letter_check_boxes()


    
def play():
    
    get_list_of_words()
    startTimer()
    update_frame_new_word()
    
   
    
    

#MAIN
global animals,countries,food,list_of_check_boxes, word, user_word,list_of_words,high_scores,AFTER,countries_img,animals_img,food_img

root = Tk()
root.title("jumblebee")
mainframe = Frame(root)
animals= ['Prawn', 'Tahr', 'Marmoset', 'Cephalopod', 'Urial', 'Monitor lizard', 'Moose', 'Wallaby', 'Quail', 'Meadowlark', 'Ptarmigan', 'Nightingale', 'Domestic pig','Hamster', 'Cricket', 'Galliform', 'Warbler', 'Barnacle', 'Jackal', 'Polar bear', 'Chinchilla', 'Kite', 'Shrimp', 'Gazelle', 'Arrow crab', 'Roadrunner', 'Vole', 'Dog', 'Slug', 'Crab', 'Otter', 'Kangaroo rat', 'Dung beetle', 'Takin', 'Blue whale', 'Sheep', 'Tern', 'Mongoose', 'Manatee', 'Manta ray', 'New World quail', 'Lab rat', 'Domestic guineafowl', 'Kingfisher', 'Zebra', 'Wildebeest', 'Goose', 'Ermine', 'Hermit crab', 'Domestic turkey', 'Worm', 'Toucan', 'Giraffe', 'Skink', 'Crow', 'Canid', 'Whippet', 'Fowl', 'Panthera hybrid', 'Bonobo', 'Cat', 'Jay', 'Deer', 'Stoat', 'Coyote', 'Salmon', 'Meerkat', 'Buffalo, African', 'Gecko', 'Antelope', 'Sparrow', 'Capybara', 'Water buffalo', 'Bald eagle', 'Cougar', 'Grasshopper', 'Parrotfish', 'Mandrill', 'Pheasant', 'Steelhead trout', 'Armadillo', 'Piranha', 'Alpaca', 'Domestic goat', 'Fancy mouse', 'Hedgehog', 'Komodo dragon', 'Ladybug', 'Marsupial', 'Beaked whale', 'Turtle', 'Guppy', 'Society finch', 'Squirrel', 'Angelfish', 'Silverfish', 'Cape buffalo', 'African elephant', 'Junglefowl', 'Leopard', 'Pigeon', 'Dragon', 'Bali cattle', 'Squid', 'Octopus', 'Boa', 'Rooster', 'Mouse', 'Mammal', 'Box jellyfish', 'Ocelot', 'Orca', 'Reptile', 'Blackbird', 'Magpie', 'Sea slug', 'Locust', 'Wombat', 'Red panda', 'Newt', 'African buffalo', 'Giant panda', 'Grouse', 'Badger', 'Koala', 'Sperm whale', 'Gayal', 'Shrew', 'Grizzly bear', 'Mule', 'Scorpion', 'Condor', 'Eagle', 'Bass', 'Bovid', 'Tuna', 'Antlion', 'Mole', 'Catshark', 'Turkey', 'Hawk', 'Iguana', 'Termite', 'Butterfly', 'Jellyfish', 'Marlin', 'Pelican', 'Praying mantis', 'Domestic Bactrian camel', 'Scale insect', 'list', 'Wildfowl', 'Tiger shark', 'Earwig', 'Hippopotamus', 'Guinea pig', 'Goat', 'Snail', 'Roundworm', 'Amphibian', 'Hare', 'Xerinae', 'Peregrine falcon', 'Domestic canary', 'Earthworm', 'Narwhal', 'Pig', 'Sawfish', 'Silkworm', 'Bear', 'Ant', 'Dingo', 'Kangaroo', 'Sea snail', 'Whitefish', 'Whooping crane', 'Walrus', 'Perch', 'Rook', 'Wolf', 'Fancy rat', 'Minnow', 'Anteater', 'Hornet', 'Constrictor', 'Chameleon', 'Porpoise', 'Penguin', 'Blue bird', 'Rodent', 'Lizard', 'Lark', 'Mockingbird', 'Domestic dromedary camel', 'Gorilla', 'Sugar glider', 'Hummingbird', 'Limpet', "Portuguese man o' war", 'Panther', 'Domestic rabbit', 'Fish', 'Prairie dog', 'Swan', 'Mite', 'Woodpecker', 'Stingray', 'X-ray fish', 'Muskox', 'Cockroach', 'Swordfish', 'Seahorse', 'Elk', 'Animals by size', 'Anaconda', 'Louse', 'Mastodon', 'Booby', 'Cod', 'Yellow perch', 'Hammerhead shark', 'Lemming', 'Donkey', 'Humpback whale', 'Ringneck dove', 'Pilot whale', 'Beetle', 'Ferret', 'Black panther', 'Gila monster', 'Marmot', 'Fly', 'Land snail', 'Tiger', 'Tree frog', 'Ox', 'Lamprey', 'Vampire squid', 'Elephant', 'Guanaco', 'Opossum', 'Anglerfish', 'Gopher', 'Camel', 'Hyena', 'Tick', 'Dragonfly', 'Landfowl', 'Dove', 'Whale', 'Finch', 'Halibut', 'Owl', 'Shark', 'Heron', 'Snipe', 'Zebra finch', 'Thrush', 'Guineafowl', 'Impala', 'Arctic Wolf', 'Right whale', 'Tasmanian devil', 'Hookworm', 'Flea', 'Flyingfish', 'Guan', 'Animals by number of neurons', 'Parrot', 'Chipmunk', 'Tiglon', 'Wildcat', 'Ostrich', 'Chimpanzee', 'Panda', 'Asp', 'Cicada', 'Mollusk', 'Gerbil', 'Egret', 'Viper', 'Quokka', 'Cheetah', 'Flamingo', 'Sloth', 'Snow leopard', 'Toad', 'Vulture', 'Cobra', 'Gibbon', 'Cattle', 'Pike', 'Frog', 'Spider monkey', 'Puffin', 'Rhinoceros', 'Crane', 'Emu', 'Ground shark', 'Monkey', 'Mountain goat', 'Reindeer', 'Starfish', 'Crane fly', 'Caterpillar', 'Tarantula', 'Cow', 'Spoonbill', 'Partridge', 'Crocodile', 'Orangutan', 'Dormouse', 'Giant squid', 'Dinosaur', 'Basilisk', 'Saber-toothed cat', 'Albatross', 'Gamefowl', 'Bison', 'Sailfish', 'Vampire bat', 'Krill', 'Dolphin', 'Pinniped', 'Python', 'Black widow spider', 'Bee', 'Koi', 'Leopon', 'Boar', 'Horse', 'Swift', 'Lungfish', 'Swallow', 'Rainbow trout', 'Aphid', 'Barracuda', 'Cardinal', 'Sockeye salmon', 'Puma', 'Chickadee', 'Arabian leopard', 'Pony', 'Mackerel', 'Lynx', 'Domestic silkmoth', 'Hoverfly', 'Lion', 'Chicken', 'Llama', 'Blue jay', 'Macaw', 'African leopard', 'Sole', 'Stork', 'Raven', 'Vicuna', 'Salamander', 'Tarsier', 'Bedbug', 'Water Boa', 'Bandicoot', 'Leech', 'Tortoise', 'Aardwolf', 'Beaver', 'Arctic Fox', 'Trapdoor spider', 'Carp', 'Wren', 'Sturgeon', 'Rabbit', 'Harrier', 'Aardvark', 'Smelt', 'Peafowl', 'Clam', 'Old World quail', 'Buzzard', 'Damselfly', 'Great blue heron', 'Bat', 'Echidna', 'Domestic duck', 'Domestic pigeon', 'Weasel', 'Great white shark', 'Bird', 'English pointer', 'Domestic silver fox', 'Moth', 'Firefly', 'Herring', 'Elephant seal', 'Trout', 'Mosquito', 'Irukandji jellyfish', 'Falcon', 'Crayfish', 'Tapir', 'Wolverine', 'Rattlesnake', 'Wasp', 'Haddock', 'Raccoon', 'Skunk', 'Mink', 'Eel', 'Siamese fighting fish', 'Bobolink', 'Primate', 'Goldfish', 'Water buffal', 'Lemur', 'Alligator', 'Cuckoo', 'Fox', 'Caribou', 'Bobcat', 'Snake', 'Lobster', 'Ground sloth', 'Platypus', 'Crawdad', 'Spider', 'Yak', 'Loon', 'Tyrannosaurus', 'Duck', 'Scallop', 'Domestic hedgehog', 'Planarian', 'Porcupine', 'Quelea', 'Peacock', 'Gull', 'Domestic goose', 'Parakeet', 'Marten', 'Centipede', 'Coral', 'Fruit bat', 'Kangaroo mouse', 'Catfish', 'Clownfish', 'Jaguar', 'Kiwi', 'Rat', 'Possum', 'Sea lion', 'Swordtail', 'Ape']
countries =['Chad', 'Sweden', 'Kuwait', 'United States', 'Malawi', 'Kosovo', 'Korea North', 'Maldives', 'Finland', 'Sudan', 'Indonesia', 'Chile', 'Benin', 'Mauritius', 'Papua New Guinea', 'Belarus', 'Egypt', 'Zambia', 'Ethiopia', 'Ivory Coast', 'United Kingdom', 'Dominican Republic', 'Bulgaria', 'Sierra Leone', 'Cape Verde', 'Madagascar', 'Taiwan', 'Singapore', 'Iraq', 'Lebanon', 'Lithuania', 'Rwanda', 'Morocco', 'Tuvalu', 'Ukraine', 'Slovenia', 'Bahamas', 'Korea South', 'Togo', 'Turkey', 'Kiribati', 'Nigeria', 'Dominica', 'Norway', 'Turkmenistan', 'Seychelles', 'East Timor', 'Japan', 'China', 'Swaziland', 'Azerbaijan', 'Lesotho', 'Nauru', 'Malaysia', 'Spain', 'Luxembourg', 'Portugal', 'Burkina', 'Macedonia', 'Bangladesh', 'Qatar', 'Guyana', 'Belize', 'Algeria', 'Libya', 'Iran', 'South Africa', 'Botswana', 'Afghanistan', 'Colombia', 'Jordan', 'Palau', 'Nepal', 'Latvia', 'Uganda', 'Nicaragua', 'Honduras', 'Austria', 'Bahrain', 'Venezuela', 'Thailand', 'Kenya', 'Somalia', 'Yemen', 'Brunei', 'Denmark', 'Equatorial Guinea', 'Angola', 'Canada', 'Czech Republic', 'Tanzania', 'Estonia', 'Poland', 'Ghana', 'Monaco', 'Liberia', 'Iceland', 'Ecuador', 'Andorra', 'Mali', 'Hungary', 'Barbados', 'Tajikistan', 'Vatican City', 'Mongolia', 'Vietnam', 'Brazil', 'Niger', 'Panama', 'Malta', 'Slovakia', 'Mexico', 'Croatia', 'Uzbekistan', 'Gabon', 'Burundi', 'Albania', 'Bhutan', 'Uruguay', 'India', 'Gambia', 'Kazakhstan', 'France', 'Liechtenstein', 'Peru', 'Fiji', 'Solomon Islands', 'Oman', 'Paraguay', 'Australia', 'New Zealand', 'Jamaica', 'Romania', 'Georgia', 'Djibouti', 'Cameroon', 'Kyrgyzstan', 'Germany', 'Micronesia', 'Serbia', 'Tonga', 'Central African Rep', 'Laos', 'Switzerland', 'Moldova', 'Cuba', 'Bosnia Herzegovina', 'Armenia', 'El Salvador', 'Haiti', 'Netherlands', 'Mauritania', 'Suriname', 'Congo', 'Marshall Islands', 'Sri Lanka', 'Italy', 'Mozambique', 'Senegal', 'Cyprus', 'Greece', 'Montenegro', 'Cambodia', 'Vanuatu', 'Zimbabw', 'Philippines', 'Bolivia', 'Eritrea', 'Guatemala', 'Pakistan', 'Grenada', 'Syria', 'South Sudan', 'San Marino', 'United Arab Emirates', 'Russian Federation', 'Belgium', 'Comoros', 'Guinea']
food=['Lean', 'Rosemary', 'Salami', 'Carbonated', 'Nutritional', 'Bowl', 'Pectin', 'Prune', 'Rennin', 'Rojos', 'Dock', 'Durian', 'Radish', 'Chili', 'Guacamole', 'Taro', 'Turnover', 'Snacks', 'Dry', 'Granola', 'Fast', 'Loaf', 'Clam', 'Strawberries', 'Chicory', 'Gum', 'Fat', 'Dressing', 'Milk', 'Seal', 'Meatloaf', 'Jackfruit', 'Teff', 'Goat', 'Beef', 'Waxgourd', 'Pudding', 'Celery', 'Tuber', 'Tennis', 'Soup', 'Taco', 'Tortilla', 'Pea', 'Toppings', 'Cornstarch', 'Croutons', 'Applesauce', 'Chickpeas', 'Sourdock', 'Whey', 'Guanabana', 'Phyllo', 'Bits', 'Olives', 'Spanish', 'Tunicate', 'Novelties', 'Cream', 'Naranjilla', 'Industrial', 'Lentils', 'Patties', 'Cockles', 'Onions', 'Alfalfa', 'Mouse', 'Stew/soup', 'Nectarines', 'Rambutan', 'Yam', 'Sapote', 'Cereals', 'Carissa', 'Foods', 'Queso', 'Hen', 'Eggnog', 'Jute', 'Parmesan', 'Pigeon', 'Side', 'Hazelnuts', 'Bagels', 'Seaweed', 'Litchis', 'Lemon', 'Butter', 'Hush', 'Lion', 'Formula', 'Oheloberries', 'Sticks', 'Yogurt', 'Chrysanthemum', 'Shortening', 'Substitute', 'Peanut', 'Corned', 'Tostada', 'Semolina', 'Rutabagas', 'Sea', 'Babyfood', 'Broth', 'Potsticker', 'Moose', 'Hummus', 'Dill', 'Purslane', 'Artichokes', 'Sesbania', 'Bar', 'Crabapples', 'Chorizo', 'Cheesecake', 'Juice', 'Epazote', 'Mollusks', 'Thuringer', 'Scrapple', 'Falafel', 'Legs', 'Knackwurst', 'Whiskey', 'Lunch', 'Preserves', 'Yardlong', 'Yeast', 'Candies', 'Deer', 'Spinach', 'Tomatillos', 'Fish', 'Yachtwurst', 'Berry', 'Pepperoni', 'Grouse', 'Guava', 'Wonton', 'Gelatin', 'Bagel', 'Borage', 'Ground', 'Capers', 'Veggie', 'Flours', 'Sweet', 'Balls', 'Peppered', 'Relish', 'Mungo', 'Doughnuts', 'Smelt', 'Cardoon', 'Vanilla', 'Fava', 'Shoots', 'Cucumber', 'Walrus', 'Caribou', 'Cornsalad', 'Chokecherries', 'Gluten', 'Fern', 'Ferns', 'Mangosteen', 'Gooseberries', 'Gravy', 'Tea', 'Trout', 'Pummelo', 'Yellow', 'Vital', 'Agutuk', 'Smoked', 'Cornmeal', 'Cress', 'Grass', 'Bratwurst', 'Dove', 'Mustard', 'Basil', 'Pulled', 'Coffee', 'Vinespinach', 'Gram', 'Lime', 'Pear', 'Apricots', 'Nuts', 'Germ', 'Triticale', 'Pie', 'Imitation', 'Winged', 'Malabar', 'Cherries', 'Grapes', 'Brotwurst', 'Groats', 'Frijoles', 'Lulo', 'Pinon', 'Flan', 'Venison', 'Shoyu', 'Crustaceans', 'Dairy', 'Carne', 'Gourd', 'Pimento', 'Papad', 'Child', 'Butterbur', 'Navajo', 'Puffs', 'Ascidians', 'Avocados', 'Stuffing', 'Dates', 'Wine', 'Keikitos', 'Pomegranates', 'Fillets', 'Pastry', 'Peach', 'Sweetener', 'Mocha', 'Margarine', 'Breakfast', 'Celeriac', 'Cranberries', 'Zwiebac', 'Buns', 'Restaurant', 'Pheasant', 'Shake', 'Miso', 'Mushrooms', 'Potatoes', 'Pumpkin', 'Lambs', 'Seeds', 'Fiddlehead', 'Cake', 'Eppaw', 'Eggs', 'Burrito', 'Yogurts', 'Pate', 'Peaches', 'Puree', 'Products', 'Red', 'Drippings', 'Salad', 'Cherimoya', 'Bison', 'Wrappers', 'Sherbet', 'Ice', 'Mountain', 'Creams', 'Prunes', 'Gras', 'Couscous', 'Drumstick', 'Potato', 'Noodles', 'From', 'Beets', 'Wild', 'Ruffed', 'Cones', 'Quail', 'Rowal', 'Kale', 'Tapioca', 'Feijoa', 'Hydrolyzed', 'Baking', 'Clementines', 'Quarters', 'Barley', 'Tamales', 'Abiyuch', 'Sorghum', 'Coriander', 'Headcheese', 'Catsup', 'Tart', 'Blackberry', 'Cattail', 'Pizza', 'Rolls', 'Greens', 'Pitanga', 'Longans', 'Lettuce', 'Oopah', 'Papayas', 'Muffin', 'Kiwifruit', 'Spread', 'Stew', 'Pepeao', 'Vegetarian', 'Creamy', 'Roast', 'Blueberry', 'Focaccia', 'Chayote', 'Citrus', 'Frying', 'Household', 'Oil', 'Toaster', 'Sauce', 'Tannier', 'Vermicelli', 'Arrowhead', 'Prickly', 'Squirrel', 'Buffalo', 'Pepper', 'Nopales', 'Molasses', 'Hearts', 'Ravioli', 'Yambean', 'Fireweed', 'Soyburgers', 'Energy', 'Lard', 'Edamame', 'Fluid', 'Lambsquarters', 'Pastrami', 'Toddler', 'Agents', 'Animal', 'Made', 'Parsley', 'Papaya', 'Puddings', 'Waffle', 'Guavas', 'Burgers', 'Kanpyo', 'Meat', 'Syrups', 'Link', 'Egg', 'Cheesefurter', 'Chips', 'Currants', 'Emu', 'Pineapple', 'Mortadella', 'Sapodilla', 'Tofu', 'Roll', 'Salt', 'Liver', 'Biscuits', 'Bananas', 'Ear', 'Pork', 'Steelhead', 'Tamari', 'Frankfurter', 'Besan', 'Collards', 'Mixed', 'Lebanon', 'Refried', 'Reduced', 'Turnips', 'Spelt', 'Persimmons', 'Beet', 'Hazelnut', 'Stinging', 'Foie', 'Food', 'Peanuts', 'Blackeyes', 'Extender', 'Jujube', 'Turtle', 'Figs', 'Chocolate', 'Prairie', 'Tunughnak', 'Incaparina', 'Soy', 'Hips', 'Thyme', 'Water', 'Fillings', 'Ham', 'Chickpea', 'Limeade', 'Waffles', 'Carob', 'Broadbeans', 'Kielbasa', 'Wheat', 'Onion', 'Desserts', 'Amaranth', 'Crackers', 'Plums', 'Pretzels', 'Roots', 'Containing', 'Pulp', 'Melon', 'Veal', 'Acorn', 'Vegetable', 'Tortillas', 'Product', 'Elk', 'Mothbeans', 'Garlic', 'Raspberries', 'Breadfruit', 'Replacement', 'Pockets', 'Meal', 'Reddi', 'Salsify', 'Sauerkraut', 'Braunschweiger', 'Thigh', 'Fungi', 'Fennel', 'Rice', 'Confectionery', 'Cone', 'Oranges', 'Quinoa', 'Pickle', 'Shakes', 'Blueberries', 'Cocoa', 'Arugula', 'Pigeonpeas', 'Kohlrabi', 'Breast', 'Ginger', 'Celtuce', 'Bear', 'Dogs', 'Maraschino', 'Salmonberries', 'Tempeh', 'Mulberries', 'Peas', 'Apricot', 'Leaves', 'Wasabi', 'Sausage', 'Huckleberries', 'Candied', 'Malted', 'Leavening', 'Beverage', 'Frog', 'Cracker', 'Peppermint', "Mother's", 'Prepared', 'Swisswurst', 'Concentrate', 'Dinner', 'Horned', 'Pears', 'Cassava', 'Gums', 'Mutton', 'Pickles', 'Dandelion', 'Soybean', 'Bologna', 'Broccoli', 'Cloudberries', 'Goose', 'Picnic', 'Elderberries', 'Extract', 'Bars', 'Blend', 'Plantains', 'Entrees', 'Barbecue', 'Radishes', 'Hyacinth', 'Chiton', 'Sandwich', 'Cocktail', 'Beerwurst', 'Raab', 'Squash', 'Brand', 'Tangerine', 'Dutch', 'Jellyfish', 'Apple', 'Lotus', 'Okra', 'Bacon', 'Puff', 'Seasoning', 'Drink', 'Popcorn', 'Topping', 'Honey', 'Flowers', 'Frozen', 'Punch', 'Rye', 'Succotash', 'Chives', 'Boysenberries', 'Loin', 'Peel', 'Brussels', 'Carrots', 'Cereal', 'Snack', 'Pastries', 'Smoothie', 'Protein', 'Cabbage', 'Liverwurst', 'Green', 'Nettles', 'Pomegranate', 'Lima', 'Cheese', 'Syrup', 'Shells', 'Malt', 'Quinces', 'Crumbs', 'Burdock', 'Powder', 'Fruit', 'Duck', 'Lupins', 'School', 'Acerola', 'Hibiscus', 'Cilantro', 'Swamp', 'Dulce', 'Franks', 'Horseradish', 'Links', 'Oats', 'Loquats', 'Muffins', 'Corn', 'Millet', 'Salmon', 'People', 'Asparagus', 'Shallots', 'Split', 'Grape', 'New', 'Endive', 'Lemonade', 'Guinea', 'Squab', 'Dough', 'Dip', 'Volteados', 'Chewing', 'Citronella', 'Ostrich', 'Cotija', 'Shell', 'Pancakes', 'Chard', 'Macaroni', 'Kiwano', 'Flavored', 'Melons', 'Olive', 'Tenders', 'Groundcherries', 'Spices', 'Turnip', 'Flour', 'Piki', 'Apache', 'Cookie', 'Taquitos', 'Radicchio', 'Octopus', 'Yautia', 'Souffle', 'Weed', 'Nance', 'Sweeteners', 'Raisins', 'Spaghetti', 'Natto', 'Dishes', 'Butters', 'Root', 'Bread', 'Bean', 'Toast', 'Flakes', 'Tangerines', 'Bulgur', 'Watermelon', 'Rhubarb', 'Mayonnaise', 'Limes', 'Chicken', 'Poultry', 'Willow', 'Isolate', 'Parfait', 'Turkey', 'Soymilk', 'Diabetes', 'Chilchen', 'Pimiento', 'Spearmint', 'Meatballs', 'Tortellini', 'Beans', 'Baby', 'Lasagna', 'Pokeberry', 'Bockwurst', 'Commercially', 'Rings', 'Watercress', 'Artificial', 'Bitter', 'Beverages', 'Loganberries', 'Nectar', 'Gelatins', 'Luncheon', 'Arrowroot', 'Parsnips', 'Zealand', 'Flower', 'Cranberry', 'Apples', 'Waterchestnuts', 'Cookies', 'Tomatoes', 'Cinnamon', 'Tamarind', 'Patty', 'Coffeecake', 'Carambola', 'Grain', 'Vinegar', 'Leeks', 'Dessert', 'Croissants', 'Danish', 'Orange', 'Leche', 'Mashu', 'Mush', 'Peppers', 'Tamarinds', 'Sprouts', 'Buckwheat', 'Rose', 'Tomato', 'Substitutes', 'Oat', 'Supplement', 'Jams', 'Formulated', 'Luxury', 'Soybeans', 'Plain', 'Kumquats', 'Mung', 'Bran', 'Frostings', 'Grapefruit', 'Blackberries', 'Mangos', 'Twists', 'Lamb', 'Agave', 'Soursop', 'Hominy', 'Cowpeas', 'Garbanzo', 'Sugar', 'Crust', 'Cauliflower', 'Wocas', 'Whole']
list_of_check_boxes = []
word = ''
user_word = []
list_of_words = []
high_scores = [[0,0,0,0],[0,0,0,0],[0,0,0,0]]
AFTER = None
countries_img = PhotoImage(file='countries.png')
animals_img = PhotoImage(file='animals.png')
food_img = PhotoImage(file='food.png')


#settings screen
setting_group = LabelFrame(mainframe,text='SETTINGS',font = 1)
themes_label = Label(setting_group, text ='Theme')
themes = ['random','ANIMALS','COUNTRIES','FOOD']
themes_option_var = StringVar()
themes_option_var.set('random')
themes_option = OptionMenu(setting_group, themes_option_var,*themes)
timer_label = Label(setting_group,text='Timer')
timer = ['30 seconds', '1 minute', '3 minutes']
timer_spin_var = StringVar()
timer_spin_var.set('No time limit')
timer_spin = Spinbox(setting_group, textvariable = timer_spin_var, values = timer,state = 'readonly')
difficulty_label = Label(setting_group,text='Difficulty')
difficulty_scale_var = IntVar()
difficulty_scale_var.set(0)
difficulty_scale = Scale(setting_group,from_=0,to=2, variable = difficulty_scale_var,label = 'easy',orient = HORIZONTAL,showvalue=False,command=change_difficulty_label)

#highscore screen
stats_group = LabelFrame(mainframe,text='HIGHSCORE',font = 1)
difficulty_highscore_label = Label(stats_group,text='Difficulty')
difficulty_highscore_var = StringVar()
difficulty_highscore_var.set('Easy')
easy_radio = Radiobutton(stats_group,text='Easy',variable = difficulty_highscore_var,value='Easy',command = update_scoreboard)
medium_radio =Radiobutton(stats_group,text='Medium',variable = difficulty_highscore_var,value='Medium',command = update_scoreboard)
hard_radio =Radiobutton(stats_group,text='Hard',variable = difficulty_highscore_var,value='Hard',command = update_scoreboard)
total_var = StringVar()
thirty_var = StringVar()
one_var = StringVar()
three_var = StringVar()
total_var.set('Total: 0')
thirty_var.set('30 seconds: 0')
one_var.set('1 Minute1: 0')
three_var.set('3 Minutes: 0')
total_label = Label(stats_group,textvariable=total_var)
thirty_label= Label(stats_group,textvariable=thirty_var)
one_label= Label(stats_group,textvariable=one_var)
three_label= Label(stats_group,textvariable=three_var)

#playbutton
play_button = Button(mainframe,text='PLAY',command = play,font=1)

#playing screen
game_group = LabelFrame(mainframe)
title_var = StringVar()
title_var.set('Press "PLAY" button to play')
title = Label(game_group,textvariable = title_var, font=1)
word_var = StringVar()
checkbox_group = LabelFrame(game_group)
user_word_var = StringVar()
user_word_label = Label(game_group,textvariable=user_word_var,font=1)
score_var = StringVar()
score_var.set('Score: 0')
user_score_label = Label(game_group,textvariable=score_var,font=1)
next_button = Button(mainframe,text='NEXT',command = update_frame_new_word,state = DISABLED)
quit_button = Button(mainframe,text='QUIT',command = quit_or_not,state = DISABLED)
timerVar = StringVar()
timerVar.set('Timer: NA')
timerLabel = Label(game_group, textvariable = timerVar,font=0.001)
image= Label(game_group)

#gridding
root.minsize(width=450, height=450)
mainframe.grid(row=1, column=1)
setting_group.grid(row=2,column=1,pady = 30,padx = 10)
themes_label.grid(row=2,column=1,sticky = W,pady=5)
themes_option.grid(row=2,column=2,ipadx = 30,pady=5)
timer_label.grid(row=3,column=1,sticky = W,pady=5)
timer_spin.grid(row=3, column=2,pady=5)
difficulty_label.grid(row=4,column=1,sticky = W,pady=5)
difficulty_scale.grid(row=4,column=2,ipadx = 23,pady=5)

stats_group.grid(row=1,column=1,ipadx=10,padx = 10)
easy_radio.grid(row=2,column=1)
medium_radio.grid(row=2,column=2)
hard_radio.grid(row=2,column=3)
total_label.grid(row=3,column = 2)
thirty_label.grid(row=4,column = 2)
one_label.grid(row=5,column = 2)
three_label.grid(row=6,column = 2)

play_button.grid(row=3, column=1, ipadx = 80,ipady = 40,padx = 10,pady=5)

game_group.grid(row=1,column=2,rowspan=4,columnspan= 2,sticky='NESW')
title.grid(row=2,column=2,pady=30)
checkbox_group.grid(row=5,column=2,pady=30)
user_word_label.grid(row=4,column=2)
user_score_label.grid(row=1, column=3,sticky = E)
next_button.grid(row=3,column=3,sticky = E,ipadx=20,ipady=20)
quit_button.grid(row=3,column=2,sticky =W,ipadx=20,ipady=20)##
timerLabel.grid(row=1,column=1,sticky = W)
image.grid(row=3,column=2)
root.mainloop()
