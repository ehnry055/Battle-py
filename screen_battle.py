from tkinter import *

class Screen_Battle(Frame):
    def __init__ (self, master, player1, player2, callback_on_exit):
        super().__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points

        # Save the method reference to which we return control after this page Exits.
        self.callback_on_exit = callback_on_exit

        self.create_widgets()
        self.grid()
        
    def create_widgets (self):
        '''
        This method creates all of the (initial) widgets for the battle page.
        '''
        Label(self, text = "You").grid(row = 4, column = 0, sticky = N)
        Label(self, text = "Computer").grid(row = 4, column = 14, sticky = N)

        you = PhotoImage(file="images/"+ str(self.player1.large_image))
        image1 = Label(self, image = you, )
        image1.photo = you
        image1.grid(row = 5, column = 0, sticky = W)

        cpu = PhotoImage(file="images/"+ str(self.player2.large_image))
        image2 = Label(self, image = cpu, )
        image2.photo = cpu
        image2.grid(row = 5, column = 14, sticky = E)

        Label(self, text = f"{self.player1.hit_points} HP").grid(row = 6, column = 0, sticky = N)
        Label(self, text = f"{self.player2.hit_points} HP").grid(row = 6, column = 14, sticky = N)
            
            
        
    def attack_clicked(self):
        ''' This method is called when the user presses the "Attack" button.
            
            This method does the following:
            1) Calls the character.attack method for both the player and (if still alive) the computer.
            2) Updates the labels on the top right with the results of the attacks.
            3) Determines if there was a victor, and if so display that info 
            4) If there is a victor, remove the Attack button.  Create an Exit button to replace it.  

            To remove a widget, use the destroy() method. For example:
    
                self.button.destroy()   
        '''        
        pass
                                            
    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked. 
            It passes control back to the callback method. '''        
        self.callback_on_exit()