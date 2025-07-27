import streamlit as st
import re
import uuid
git add homework_genie.py
git commit -m "Temporarily remove database import to fix Streamlit error"
git push origin main
    init_database, 
    log_user_interaction, 
    get_popular_topics, 
    get_interaction_stats,
    search_questions_in_db
)
from practice_problems import display_practice_mode

# Initialize database on app start
init_database()

# Generate session ID for tracking user interactions
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Page configuration
st.set_page_config(
    page_title="Homework Genie", 
    page_icon="📘", 
    layout="centered"
)

# Main title and header
st.title("📘 Homework Genie")
st.subheader("Your magical homework helper! ✨")
st.write("Ask me any question about Math, Reading, Science, History, Geography, Art, or Music and I'll help you learn!")

# Mode selection
mode = st.radio(
    "Choose your learning mode:",
    ["❓ Ask Questions", "🎯 Practice Problems"],
    help="Select whether you want to ask questions or practice with step-by-step problems"
)

# Subject selection
st.write("### Choose your subject:")
subject = st.radio(
    "Pick the subject you need help with:",
    ["Math 🔢", "Reading 📖", "Science 🔬", "History 🏛️", "Geography 🌍", "Art 🎨", "Music 🎵"],
    help="Select the subject area for your homework question"
)

# Clean subject name for processing
subject_clean = subject.split()[0]

# Display content based on selected mode
if mode == "❓ Ask Questions":
    # Question input
    st.write("### Ask your question:")
    user_question = st.text_area(
        "📝 Type your homework question here:",
        placeholder="For example: 'What is 5 times 3?' or 'What is a noun?' or 'How do plants grow?'",
        height=100
    )
else:  # Practice Problems mode
    display_practice_mode(subject_clean)
    user_question = ""  # Set empty to avoid errors in the rest of the code

