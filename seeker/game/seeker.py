# TODO: Implement the Seeker class as follows...
import random
class Seeker:
# 1) Add the class declaration. Use the following class comment.

    """The person looking for the Hider. 
    
    The responsibility of a Seeker is to keep track of its location and distance travelled.
    
    Attributes:
        location (int): The location of the Seeker (1-1000).
    """

    def __init__(self):
        """Constructs a new Seeker.

        Args:
            self (Seeker): An instance of Seeker.
        """
        self._location = random.randint(1, 1000)

    def get_location(self):
# 3) Create the get_location(self) method. Use the following method comment.
        """Gets the current location.
        
        Returns:
            number: The current location,
        """
        return self.location

    def move_location(self, location):
# 4) Create the move_location(self, location) method. Use the following method comment.
        """Moves to the given location.


        Args:
            self (Seeker): An instance of Seeker.
            location (int): The given location.
        """
        self._location = location