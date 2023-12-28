import math

class Spec_game():
    def __init__(self,dict):
        self.game = dict['game']
        self.game_nb = dict['game_nb']
        self.p1 = dict['p1']
        self.p2 = dict['p2']
        self.p3 = dict['p3']
        self.p4 = dict['p4']
        self.round = dict['round']
        self.tot_points = self.retrieve_points_from_round()
        self.tot_bps = self.retrieve_bps_from_round()
        self.list_participants = [self.p1,self.p2,self.p3,self.p4]
        self.list_teams = self.construct_list_teams()

    def construct_list_teams(self):
        list_teams = []
        for p in self.list_participants:
            t = p.get_team()
            if t in set(list_teams):
                pass
            else:
                list_teams.append(t)

        assert len(list_teams) == 2, "List of teams should have length 2"
        return list_teams

    def get_tot_points(self):
        return self.tot_points

    def get_bc(self):

        bc_dict = {}
        tot_bp_per_team = self.calc_bc_per_team()
        dict_coef_per_team = self.get_coef_from_tot_bp(tot_bp_per_team)
        for p in self.list_participants:
            t = p.get_team()
            bc_dict[p] = dict_coef_per_team[t]

        return dict_coef_per_team,bc_dict

    def get_game_nb(self):
        return self.game_nb

    def retrieve_points_from_round(self):

        points_per_round = {
            1: 20,
            2: 20,
            3: 25,
            4: 25,
            5: 30,
            6: 30,
            7: 35,
            8: 40
        }

        if self.round <= 8:
            return points_per_round[self.round]
        else:
            return 40

    def retrieve_bps_from_round(self):

        bps_per_round = {
            1: 40,
            2: 40,
            3: 30,
            4: 25,
            5: 25,
            6: 25,
            7: 25,
            8: 25
        }

        if self.round <= 8:
            return bps_per_round[self.round]
        else:
            return 25

    def process_outcome(self,outcome_dict_points,outcome_dict_bps):

        self.outcome_points_input = outcome_dict_points
        self.outcome_bps_input = outcome_dict_bps

        assert set(outcome_dict_points.keys()) == set(self.list_participants), f"Outcome dict points list of keys {outcome_dict_points.keys()} does not correspond to list of participants {self.list_participants}"
        assert set(outcome_dict_bps.keys()) == set(self.list_participants), f"Outcome dict BPs list of keys {outcome_dict_bps.keys()} does not correspond to list of participants {self.list_participants}"

        outcome_dict_points_recalc = self.recaculaculate_points(outcome_dict_points)
        outcome_dict_bps_recalc = self.normalize_bps(outcome_dict_bps)

        self.outcome_points_recalc = outcome_dict_points_recalc
        self.outcome_bps_recalc = outcome_dict_bps

        for player in self.list_participants:
            player.add_points(outcome_dict_points_recalc[player],f"round {self.round}")
            player.add_bps(outcome_dict_bps_recalc[player],f"round {self.round}")

    def recaculaculate_points(self,dict):

        normalized_points = self.normalize_points(dict)
        recalc_bc = self.correct_boitcoef(normalized_points)

        return recalc_bc

    def normalize_points(self,dict):

        sum_points = sum(dict.values())
        norm_dict = {}

        for key in dict.keys():
            norm_dict[key] = round(self.tot_points * dict[key]/sum_points)

        return norm_dict

    def normalize_bps(self,dict):

        sum_points = sum(dict.values())
        norm_dict = {}

        for key in dict.keys():
            norm_dict[key] = round(self.tot_bps * dict[key]/sum_points)

        return norm_dict

    def correct_boitcoef(self,dict):

        dict_corrected_bc = {}

        bc_team,bc_player = self.get_bc()
        for p in dict.keys():
            dict_corrected_bc[p] = dict[p] * bc_player[p]

        return dict_corrected_bc

    def calc_bc_per_team(self):
        teams_bp = {}
        for p in self.list_participants:
            t = p.get_team()
            if t in set(teams_bp.keys()):
                teams_bp[t] += p.get_bps()
            else:
                teams_bp[t] = p.get_bps()

        return teams_bp

    def get_coef_from_tot_bp(self,tot_bp_dict):

        def coef_from_abs(abs):
            if abs < 10:
                return 1
            elif abs < 20:
                return 1.1
            elif abs < 30:
                return 1.2
            elif abs < 40:
                return 1.3
            elif abs < 50:
                return 1.4
            else:
                return 1.5

        dict_coef = {}
        diff = tot_bp_dict[self.list_teams[0]] - tot_bp_dict[self.list_teams[1]]
        sgn = math.copysign(1,diff)
        abs_diff = abs(diff)

        coef_abs = coef_from_abs(abs_diff)

        dict_coef[self.list_teams[0]] = max(sgn * coef_abs,1)
        dict_coef[self.list_teams[1]] = max(-sgn * coef_abs,1)

        return dict_coef