def get_math_response(question):
    """Handle math-related questions"""
    q = question.lower()
    
    # Multiplication
    if any(word in q for word in ["multiply", "times", "×", "*"]):
        # Extract numbers if possible for specific calculation
        import re
        numbers = re.findall(r'\d+', question)
        if len(numbers) >= 2:
            try:
                num1, num2 = int(numbers[0]), int(numbers[1])
                result = num1 * num2
                return f"Answer: {result}\n\nExplanation: Multiplying means adding a number to itself multiple times! For example, {num1} × {num2} means adding {num1} to itself {num2} times: " + " + ".join([str(num1)] * num2) + f" = {result}. It's like having {num2} groups of {num1} things each!"
            except:
                pass
        return "Answer: (depends on your numbers)\n\nExplanation: Multiplying means adding a number to itself multiple times! For example, 3 × 4 means 3 + 3 + 3 + 3 = 12. It's like having 4 groups of 3 things each!"
    
    # Addition
    elif any(word in q for word in ["add", "plus", "+"]):
        import re
        numbers = re.findall(r'\d+', question)
        if len(numbers) >= 2:
            try:
                num1, num2 = int(numbers[0]), int(numbers[1])
                result = num1 + num2
                return f"Answer: {result}\n\nExplanation: Adding means putting numbers together to make a bigger number! When you add {num1} + {num2}, you're counting {num1} things, then {num2} more things, which gives you {result} things total!"
            except:
                pass
        return "Answer: (depends on your numbers)\n\nExplanation: Adding means putting numbers together to make a bigger number! When you add 2 + 3, you're counting 2 things, then 3 more things, which gives you 5 things total!"
    
    # Subtraction
    elif any(word in q for word in ["subtract", "minus", "-", "take away"]):
        import re
        numbers = re.findall(r'\d+', question)
        if len(numbers) >= 2:
            try:
                num1, num2 = int(numbers[0]), int(numbers[1])
                result = num1 - num2
                return f"Answer: {result}\n\nExplanation: Subtracting means taking some away from what you have. If you have {num1} things and take away {num2}, you subtract: {num1} - {num2} = {result} things left!"
            except:
                pass
        return "Answer: (depends on your numbers)\n\nExplanation: Subtracting means taking some away from what you have. If you have 8 cookies and eat 3, you subtract: 8 - 3 = 5 cookies left!"
    
    # Division
    elif any(word in q for word in ["divide", "division", "÷", "/"]):
        import re
        numbers = re.findall(r'\d+', question)
        if len(numbers) >= 2:
            try:
                num1, num2 = int(numbers[0]), int(numbers[1])
                if num2 != 0:
                    result = num1 / num2
                    if result == int(result):
                        result = int(result)
                    return f"Answer: {result}\n\nExplanation: Division means splitting things into equal groups. If you have {num1} things and want to share them equally among {num2} groups, each group gets {num1} ÷ {num2} = {result}!"
            except:
                pass
        return "Answer: (depends on your numbers)\n\nExplanation: Division means splitting things into equal groups. If you have 12 candies and want to share them equally among 3 friends, each friend gets 12 ÷ 3 = 4 candies!"
    
    # Fractions
    elif "fraction" in q:
        return "Answer: (depends on the fraction)\n\nExplanation: A fraction shows parts of a whole! Think of a pizza: 1/2 means 1 piece out of 2 equal pieces. 3/4 means 3 pieces out of 4 equal pieces!"
    
    # Even and odd numbers
    elif any(word in q for word in ["even", "odd"]):
        import re
        numbers = re.findall(r'\d+', question)
        if numbers:
            try:
                num = int(numbers[0])
                if num % 2 == 0:
                    return f"Answer: {num} is even\n\nExplanation: Even numbers can be split into pairs perfectly! {num} ÷ 2 = {num//2} with no remainder. Even numbers are: 2, 4, 6, 8, 10..."
                else:
                    return f"Answer: {num} is odd\n\nExplanation: Odd numbers always have one left over when split into pairs! {num} ÷ 2 = {num//2} with 1 left over. Odd numbers are: 1, 3, 5, 7, 9..."
            except:
                pass
        return "Answer: (tell me a number to check!)\n\nExplanation: Even numbers can be split into pairs perfectly (2, 4, 6, 8...). Odd numbers always have one left over (1, 3, 5, 7...)!"
    
    # Place value
    elif any(word in q for word in ["place value", "tens", "ones", "hundreds"]):
        import re
        numbers = re.findall(r'\d+', question)
        if numbers:
            try:
                num = numbers[0]
                if len(num) >= 3:
                    return f"Answer: In {num}: {num[-3]} is hundreds, {num[-2]} is tens, {num[-1]} is ones\n\nExplanation: Place value tells us what each digit means! Each position has a different value - hundreds, tens, and ones from left to right."
                elif len(num) == 2:
                    return f"Answer: In {num}: {num[-2]} is tens, {num[-1]} is ones\n\nExplanation: Place value tells us what each digit means! The left digit is tens, the right digit is ones."
            except:
                pass
        return "Answer: (give me a number to break down!)\n\nExplanation: Place value tells us what each digit means! In 234: the 2 is in hundreds place (200), 3 is in tens place (30), and 4 is in ones place (4)!"
    
    # Shapes
    elif any(word in q for word in ["shape", "triangle", "square", "circle", "rectangle"]):
        if "triangle" in q:
            return "Answer: A triangle has 3 sides\n\nExplanation: Triangles are shapes with exactly 3 straight sides and 3 corners. They come in different types but always have 3 sides!"
        elif "square" in q:
            return "Answer: A square has 4 equal sides\n\nExplanation: Squares are special rectangles where all 4 sides are exactly the same length, and all corners are right angles!"
        elif "rectangle" in q:
            return "Answer: A rectangle has 4 sides (opposite sides equal)\n\nExplanation: Rectangles have 4 sides where opposite sides are the same length, and all corners are right angles!"
        elif "circle" in q:
            return "Answer: A circle has no sides (it's round)\n\nExplanation: Circles are perfectly round shapes with no straight sides or corners. Every point on the circle is the same distance from the center!"
        return "Answer: (depends on the shape)\n\nExplanation: Shapes are everywhere! A triangle has 3 sides, a square has 4 equal sides, a rectangle has 4 sides with opposite sides equal, and a circle is perfectly round!"
    
    # Time
    elif any(word in q for word in ["time", "clock", "hour", "minute"]):
        return "Answer: 60 minutes = 1 hour, 24 hours = 1 day\n\nExplanation: Time helps us know when things happen! There are 60 minutes in 1 hour, and 24 hours in 1 day. The big hand shows minutes, the little hand shows hours!"
    
    # Money
    elif any(word in q for word in ["money", "cent", "dollar", "coin"]):
        return "Answer: 1 penny = 1¢, 1 nickel = 5¢, 1 dime = 10¢, 1 quarter = 25¢, 1 dollar = 100¢\n\nExplanation: Money math is important! A penny = 1 cent, nickel = 5 cents, dime = 10 cents, quarter = 25 cents, and a dollar = 100 cents!"
    
    return None

