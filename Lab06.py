#1.
class Player:
    def __init__(self, firstname, lastname, team=None):
        self.first_name = firstname
        self.last_name = lastname
        self.team = team
        self.score = []
        
    def add_score(self, date, score):
        self.date = date
        self.score.append(score)
        print self.score

    def total_score(self):
        self.total = 0
        for i in range (len(self.score)):
            self.total = sum (self.score)
        print self.total
        
    def average_score(self):
        self.average = 0
        count = len(self.score)
        for i in range (len(self.score)):
            self.average = float(sum(self.score))/ float (count)
        print self.average
    
    


            
new_score = Player('Fernando','Torres',)
new_score.add_score ('2012/06/23',0)
new_score.add_score ('2012/06/24',0)
new_score.add_score ('2012/06/25',1)
new_score.add_score ('2012/06/26',0)
new_score.add_score ('2012/06/27',1)
new_score.total_score()
new_score.average_score()

#Part III
class Team:
    def __init__(self, name, league, manager_name, points):
        self.name = name
        self.league = league
        self.manger_name = manager_name
        self.player = []
        
    def add_player(self,player):
        self.player.append(player)
        print self.player
        
    def __str__(self):
        return "the name of the team is "+self.name
    
new_team_1 = Team('Portugal','English', 'Sir', 3)
new_team_2 = Team('Spain', 'Spanish', 'Him', 4)

spain = Team('spain','spanish','nana',0)
portugal = Team('portugal', 'english', 'ama', 3)
spain.add_player('Torres')
portugal.add_player('Ronaldo')

torres = Player('Fernando', 'Torres',spain)
ronaldo = Player('Christiano', 'Ronaldo', portugal)

print spain
print portugal
print torres.team


class Match:
    def __init__(self, home_team, away_team, date):
        self.home_team = home_team
        self.away_team = away_team
        self.date = date
        self.home_scores = {}
        self.away_scores = {}
        
    def home_score(self):
        return sum(self.home_scores.values())
        

    def away_score(self):
        return sum(self.away_scores.values())

    def winner(self):
        if self.home_score() > self.away_score():
            print 'winner ', 
            return self.home_team.name
        if self.home_score() < self.away_score():
            print 'winner ', 
            return self.away_team.name
        if self.home_score() == self.away_score():
            return 'draw'

    def add_score(self, player, score):
        the_team = player.team
        if the_team == self.home_team:
            if player.last_name in self.home_scores:
                self.home_scores[player.last_name] += score
            else:
                self.home_scores[player.last_name] = score
                
        if the_team == self.away_team:
            if player.last_name in self.away_scores:
                self.away_scores[player.last_name] += score
            else:
                self.away_scores[player.last_name] = score

euro_semi_final = Match(spain, portugal, '2012/06/27')
euro_semi_final.add_score(torres,1)
euro_semi_final.add_score(ronaldo,2)
euro_semi_final.add_score(torres,1)
print euro_semi_final.winner()
 
 
 
            
        
