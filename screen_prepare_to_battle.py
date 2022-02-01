from tkinter import *

class Screen_PrepareToBattle(Frame):
    def __init__ (self, master, player1, player2, callback_on_commence_battle):
        super().__init__(master)

        # Save player character object references
        self.player1 = player1
        self.player2 = player2
        
        # Save the method reference to which we return control after the player hits "Next"
        self.callback_on_commence_battle = callback_on_commence_battle
        
        self.create_widgets()
        self.grid()
        
    
    def create_widgets (self):
        '''
        This method creates all of the widgets the prepare to battle page.
        '''
        Label(self, text = "You").grid(row = 0, column = 0, sticky = N)
        Label(self, text = "Computer").grid(row = 0, column = 14, sticky = N)

        you = PhotoImage(file="images/"+ str(self.player1.large_image))
        image1 = Label(self, image = you, )
        image1.photo = you
        image1.grid(row = 1, column = 0, sticky = W)

        cpu = PhotoImage(file="images/"+ str(self.player2.large_image))
        image2 = Label(self, image = cpu, )
        image2.photo = cpu
        image2.grid(row = 1, column = 14, sticky = E)

        Label(self, text = f"{self.player1.hit_points} HP\n{self.player1.dexterity} Dexterity\n{self.player1.strength} Strength").grid(row = 2, column = 0, sticky = N)
        Label(self, text = f"{self.player2.hit_points} HP\n{self.player2.dexterity} Dexterity\n{self.player2.strength} Strength").grid(row = 2, column = 14, sticky = N)

        Button(self, text = "Commence Battle!", fg = "Red", command = self.commence_battle_clicked).grid(row = 5, column = 14, sticky = E)


 
    def commence_battle_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.callback_on_commence_battle()
            
        