def get_reading_response(question):
    """Handle reading-related questions"""
    q = question.lower()
    
    # Parts of speech
    if "noun" in q:
        return "Answer: A noun is a person, place, or thing\n\nExplanation: Examples: 'dog' (thing), 'school' (place), 'teacher' (person). Nouns are the naming words that tell us what we're talking about!"
    
    elif "verb" in q:
        return "Answer: A verb shows action or what someone is doing\n\nExplanation: Examples: run, jump, think, sing, eat. Verbs are the action words that make sentences exciting and tell us what's happening!"
    
    elif "adjective" in q:
        return "Answer: An adjective describes or tells us more about a noun\n\nExplanation: Examples: 'big dog', 'red apple', 'funny joke'. They make our writing more colorful by giving details about people, places, and things!"
    
    elif "adverb" in q:
        return "Answer: An adverb tells us more about a verb\n\nExplanation: They often end in -ly: quickly, slowly, carefully. They tell us HOW something is done, making our writing more detailed!"
    
    # Reading comprehension
    elif any(word in q for word in ["main idea", "theme"]):
        return "Answer: The main idea is what the story is mostly about\n\nExplanation: Look for the most important point the author wants you to understand! It's usually mentioned several times in different ways throughout the text."
    
    elif any(word in q for word in ["character", "protagonist"]):
        return "Answer: Characters are the people or animals in a story\n\nExplanation: The main character (protagonist) is usually the one the story focuses on the most, and whose problem or adventure we follow!"
    
    elif "setting" in q:
        return "Answer: Setting is WHERE and WHEN a story takes place\n\nExplanation: It could be a school, a forest, the past, or the future! The setting helps create the mood and affects what happens in the story."
    
    # Phonics and spelling
    elif any(word in q for word in ["phonics", "sound", "letter"]):
        return "Answer: Phonics helps us sound out words by blending letter sounds\n\nExplanation: Each letter makes a sound, and we blend sounds together to read words: c-a-t makes 'cat'! This is how we decode new words."
    
    elif any(word in q for word in ["rhyme", "rhyming"]):
        return "Answer: Rhyming words sound the same at the end\n\nExplanation: Like 'cat' and 'hat', or 'dog' and 'log'. Rhymes make poems and songs fun to read and help us remember words!"
    
    elif any(word in q for word in ["syllable", "clap"]):
        return "Answer: Syllables are the beats in words\n\nExplanation: Clap as you say a word: 'but-ter-fly' has 3 claps, so 3 syllables! This helps us break down long words to read them easier."
    
    # Reading strategies
    elif any(word in q for word in ["context clue", "unknown word"]):
        return "Answer: Use context clues to figure out unknown words\n\nExplanation: When you don't know a word, look at the words around it for clues! The other words in the sentence can help you figure out what it means."
    
    elif any(word in q for word in ["summary", "summarize"]):
        return "Answer: A summary tells the most important parts in a few sentences\n\nExplanation: Include who, what, where, when, and why! Leave out small details and focus on the main events and ideas."
    
    return None

def get_science_response(question):
    """Handle science-related questions"""
    q = question.lower()
    
    # Physics concepts
    if "gravity" in q:
        return "Answer: Gravity is the force that pulls everything down toward Earth\n\nExplanation: It's an invisible force that keeps us on the ground! That's why when you drop something, it falls down instead of floating up to the ceiling."
    
    elif any(word in q for word in ["magnet", "magnetic"]):
        return "Answer: Magnets attract certain metals and have north and south poles\n\nExplanation: They can pull (attract) some metals like iron, and they have two ends called poles: north and south! Opposite poles attract, same poles push away."
    
    elif any(word in q for word in ["light", "shadow"]):
        return "Answer: Light travels in straight lines and creates shadows when blocked\n\nExplanation: When light hits something it can't go through, it makes a shadow on the other side. Light helps us see everything around us!"
    
    elif any(word in q for word in ["sound", "vibration"]):
        return "Answer: Sound happens when things vibrate and travel through air\n\nExplanation: Sound occurs when things shake back and forth (vibrate)! The vibrations travel through the air to your ears so you can hear them."
    
    # Life science
    elif any(word in q for word in ["plant", "grow"]):
        return "Answer: Plants need sunlight, water, air, and nutrients to grow\n\nExplanation: Plants are amazing living things! They need four things: sunlight for energy, water to drink, air to breathe, and nutrients from soil for food. This is called photosynthesis!"
    
    elif any(word in q for word in ["animal", "habitat"]):
        return "Answer: Animals live in habitats that provide everything they need\n\nExplanation: A habitat is like an animal's home that gives them food, water, shelter, and space! Fish live in water, birds in trees, and bears in forests."
    
    elif any(word in q for word in ["food chain", "eat"]):
        return "Answer: A food chain shows who eats what in nature\n\nExplanation: It's like a feeding line! Plants make their own food from sunlight, plant-eaters (herbivores) eat plants, and meat-eaters (carnivores) eat other animals."
    
    elif any(word in q for word in ["life cycle", "baby"]):
        return "Answer: All living things have a life cycle of birth, growth, reproduction, and death\n\nExplanation: Every living thing follows this pattern! They are born, grow up, have babies of their own, and complete the circle of life."
    
    # Earth science
    elif any(word in q for word in ["water cycle", "rain"]):
        return "Answer: The water cycle moves water through evaporation, condensation, and precipitation\n\nExplanation: It's water's amazing journey! Water evaporates (rises up from oceans), forms clouds (condenses), then falls as rain (precipitation) and starts over!"
    
    elif any(word in q for word in ["weather", "cloud"]):
        return "Answer: Weather is atmospheric conditions; clouds are water droplets in the air\n\nExplanation: Weather is what's happening in the sky right now! Clouds are made of tiny water droplets floating in the air. Different clouds bring different weather."
    
    elif any(word in q for word in ["rock", "mineral"]):
        return "Answer: Rocks are made of minerals and come in three main types\n\nExplanation: The three types are: igneous (from cooled lava), sedimentary (from pressed layers), and metamorphic (changed by heat and pressure)!"
    
    elif any(word in q for word in ["soil", "dirt"]):
        return "Answer: Soil is a mixture of nutrients, organisms, and decomposed matter\n\nExplanation: Soil isn't just dirt! It's full of nutrients, tiny creatures, air pockets, and decomposed plants that help new plants grow healthy and strong."
    
    # Space science
    elif any(word in q for word in ["sun", "solar"]):
        return "Answer: The Sun is our nearest star that provides light and heat\n\nExplanation: It's a giant ball of hot gas that gives us light and heat! It's so big that over 1 million Earths could fit inside it, and it's 93 million miles away."
    
    elif any(word in q for word in ["moon", "phase"]):
        return "Answer: The Moon orbits Earth and shows different phases as it reflects sunlight\n\nExplanation: The Moon is Earth's companion in space! It looks different each night because we see different amounts of the Sun shining on its surface."
    
    elif any(word in q for word in ["planet", "earth"]):
        return "Answer: Earth is our home planet with the right conditions for life\n\nExplanation: Earth is special because it's the perfect distance from the Sun - not too hot, not too cold - and has air, water, and land for life to exist!"
    
    # Basic chemistry
    elif any(word in q for word in ["matter", "solid", "liquid", "gas"]):
        return "Answer: Matter exists in three main states: solid, liquid, and gas\n\nExplanation: Everything around us is made of matter! Solids hold their shape (like ice), liquids flow (like water), and gases spread out (like steam)."
    
    elif any(word in q for word in ["mix", "solution"]):
        return "Answer: When substances mix, they either blend completely or stay separate\n\nExplanation: Sometimes they blend completely (like sugar dissolving in water) and sometimes they stay separate (like oil floating on water). It depends on their properties!"
    
    return None

