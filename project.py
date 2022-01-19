snakes = {
            17:7,
            62:19,
            54:34,
            87:36,
            64:60,
            93:73,
            95:75,
            98:76
    }

    # key is starting position of ladder
    # value is ending position of ladder
    # Therefore (key < value)
        ladders = {
            1:38,
            4:14,
            9:31,
            21:42,
            28:84,
            51:67,
            72:91,
            80:99
        }
        player_one_name = 'Aadil'
        player_one_initial_position = 0
        player_one_final_position = 0

        player_two_name = 'Aquib'
        player_two_initial_position = 0
        player_two_final_position = 0
        def play(self):
        while (self.player_one_final_position <= 100 or self.player_two_final_position <= 100) :
        # player one rolls the dice 
            print(self.player_one_name +' is playing')
            dice_value = random.choice([1,2,3,4,5,6])
            if self.player_one_final_position + dice_value <= 100 :
                self.player_one_final_position = self.player_one_final_position + dice_value
                print(self.player_one_name + ' rolled a '+str(dice_value)+' and moved from the position '+str(self.player_one_initial_position)+' to the position '+str(self.player_one_final_position)+'\n')
                self.player_one_initial_position = self.player_one_final_position

            # snake bite checking 
            if self.player_one_initial_position in self.snakes.keys():
                print('oh no......!!!!!!!, '+self.player_one_name+' got snake-bite by '+str(self.snakes[self.player_one_initial_position])+' positions')
                self.player_one_final_position = self.snakes[self.player_one_initial_position]
                print(self.player_one_name+' moved down to '+str(self.player_one_final_position)+' position due to snake bite'+'\n')
                self.player_one_initial_position = self.player_one_final_position

            # ladder luck checking
            if self.player_one_initial_position in self.ladders.keys():
                print('woo-hoo..!!, '+self.player_one_name+' got lucky to climb ladder to '+str(self.ladders[self.player_one_initial_position])+' position')
                self.player_one_final_position = self.ladders[self.player_one_initial_position]
                print(self.player_one_name+' moved up to '+str(self.player_one_final_position)+' position due to ladder'+'\n')
                self.player_one_initial_position = self.player_one_final_position

            # checking for winner 
            if (self.player_one_final_position == self.player_one_initial_position == 100) :
                print(self.player_one_name+' has won the game, Hurray!!!')
                break 
            

        # player two rolls the dice
            print(self.player_two_name +' is playing')
            dice_value = random.choice([1,2,3,4,5,6])
            if self.player_two_final_position + dice_value <= 100 :
                self.player_two_final_position = self.player_two_final_position + dice_value
                print(self.player_two_name + ' rolled a '+str(dice_value)+' and moved from the position '+str(self.player_two_initial_position)+' to the position '+str(self.player_two_final_position)+'\n')
                self.player_two_initial_position = self.player_two_final_position

            # snake bite checking 
            if self.player_two_initial_position in self.snakes.keys():
                print('oh no......!!!!!!!, '+self.player_two_name+' got snake-bite by '+str(self.snakes[self.player_two_initial_position])+' positions')
                self.player_two_final_position = self.snakes[self.player_two_initial_position]
                print(self.player_two_name+' moved down to '+str(self.player_two_final_position)+' position due to snake bite'+'\n')
                self.player_two_initial_position = self.player_two_final_position

            # ladder luck checking
            if self.player_two_initial_position in self.ladders.keys():
                print('woo-hoo..!!, '+self.player_two_name+' got lucky to climb ladder to '+str(self.ladders[self.player_two_initial_position])+' position')
                self.player_two_final_position = self.ladders[self.player_two_initial_position]
                print(self.player_two_name+' moved up to '+str(self.player_two_final_position)+' position due to ladder'+'\n')
                self.player_two_initial_position = self.player_two_final_position

            # checking for winner
            if (self.player_two_final_position == self.player_two_initial_position == 100) :
                print(self.player_two_name+' has won the game, Hurray!!!')
                break