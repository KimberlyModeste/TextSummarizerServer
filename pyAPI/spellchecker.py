from symspellpy import SymSpell, Verbosity
import pkg_resources

sym_spell = SymSpell()
dictionary_path = pkg_resources.resource_filename(
    "symspellpy", "frequency_dictionary_en_82_765.txt"
)
sym_spell.load_dictionary(dictionary_path, 0, 1)
myString = "Hello my naem is Kimberly"
# mystring = myString.split(' ')

# print(mystring[2])

# suggestions = sym_spell.lookup(mystring[0], Verbosity.CLOSEST, max_edit_distance=2)[0].term
ns = ''

for word in myString.split(' '):
	temp=sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)[0].term
	if(word[0].islower()):
		ns+=temp+' '
	else:
		ns+=temp.capitalize()+' '

	# suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)[0].term
	# print(suggestions[0])
ns = ns[:-1]
print(ns)

# print(suggestions)


# for suggestion in suggestions:
#     print(suggestion.term[0])