def get_history_response(question):
    """Handle history-related questions"""
    q = question.lower()
    
    # American History
    if any(word in q for word in ["christopher columbus", "columbus"]):
        return "Answer: Christopher Columbus sailed to the Americas in 1492\n\nExplanation: Columbus was an explorer from Italy who sailed across the Atlantic Ocean and reached the Americas, though he thought he had reached Asia!"
    
    elif any(word in q for word in ["george washington", "washington"]):
        return "Answer: George Washington was the first President of the United States\n\nExplanation: He led the American army during the Revolutionary War and became our first president. He's called the 'Father of Our Country'!"
    
    elif any(word in q for word in ["civil war", "lincoln"]):
        return "Answer: The Civil War was fought from 1861-1865; Abraham Lincoln was president\n\nExplanation: It was a war between the North and South mainly about slavery. Lincoln helped end slavery and keep the country together!"
    
    elif any(word in q for word in ["declaration of independence", "independence"]):
        return "Answer: The Declaration of Independence was signed in 1776\n\nExplanation: This important document said America wanted to be free from British rule. It was signed on July 4th, which is why we celebrate Independence Day!"
    
    # Ancient History
    elif any(word in q for word in ["pyramid", "egypt", "pharaoh"]):
        return "Answer: Pyramids were built by ancient Egyptians as tombs for pharaohs\n\nExplanation: Pharaohs were Egyptian kings, and they built these amazing stone structures thousands of years ago. The Great Pyramid is one of the wonders of the world!"
    
    elif any(word in q for word in ["dinosaur", "fossil"]):
        return "Answer: Dinosaurs lived millions of years ago; we learn about them from fossils\n\nExplanation: Fossils are remains of ancient animals preserved in rock. They show us what dinosaurs looked like and how they lived!"
    
    # General history concepts
    elif any(word in q for word in ["timeline", "chronology"]):
        return "Answer: A timeline shows events in the order they happened\n\nExplanation: It helps us understand when things occurred and how events connect to each other. Time moves from left to right or top to bottom!"
    
    elif any(word in q for word in ["artifact", "museum"]):
        return "Answer: Artifacts are old objects that teach us about the past\n\nExplanation: Things like pottery, tools, and clothing from long ago help historians understand how people lived in different time periods!"
    
    return None

