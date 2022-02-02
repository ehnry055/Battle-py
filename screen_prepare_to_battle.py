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

        Label(self, text = "You").grid(row = 0, column = 1, sticky = N)
        Label(self, text = "Computer").grid(row = 0, column = 2, sticky = N)

        for i in range(1, 3):
            if i == 1:
                p = self.player1
            else:
                p = self.player2

            character = PhotoImage(file="images/" + str(p.large_image))
            image = Label(self, image = character, )
            image.photo = character
            image.grid(row = 1, column = i, sticky = W)

            Label(self, text = f"{p.hit_points} HP\n{p.dexterity} Dexterity\n{p.strength} Strength").grid(row = 2, column = i, sticky = N)

        Button(self, text = "Commence Battle!", fg = "Red", command = self.commence_battle_clicked).grid(row = 5, column = 2, sticky = E)


    def commence_battle_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''         
        self.callback_on_commence_battle()
            
        