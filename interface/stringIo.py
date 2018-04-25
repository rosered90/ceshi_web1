from io import BytesIO as StringIO

f = StringIO()
print f.write('hello')
print f.write('hello fang')
print (f.getvalue())