def get_geography_response(question):
    """Handle geography-related questions"""
    q = question.lower()
    
    # Continents and oceans
    if any(word in q for word in ["continent", "seven continents"]):
        return "Answer: There are 7 continents: North America, South America, Europe, Asia, Africa, Australia, Antarctica\n\nExplanation: Continents are the largest land masses on Earth. Asia is the biggest, and Antarctica is the coldest!"
    
    elif any(word in q for word in ["ocean", "five oceans"]):
        return "Answer: There are 5 oceans: Pacific, Atlantic, Indian, Arctic, Southern\n\nExplanation: Oceans are huge bodies of salt water. The Pacific is the largest ocean, covering about one-third of Earth's surface!"
    
    elif any(word in q for word in ["equator", "hemisphere"]):
        return "Answer: The equator divides Earth into Northern and Southern hemispheres\n\nExplanation: It's an imaginary line around the middle of Earth where it's always warm. Countries near the equator have hot, tropical climates!"
    
    # Countries and capitals
    elif any(word in q for word in ["united states", "america", "usa"]):
        return "Answer: The United States has 50 states; the capital is Washington, D.C.\n\nExplanation: The U.S. is a large country in North America. Each state has its own capital city, but the nation's capital is Washington, D.C.!"
    
    elif any(word in q for word in ["canada", "canadian"]):
        return "Answer: Canada is north of the United States; the capital is Ottawa\n\nExplanation: Canada is the second-largest country in the world by area. It has provinces instead of states, and many people speak French and English!"
    
    elif any(word in q for word in ["mexico", "mexican"]):
        return "Answer: Mexico is south of the United States; the capital is Mexico City\n\nExplanation: Mexico is part of North America and has a rich culture with ancient civilizations like the Aztecs and Mayans!"
    
    # Physical features
    elif any(word in q for word in ["mountain", "peak", "range"]):
        return "Answer: Mountains are high areas of land formed by Earth's movements\n\nExplanation: Mountain ranges like the Rockies and Appalachians were formed when Earth's plates pushed together over millions of years!"
    
    elif any(word in q for word in ["river", "stream"]):
        return "Answer: Rivers are flowing bodies of fresh water that eventually reach the ocean\n\nExplanation: Rivers start in mountains or hills and flow downhill to lakes or oceans. They provide fresh water and transportation for people!"
    
    elif any(word in q for word in ["desert", "sahara"]):
        return "Answer: Deserts are very dry areas with little rainfall\n\nExplanation: Deserts get less than 10 inches of rain per year. The Sahara in Africa is the world's largest hot desert!"
    
    # Map skills
    elif any(word in q for word in ["map", "compass", "direction"]):
        return "Answer: Maps show places from above; compass directions are North, South, East, West\n\nExplanation: Maps help us find places and understand distances. A compass rose shows directions, with North usually at the top!"
    
    elif any(word in q for word in ["scale", "legend"]):
        return "Answer: Map scale shows real distances; legend explains map symbols\n\nExplanation: Scale tells you how far apart places really are. Legend (or key) explains what symbols, colors, and lines mean on the map!"
    
    return None

def get_art_response(question):
    """Handle art-related questions"""
    q = question.lower()
    
    # Primary colors and color theory
    if any(word in q for word in ["primary color", "primary colours"]):
        return "Answer: The primary colors are red, blue, and yellow\n\nExplanation: These are called primary because you can't make them by mixing other colors. All other colors can be made by mixing these three!"
    
    elif any(word in q for word in ["secondary color", "secondary colours"]):
        return "Answer: Secondary colors are orange, green, and purple\n\nExplanation: You make these by mixing primary colors: red + yellow = orange, blue + yellow = green, red + blue = purple!"
    
    elif any(word in q for word in ["color wheel", "colour wheel"]):
        return "Answer: A color wheel shows how colors relate to each other\n\nExplanation: It's arranged like a circle with primary colors evenly spaced, and secondary colors between them. Opposite colors are called complementary!"
    
    # Art techniques and tools
    elif any(word in q for word in ["paint", "painting", "brush"]):
        return "Answer: Painting uses brushes and paint to create artwork on surfaces\n\nExplanation: Different brushes make different marks - flat brushes for broad strokes, round brushes for details. You can paint with watercolors, tempera, or acrylic!"
    
    elif any(word in q for word in ["draw", "drawing", "pencil"]):
        return "Answer: Drawing uses pencils, crayons, or markers to make pictures\n\nExplanation: You can use different pencils for light or dark lines. Start with basic shapes like circles, squares, and triangles to build more complex drawings!"
    
    elif any(word in q for word in ["sculpture", "clay"]):
        return "Answer: Sculpture is 3D art made from materials like clay, stone, or metal\n\nExplanation: Unlike flat paintings, sculptures have height, width, and depth. You can walk around them and see them from all sides!"
    
    # Art elements
    elif any(word in q for word in ["line", "shape", "form"]):
        return "Answer: Line, shape, and form are basic elements of art\n\nExplanation: Lines can be straight, curved, thick, or thin. Shapes are flat (like circles), while forms are 3D (like spheres). They're the building blocks of art!"
    
    elif any(word in q for word in ["texture", "pattern"]):
        return "Answer: Texture is how something feels; pattern is designs that repeat\n\nExplanation: Texture can be rough, smooth, bumpy, or soft. Patterns repeat like stripes, polka dots, or checkerboards. Both make art more interesting!"
    
    # Famous artists (age-appropriate)
    elif any(word in q for word in ["vincent van gogh", "van gogh"]):
        return "Answer: Vincent van Gogh was a famous artist who painted with thick, swirling brushstrokes\n\nExplanation: He painted beautiful pictures like 'Starry Night' with its swirling sky. He used lots of paint to create texture you can actually feel!"
    
    elif any(word in q for word in ["leonardo da vinci", "mona lisa"]):
        return "Answer: Leonardo da Vinci painted the famous 'Mona Lisa' and was also an inventor\n\nExplanation: He lived over 500 years ago and was interested in art, science, and inventions. The Mona Lisa's mysterious smile is in a museum in France!"
    
    return None

