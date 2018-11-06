import sys

if len(sys.argv) != 2:
	print "Uso: " + sys.argv[0] + " texto"
	sys.exit(0)

print "hola mundo " + sys.argv[1]
