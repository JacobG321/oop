
players = [
    {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
    },
    {
    	"name": "Kyrie Irving", 
    	"age":32, "position": "Point Guard", 
    	"team": "Brooklyn Nets"
    },
    {
    	"name": "Damian Lillard", 
    	"age":33, "position": "Point Guard", 
    	"team": "Portland Trailblazers"
    },
    {
    	"name": "Joel Embiid", 
    	"age":32, "position": "Power Foward", 
    	"team": "Philidelphia 76ers"
    },
    {
    	"name": "", 
    	"age":16, 
    	"position": "P", 
    	"team": "en"
    }
]




class Player:
    def __init__(self, my_dict):
        for key in my_dict:
            setattr(self, key, my_dict[key])
        # Player.team_list.append(self)

    @classmethod
    def get_team(cls, team_list):
        team_lst = []
        #iterate through the list
        for player in team_list:
            #build objects with the dictionaries
            team_lst.append(cls(player))
        return team_lst
            

# in order to use a value from a method, return it


print(Player.get_team(players)[0].name)

# print(players[0])

kevin = {
    "name": "Kevin Durant", 
    "age":34, 
    "position": "small forward", 
    "team": "Brooklyn Nets"
    }
jason = {
    "name": "Jason Tatum", 
    "age":24, 
    "position": "small forward", 
    "team": "Boston Celtics"
    }
kyrie = {
    "name": "Kyrie Irving", 
    "age":32, "position": "Point Guard", 
    "team": "Brooklyn Nets"
    }
    
# Create your Player instances here!
# player_jason = Player(jason)
# player_kevin = Player(kevin)
# player_kyrie = Player(kyrie)
# # print(player_jason.name)

# print(Player.team_list[2].name)




