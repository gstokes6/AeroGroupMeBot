from MESSAGE_FLAGS import messageFlag

##for seeing if academic is invoked
from MESSAGE_FLAGS import isAcademicInvoked

##some needed modules
import random

class isWheelSpin(messageFlag.messageFlag):
    def __init__(self,message):
        super().__init__(message)
        
    def checkTrue(self,message):
        ##Logic to find if flag is set
        
        ##first see if invoked
        invokedFlag = isAcademicInvoked.isAcademicInvoked(message)
        isInvoked = invokedFlag.isTrue
        
        ##see if keyword is in message
        Msg = message['text'].lower()
        isKeyPhrase = ( "spin the wheel" in Msg )

        if (isKeyPhrase and isInvoked):
            self.isTrue = True
        
    def response(self):
        Names = ['Brandon Alkire', 'Thomas Benda', 'Jon Blaine', 'Laken Boone', 'Jacob Bosarge', 'Ryan Bowman', 'Dakota Burkhalter', 'Adam Burkley', 'Ike Callaway', 'Brandon Carlile', 'Madison Carrens', 'James Carver', 'Jared Chappell', 'Anthony Comer', 'Thomas Cox', 'Weston Craig', 'Jared Culberson', 'Yurou Dai', 'James Dimmette', 'Matthew Gallagher', 'Levi Gosdin', 'Zachary Griffin', 'Andrew Guazzerotti', 'Brayden Guevarra', 'Anderson Hamilton', 'Liam Hamilton', 'Christopher Heilmann', 'Ezekiel Hietala', 'Xingran Huang', 'Coleson Jeffries', 'Samuel Jones', 'Devantia Jordan', 'Timothy Jordan', 'Harrison Kerr', 'Martin Kloser', 'Joseph Kolar', 'Paul Last', 'Benjamin Lattner', 'Austen Lebeau', 'Craige Legrand', 'Joshua Losch', 'Matthew Lutz', 'Tristan Macke', 'Jordan Martindale', 'William McAtee', 'Brenden McGath', 'Katherine Milbrandt', 'Anna Miller', 'Andre Montenegro', 'Keaton Morris', 'Rebecca Morris', 'Robert Mulholland', 'Tanner Nardone', 'Dakota Newsome', 'Michael Onken', 'Megan Parker', 'Grady Pastor', 'Ethan Peterson', 'Maverick Pierce', 'Kyle Ramirez', 'Boyu Ran', 'Henry Reagan', 'Seth Rhodes', 'Cassandra Richmond', 'William Robinson', 'Ethan Russell', 'Matthew Seay', 'Zixi Shi', 'Gavin Smith', 'Harrison Smith', 'Gavin Stokes', 'Harrison Taylor', 'Hunter Terry', 'Garrett Vickery', 'Zachary Wadzinski', 'Jacob Wallace', 'Taylor Watson', 'Samuel Wheeler', 'Benjamin Williams', 'Jason Williamson', 'Bradley Windom', 'Dylan Young']
        randnum = random.randrange(len(Names))
        Person = Names[randnum]
        ans = 'The random number is '+str(randnum+3)+', so fuck '+Person+' in particular.'
        groupMe.reply(ans)
        