def get_music_response(question):
    """Handle music-related questions"""
    q = question.lower()
    
    # Basic music concepts
    if any(word in q for word in ["note", "musical note"]):
        return "Answer: Musical notes represent different sounds and have names: A, B, C, D, E, F, G\n\nExplanation: Notes are like letters for music! Each note has a different pitch (how high or low it sounds). The pattern repeats: A, B, C, D, E, F, G, then A again!"
    
    elif any(word in q for word in ["rhythm", "beat"]):
        return "Answer: Rhythm is the pattern of beats in music, like a musical heartbeat\n\nExplanation: You can clap or tap to the beat! Some beats are strong (like 1-2-1-2) and some are gentle. Rhythm makes music fun to dance and march to!"
    
    elif any(word in q for word in ["melody", "tune"]):
        return "Answer: Melody is the tune - the main musical line you can sing along with\n\nExplanation: It's made of different notes going up and down, like 'Twinkle, Twinkle, Little Star.' The melody is usually what you remember most about a song!"
    
    # Instruments
    elif any(word in q for word in ["piano", "keyboard"]):
        return "Answer: Piano has black and white keys that make different sounds when pressed\n\nExplanation: White keys play natural notes (C, D, E, F, G, A, B), and black keys play sharp or flat notes. You can play melody with one hand and harmony with the other!"
    
    elif any(word in q for word in ["guitar", "string"]):
        return "Answer: Guitar is a stringed instrument you pluck or strum to make music\n\nExplanation: It has 6 strings that vibrate to make sound. Pressing strings in different places changes the pitch. You can play chords (multiple notes) or single notes!"
    
    elif any(word in q for word in ["drum", "percussion"]):
        return "Answer: Drums are percussion instruments that make sound when you hit them\n\nExplanation: Different drums make different sounds - big drums sound low and deep, small drums sound high and sharp. They help keep the rhythm in music!"
    
    elif any(word in q for word in ["violin", "bow"]):
        return "Answer: Violin is played with a bow that slides across strings to make sound\n\nExplanation: It's the smallest instrument in the string family and makes high, beautiful sounds. Moving the bow faster or slower changes how the music sounds!"
    
    # Music styles
    elif any(word in q for word in ["classical music", "orchestra"]):
        return "Answer: Classical music is performed by orchestras with many different instruments\n\nExplanation: An orchestra has four main groups: strings (violins, cellos), woodwinds (flutes, clarinets), brass (trumpets, trombones), and percussion (drums, cymbals)!"
    
    elif any(word in q for word in ["folk music", "traditional"]):
        return "Answer: Folk music tells stories and is passed down through families and communities\n\nExplanation: Different countries and cultures have their own folk songs that teach about their history, values, and daily life. Many folk songs are easy to sing along with!"
    
    # Music theory basics
    elif any(word in q for word in ["scale", "do re mi"]):
        return "Answer: A scale is a series of notes that go up or down: Do, Re, Mi, Fa, Sol, La, Ti, Do\n\nExplanation: This is called the major scale, and it sounds happy and bright. You might know it from 'The Sound of Music' - each note has its own special sound!"
    
    elif any(word in q for word in ["loud", "soft", "volume", "dynamics"]):
        return "Answer: Music can be played loudly (forte) or softly (piano) to create different feelings\n\nExplanation: Loud music can sound exciting or scary, while soft music can sound peaceful or mysterious. Musicians use Italian words: forte means loud, piano means soft!"
    
    return None

