b = 1
c = 5

def func1(*args):
    arg1, arg2, arg3 = args
    a = b + c
    print "This is %s and %r %r but a = %r" % (arg1, arg2, arg3, a)

def func2(arg1):
    arg1 = "a" + arg1
    print ("Baaang!!! arg1 = %r") % arg1

func1('Cool', 'F*cking', 'Awesome')
func2("b")
