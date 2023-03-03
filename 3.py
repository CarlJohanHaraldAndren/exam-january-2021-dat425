class Doorlock():
    def __init__(self, pin):
        # initialize the class with a pin and the open attribute set to False
        self.pin = pin
        self.open = False

    def lock(self):
        # if the door is open, then lock it and return True
        if self.open == True:
            self.open = False
            return True
        else:
            # if the door is already locked, return False
            return False

    def unlock(self, pin):
        # if the provided 'pin' matches the class' 'pin' and the door is locked, unlock it and return True
        if self.pin == pin and self.open == False:
            self.open = True
            return True
        else:
            # if the 'pin' does not match or the door is already unlocked, return False
            return False

    def setpin(self, pin, new_pin):
        # if the provided 'pin' matches the class' 'pin', change the 'pin' attribute to the 'new_pin' and return True
        if self.pin == pin and self.open == False:
            self.pin = new_pin
            return True
        else:
            # if the 'pin' does not match or the door is unlocked, return False
            return False