def get_response(subject, question):
    """Main function to get responses based on subject and question"""
    if not question.strip():
        return "🤔 I'd love to help, but I need a question first! What would you like to learn about?"
    
    q = question.lower()
    
    if subject == "Math":
        # --- Extract numbers ---
        try:
            numbers = list(map(int, re.findall(r'\d+', q)))
        except ValueError:
            numbers = []
        
        if len(numbers) >= 2:
            num1, num2 = numbers[0], numbers[1]

            # --- Detect operation ---
            if "multiply" in q or "times" in q or "x" in q:
                answer = num1 * num2
                return f"Answer: {answer}\n\nExplanation: {num1} × {num2} = {answer}. Multiplying means adding a number repeatedly."
            elif "add" in q or "plus" in q:
                answer = num1 + num2
                return f"Answer: {answer}\n\nExplanation: {num1} + {num2} = {answer}. Adding means putting numbers together."
            elif "subtract" in q or "minus" in q:
                answer = num1 - num2
                return f"Answer: {answer}\n\nExplanation: {num1} - {num2} = {answer}. Subtracting means taking away."
            elif "divide" in q or "divided" in q:
                if num2 != 0:
                    answer = num1 / num2
                    if answer == int(answer):
                        answer = int(answer)
                    return f"Answer: {answer}\n\nExplanation: {num1} ÷ {num2} = {answer}. Dividing means splitting into equal parts."
                else:
                    return "Answer: Cannot divide by zero\n\nExplanation: Division by zero is not possible in mathematics. You can't split something into zero groups!"

        # If no numbers found or only one number, try the existing math response function
        response = get_math_response(question)
        if response:
            return response
            
        return "Answer: I need more information\n\nExplanation: I see numbers, but I'm not sure what to do. Try using words like add, multiply, subtract, or divide."
    
    elif subject == "Reading":
        if "noun" in q:
            return "Answer: A noun is a person, place, or thing.\n\nExplanation: Examples include 'dog', 'school', and 'pencil'. Nouns name people, places, and things."
        elif "verb" in q:
            return "Answer: A verb is an action word.\n\nExplanation: Examples include 'run', 'jump', and 'write'. Verbs show what someone or something is doing."
        elif "adjective" in q:
            return "Answer: An adjective is a describing word.\n\nExplanation: It tells more about a noun. Examples: 'blue car', 'tall girl', or 'funny story'."
        else:
            response = get_reading_response(question)
            if response:
                return response

    elif subject == "Science":
        if "gravity" in q:
            return "Answer: Gravity is a force that pulls objects down to Earth.\n\nExplanation: It keeps us from floating away and makes things fall when dropped."
        elif "water cycle" in q:
            return "Answer: The water cycle describes how water moves through Earth.\n\nExplanation: It includes evaporation (water rising), condensation (clouds forming), and precipitation (rain falling)."
        elif "plant" in q:
            return "Answer: Plants need sunlight, water, air, and soil to grow.\n\nExplanation: They use sunlight to make food in a process called photosynthesis."
        else:
            response = get_science_response(question)
            if response:
                return response
    
    elif subject == "History":
        response = get_history_response(question)
        if response:
            return response
    
    elif subject == "Geography":
        response = get_geography_response(question)
        if response:
            return response
    
    elif subject == "Art":
        response = get_art_response(question)
        if response:
            return response
    
    elif subject == "Music":
        response = get_music_response(question)
        if response:
            return response
    
    return "Hmm... Genie's still learning that one! Try asking a question about your chosen subject. 🧞"

# Show question interface only in Ask Questions mode
if mode == "❓ Ask Questions":
    # Create two columns for the button and additional info
    col1, col2 = st.columns([2, 1])

    with col1:
        # Ask the Genie button
        ask_button = st.button("🔮 Ask the Genie!", type="primary")

    with col2:
        # Show a tip
        if st.button("💡 Show Tip"):
            tips = {
                "Math": "Try asking about numbers, shapes, or math operations like adding and multiplying!",
                "Reading": "Ask about parts of speech, reading strategies, or story elements!",
                "Science": "Wonder about plants, animals, weather, or how things work!",
                "History": "Ask about famous people, important events, or how people lived long ago!",
                "Geography": "Wonder about countries, continents, oceans, or places around the world!",
                "Art": "Ask about colors, drawing, painting, or famous artists and their work!",
                "Music": "Wonder about instruments, songs, rhythm, or how music is made!"
            }
            st.info(f"💡 **Tip for {subject_clean}:** {tips.get(subject_clean, 'Keep asking questions!')}")

    # Process the question when button is clicked
    if ask_button:
        if user_question.strip():
            with st.spinner("🔮 The Genie is thinking..."):
                answer = get_response(subject_clean, user_question)
                
                # Log the interaction to database
                log_user_interaction(
                    subject=subject_clean,
                    question_asked=user_question,
                    answer_provided=answer,
                    session_id=st.session_state.session_id
                )
            
            # Display the answer with nice formatting
            st.success("💬 **Genie says:**")
            st.write(answer)
            
            # Add some encouragement
            st.balloons()
            
            # Suggest asking another question
            st.info("🎓 Got another question? The Genie loves to help you learn!")
            
        else:
            st.warning("📝 Please type a question first, then ask the Genie!")

# Sidebar with database statistics and admin features
with st.sidebar:
    st.write("### 📊 Learning Stats")
    
    # Add admin toggle
    show_admin = st.checkbox("🔧 Show Admin Panel", value=False)
    
    try:
        # Get interaction statistics
        stats = get_interaction_stats()
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Questions Asked", stats["total_questions"])
        with col2:
            st.metric("Practice Problems", stats["total_practice"])
        
        # Show questions by subject
        if stats["subject_stats"]:
            st.write("**Questions by Subject:**")
            for subject, count in stats["subject_stats"]:
                st.write(f"• {subject}: {count}")
        
        # Show practice stats by subject
        if stats["practice_stats"]:
            st.write("**Practice Performance:**")
            for subject, total, correct in stats["practice_stats"]:
                if total and correct is not None:
                    accuracy = (correct / total) * 100 if total > 0 else 0
                    st.write(f"• {subject}: {correct}/{total} ({accuracy:.1f}%)")
        
        # Show popular topics for current subject
        popular_topics = get_popular_topics(subject_clean, limit=3)
        if popular_topics:
            st.write(f"**Popular {subject_clean} Topics:**")
            for topic in popular_topics:
                st.write(f"• {topic.topic_name.title()}: {topic.question_count} questions")
        
        # Recent activity indicator
        if stats["total_questions"] > 0:
            st.success("🎯 Database is active!")
        else:
            st.info("🌟 Be the first to ask a question!")
            
    except Exception as e:
        st.error("📊 Stats temporarily unavailable")

