
import re

print ("Enter ref:")
ref = input()

ref = ref.replace(":", ".")
ref = ref.capitalize()
ref = (re.split(r'\s',ref))
ref.append("-")
ref[0] = ref[0] + '.'
newref = ''.join(ref)
print(newref)