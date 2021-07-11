from tesla import Tesla
def test_color():
    tesla= Tesla('S', 'red')
    assert tesla.color() == 'red'

#def test_seats_count():
    #tesla= Tesla('S', 'red')
    #assert tesla.seats_count == 2

def test_unlock(self):
    tesla= Tesla('S', 'red')
    assert tesla.unlock()