# Admin Panel (if enabled)
if show_admin:
    st.write("---")
    st.write("### 🔧 Admin Dashboard")
    
    admin_tab1, admin_tab2, admin_tab3 = st.tabs(["📈 Statistics", "💬 Recent Questions", "🗃️ Database"])
    
    with admin_tab1:
        try:
            stats = get_interaction_stats()
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total Questions", stats["total_questions"])
            with col2:
                st.metric("Unique Sessions", len(set([q.session_id for q in stats["recent_questions"] if q.session_id])))
            
            # Subject breakdown chart
            if stats["subject_stats"]:
                import pandas as pd
                df = pd.DataFrame(stats["subject_stats"], columns=['Subject', 'Count'])
                st.bar_chart(df.set_index('Subject'))
                
        except Exception as e:
            st.error(f"Error loading stats: {e}")
    
    with admin_tab2:
        try:
            stats = get_interaction_stats()
            st.write("**Recent Questions:**")
            
            for q in stats["recent_questions"]:
                with st.expander(f"{q.subject}: {q.question_asked[:50]}..."):
                    st.write(f"**Question:** {q.question_asked}")
                    st.write(f"**Answer:** {q.answer_provided[:200]}...")
                    st.write(f"**Time:** {q.created_at}")
                    st.write(f"**Session:** {q.session_id}")
                    
        except Exception as e:
            st.error(f"Error loading recent questions: {e}")
    
    with admin_tab3:
        try:
            from database import get_db, Question, UserInteraction, PopularTopics
            
            db = get_db()
            
            # Database table counts
            question_count = db.query(Question).count()
            interaction_count = db.query(UserInteraction).count()
            topic_count = db.query(PopularTopics).count()
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Questions in DB", question_count)
            with col2:
                st.metric("User Interactions", interaction_count)
            with col3:
                st.metric("Popular Topics", topic_count)
            
            # Show all popular topics
            st.write("**All Popular Topics:**")
            topics = get_popular_topics(limit=20)
            if topics:
                topics_df = pd.DataFrame([
                    {"Subject": t.subject, "Topic": t.topic_name, "Count": t.question_count, "Last Asked": t.last_asked}
                    for t in topics
                ])
                st.dataframe(topics_df)
            
            db.close()
            
        except Exception as e:
            st.error(f"Error accessing database: {e}")

# Footer with helpful information
st.write("---")
st.write("### 🌟 How to get the best help:")
st.write("• **Be specific** - instead of 'math help', try 'how do I multiply 6 times 4?'")
st.write("• **Use key words** - mention the topic you're learning about")
st.write("• **Don't give up** - if the Genie doesn't know something, ask your teacher!")

# Fun fact section
with st.expander("🎯 Fun Learning Facts"):
    fun_facts = {
        "Math": [
            "Zero was invented about 1,500 years ago!",
            "The word 'mathematics' comes from the Greek word 'mathema' meaning 'knowledge'!",
            "Ancient people counted on their fingers and toes - that's why we use base 10!"
        ],
        "Reading": [
            "The average person reads about 250 words per minute!",
            "Reading for just 6 minutes can reduce stress by 68%!",
            "The word 'bookworm' comes from insects that actually eat books!"
        ],
        "Science": [
            "A group of flamingos is called a 'flamboyance'!",
            "Lightning is five times hotter than the surface of the Sun!",
            "Butterflies taste with their feet!"
        ]
    }
    
    facts = fun_facts.get(subject_clean, ["Learning is the best adventure!"])
    for fact in facts:
        st.write(f"• {fact}")

# Study tips based on subject
with st.expander("📚 Study Tips"):
    study_tips = {
        "Math": [
            "Practice a little bit every day - math builds on itself!",
            "Draw pictures or use objects to help you understand problems",
            "Check your work by doing the problem a different way",
            "Don't be afraid to make mistakes - they help you learn!"
        ],
        "Reading": [
            "Read a little bit every day to improve your skills",
            "Ask questions about what you read to check understanding",
            "Look up words you don't know and use them in sentences",
            "Read different types of books to expand your vocabulary"
        ],
        "Science": [
            "Observe the world around you and ask 'why' and 'how'",
            "Try simple experiments at home (with adult help!)",
            "Keep a science journal to record your observations",
            "Connect what you learn to things you see in real life"
        ]
    }
    
    tips = study_tips.get(subject_clean, ["Stay curious and keep learning!"])
    for tip in tips:
        st.write(f"• {tip}")
