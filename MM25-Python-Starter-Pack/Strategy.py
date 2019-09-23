from API import Game
import random
import sys

class Strategy(Game):
    def __init__(self, game_json):
        self.rounds = 0
        self.movement = []
        Game.__init__(self, game_json)
    """
        FILL THIS METHOD OUT FOR YOUR BOT:
        Method to set unit initializations. Run at the beginning of a game, after assigning player numbers.
        We have given you a default implementation for this method.
        OUTPUT:
            An array of 3 dictionaries, where each dictionary details a unit. The dictionaries should have the following fields
                "health": An integer indicating the desired health for that unit
                "speed": An integer indicating the desired speed for that unit
                "unitId": An integer indicating the desired id for that unit. In this provided example, we assign Ids 1,2,3 if you are player1, or 4,5,6 if you are player2
                "attackPattern": a 7x7 2d integer list indicating the desired attack pattern for that unit
                "terrainPattern": a 7x7 2d boolean list indicating the desired terrain pattern for that unit.
        Note: terrainPattern and attackPattern should be indexed x,y. with (0,0) being the bottom left
        If player_id is 1, UnitIds for the bots should be 1,2,3. If player_id is 2, UnitIds should be 4,5,6
    """
    def get_setup(self):
        unit_1 = {"health": 6, "speed": 5, "attackPattern": [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 2, 2],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]], "unitId": 1}
        if self.player_id == 2:
            unit_1["unitId"] = 4
        unit_1["terrainPattern"] = [
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False],
        [False, False, False, False, False, False, False]]

        unit_2 = {"health": 6, "speed": 5, "attackPattern": [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 2, 2],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]], "unitId": 2}
        if self.player_id == 2:
            unit_2["unitId"] = 5
        unit_2["terrainPattern"] = [
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False]]

        unit_3 = {"health": 6, "speed": 5, "attackPattern": [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 2, 2, 2],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]], "unitId": 3}
        if self.player_id == 2:
            unit_3["unitId"] = 6
        unit_3["terrainPattern"] = [
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False]]

        units = [unit_1, unit_2, unit_3]
        return units
    """
        FILL THIS METHOD OUT FOR YOUR BOT:
        Method to implement the competitors strategy in the next turn of the game.
        We have given you a default implementation here.
        OUTPUT:
            A list of 3 dictionaries, each of which indicates what to do on a given turn with that specific unit. Each dictionary should have the following keys:
                "unitId": The Id of the unit this dictionary will detail the action for
                "movement": an array of directions ("UP", "DOWN", "LEFT", or "RIGHT") details how you want that unit to move on this turn
                "attack": the direction in which to attack ("UP", "DOWN", "LEFT", or "RIGHT")
                "priority": The bots move one at a time, so give the priority which you want them to act in (1,2, or 3)
    """
    def do_turn(self):
        my_units = self.get_my_units()
        enemy_units = self.get_enemy_units()
        direction = ["UP", "DOWN", "LEFT", "RIGHT"]

        decision = []
        self.rounds = 0

        for i in my_units:
            self.rounds += 1
            if i.id == 1 or i.id==4:
                moves = self.no_collide(i, self.choose_move(i, enemy_units[-1]))
                self.movement = moves
                fire = self.destination(i, moves)
                decision.append({"priority": 3,
                                 "movement": moves,
                                 "attack": self.choose_atk(i, fire, direction), # if moves[0]!="STAY" else "DOWN" if i.player_id==1 else "UP",
                                 "unitId": i.id})
            elif i.id==2 or i.id==5:
                moves = self.no_collide(i, self.choose_move(i, enemy_units[-1]))
                self.movement = moves
                fire = self.destination(i, moves)
                decision.append({"priority": 1,
                                 "movement": moves,
                                 "attack": self.choose_atk(i, fire, direction) if moves[0]!="STAY" else "DOWN" if i.player_id==1 else "UP",
                                 "unitId": i.id})
            else:
                moves= self.no_collide(i, self.choose_move(i, enemy_units[-1]))
                self.movement = moves
                fire = self.destination(i, moves)
                decision.append({"priority": 2,
                                 "movement": moves,
                                 "attack": self.choose_atk(i, fire, direction) if moves[0]!="STAY" else "RIGHT" if i.player_id==1 else "LEFT",
                                 "unitId": i.id})
        self.rounds = 0
        return decision

    def get_enemy_positions(self):
        enemy_units = Game.get_enemy_units(self)
        enemy_positions = []
        for i in enemy_units:
            e_x = i.pos.x
            e_y = i.pos.y
            enemy_positions.append((e_x, e_y))
        return enemy_positions

    def get_friendly_positions(self):
        my_units = Game.get_my_units(self)
        my_positions = []
        priority = 0
        #If i is <= rounds, which means it has already moved.
        # (m_x,m_y) = destination(moves)
        for i in my_units:
            if(i.id %3 == 1):
                priority = 3
            elif(i.id %3 == 2):
                priority = 1
            elif(i.id %3 == 0):
                priority = 2

            if(priority <= self.rounds):
                my_positions.append(self.destination(i, self.movement))
            else:
                m_x = i.pos.x
                m_y = i.pos.y
                my_positions.append((m_x,m_y))
        return my_positions

    # Returns an array of tuples representing terrain
    def get_danger(self):
        grid = self.game["tiles"]
        dangerous = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j]["type"] == 'DESTRUCTIBLE' or grid[i][j]["type"] == 'INDESTRUCTIBLE':
                    dangerous.append((i, j))
        return dangerous

    def move_clamp(self, n, s):
        if len(n) > s:
            n = n[:s]
        while len(n) < s:
            n.append("STAY")
        return n

    def atk_range(self, u, d):
        pos = []
        for i in d:
            l = self.get_positions_of_attack_pattern(u.id, i)
            for j in l:
                pos.append((j[0].x, j[0].y))
        return pos

    def choose_atk(self, unit, pos, direct):
        for i in direct:
            atk = []
            l = self.get_positions_of_attack_pattern(unit.id, i, pos)
            for j in l:
                atk.append((j[0].x, j[0].y))
            for k in self.get_enemy_positions():
                if k in atk:
                    return i
        return "STAY"


        # Determine if target is going to move current turn
        # If yes, don't attack
        # If target has already moved, we can't get new destination right? So don't attack.
        # Basically our attack options are limited to who HASN'T moved during the turn

    def choose_move(self, f_unit, e_unit):
        # Find shortest safe path to given enemy unit
        route = self.path_to((f_unit.pos.x, f_unit.pos.y), (e_unit.pos.x, e_unit.pos.y), self.get_danger())
        des = (e_unit.pos.x, e_unit.pos.y)
        if route is None:
            des = [(5, 5), (4, 4), (3, 3)] if self.player_id==1 else [(6,6), (7,7), (8,8)]
            return self.move_clamp(self.path_to((f_unit.pos.x, f_unit.pos.y), des[(f_unit.id-1)%3], self.get_danger()), f_unit.speed)
        return self.move_clamp(route, f_unit.speed)

    def get_valid(self, unit, des):
        pos =[]
        start_x = unit.pos.x
        start_y = unit.pos.y
        end_x = des[0]
        end_y = des[1]
        x_change = abs(end_x - start_x)
        y_change = abs(end_y - start_y)

        for i in range(x_change):
            if start_x < end_x:
                pos.append((start_x+i, start_y))
            else:
                pos.append((start_x-i, start_y))

        for i in range(len(pos)):
            if pos[i] in self.get_danger():
                return pos[i-1]

        pos.clear()

        for i in range(y_change):
            if start_y < end_y:
                pos.append((end_x, start_y+i))
            else:
                pos.append((end_x, start_y-i))

        for i in range(len(pos)):
            if pos[i] in self.get_danger():
                return pos[i-1]
        return des

    def no_collide(self, unit, path):

        # We need to update get_friendly_positions each time someone moves
        # Then information will be accurate

        stay = False
        collide = self.get_enemy_positions() + self.get_friendly_positions()
        x = unit.pos.x
        y = unit.pos.y
        for i in range(len(path)):
            if(stay):
                path[i] = "STAY"
            else:
                if path[i] is "UP":
                    y+=1
                elif path[i] is "DOWN":
                    y-=1
                elif path[i] is "LEFT":
                    x-=1
                elif path[i] is "RIGHT":
                    x+=1
                for j in collide:
                    if j == (x,y):
                        stay = True
                        path[i] = "STAY"
        return path

    def destination(self, unit, moves):
        x = unit.pos.x
        y = unit.pos.y
        for i in range(len(moves)):
            if moves[i] is "UP":
                y += 1
            elif moves[i] is "DOWN":
                y -= 1
            elif moves[i] is "LEFT":
                x -= 1
            elif moves[i] is "RIGHT":
                x += 1
        return (x, y)
