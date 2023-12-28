class Player():
    def __init__(self,name,team):
        self.name = name
        self.team = team
        self.points_dict = {}
        self.bps_dict = {}

    def get_name(self):
        return self.name

    def get_team(self):
        return self.team

    def get_points(self):
        return sum(self.points_dict.values())

    def get_bps(self):
        return sum(self.bps_dict.values())

    def get_points_dict(self):
        return self.points_dict

    def get_bps_dict(self):
        return self.bps_dict

    def add_points(self,points,key):
        if key in self.points_dict:
            raise ValueError("key already taken, not allowed to overwrite")
        else:
            self.points_dict[key] = points

    def add_bps(self,points,key):
        if key in self.bps_dict:
            raise ValueError("key already taken, not allowed to overwrite")
        else:
            self.bps_dict[key] = points

    def change_points(self,points,key):
        if key in self.points_dict:
            print(f"Changing points of key {key} from {self.points_dict[key]} to {points}")
            self.points_dict[key] = points
        else:
            raise ValueError("key not yet taken, impossible to overwrite")

    def change_bps(self,points,key):
        if key in self.bps_dict:
            print(f"Changing points of key {key} from {self.bps_dict[key]} to {points}")
            self.bps_dict[key] = points
        else:
            raise ValueError("key not yet taken, impossible to overwrite")




