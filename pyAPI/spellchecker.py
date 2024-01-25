from symspellpy import SymSpell, Verbosity
import pkg_resources
import sys

#Get SymSpell running
sym_spell = SymSpell() 

#Open the Symspell dictionary
dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt"
) 
#Load symspell dictionary 
sym_spell.load_dictionary(dictionary_path, 0, 1)

#Retriving my text
text = sys.argv[1]

new_string = ''

# Splitting the words individually and looking them up the taking the top 
# result and adding it to the new sentence.
for word in text.split(' '):
	temp=sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)[0].term
	if(word[0].islower()):
		new_string+=temp+' '
	else:
		new_string+=temp.capitalize()+' '

# Deleting last character which is a space
new_string = new_string[:-1]

# Sending back sentence as a hex so no information is lost.
print(new_string.encode(encoding="utf-8").hex())
