# import XML libraries
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import HTMLParser
import sys
import os

instructions = """
To use:
python SetMaxAttempts.py number path/to/problem/folder

Your options for the number are:
  - An actual number, which sets all problems to the same # of attempts
  - delete or default, which removes the value to allow the course-wide default to take over
  - auto (recommended), in which case attempts are set as follows:
    - Numerical and Formula problems get 10
    - Customresponse and Text problems get 5
    - Checkbox problems get a number of attempts equal to the number of choices, max 5.
    - MC problems get...
      - 3 if they have 7+ options
      - 2 if they have 4-6 options
      - 1 if they have 2-3 options
    - Multi-problems get the highest number of the set. 

There will probably still be some issues, so you'll need to review. This code will help you make a first pass, not a final pass.
"""

# Here are all the problem types we work on:
allProbtypes = ['multiplechoiceresponse',
    'choiceresponse',
    'customresponse',
    'formularesponse',
    'numericalresponse',
    'stringresponse',
]



# Get directory from command line argument
try:
    numberAttempts = sys.argv[1]
    directory = sys.argv[2]
except IndexError:
    # Probably the wrong number of arguments
    sys.exit(instructions)

# Walk through the problems folder
for dirpath, dirnames, filenames in os.walk(directory):
    for eachfile in filenames:
        thisProbType = []
        
        # Get the XML for each file
        tree = ET.parse(os.path.join(dirpath, eachfile))
        root = tree.getroot()
        
        # Auto-set the showanswer value 
        if numberAttempts.lower() == 'auto':
            
            # Check the problem type
            for probtype in allProbtypes:
                for item in root.iter(probtype):
                    thisProbType.append(item.tag)
        
            # Check for number of choice elements
            numberOptions = len(list(root.iter('choice')))
        
            # Set number of attempts properly
            if 'multiplechoiceresponse' in thisProbType:
                if numberOptions <= 3:
                    root.set('max_attempts', '1')
                elif numberOptions <= 6:
                    root.set('max_attempts', '2')
                else:
                    root.set('max_attempts', '3')
        
            if 'choiceresponse' in thisProbType:
                root.set('max_attempts', str(numberOptions) if numberOptions <= 5 else '5')
        
        
            if 'customresponse' in thisProbType or 'stringresponse' in thisProbType:
                root.set('max_attempts', '5')
        
            if 'formularesponse' in thisProbType or 'numericalresponse' in thisProbType:
                root.set('max_attempts', '10')
        
        # Remove the max_attempts value to allow unlimited attempts or course default
        elif numberAttempts.lower() == 'default' or numberAttempts.lower() == 'default':
            try:
                del root.attrib['max_attempts']
            except:
                pass

        # For non-auto mode.
        else:
            root.set('max_attempts', numberAttempts)
            
        
        # Save the file
        tree.write(os.path.join(dirpath, eachfile), encoding='UTF-8', xml_declaration=False)