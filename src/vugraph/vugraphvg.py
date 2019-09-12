
"""
Provides a description of what the Vugraph contains. For example:

WBF Youth World Online Team Championships,Final 4/4,I,1,14,USA,0,France,0
"""


class VugraphVG(object):
    def __init__(self,
                 description,
                 note,
                 round_type,
                 start_deal,
                 end_deal,
                 team1,
                 team1_points,
                 team2,
                 team2_points):
        self.description = description
        self.note = note
        self.round_type = round_type
        self.start_deal = start_deal
        self.end_deal = end_deal
        self.team1 = team1
        self.team1_points = team1_points
        self.team2 = team2
        self.team2_points = team2_points

    @staticmethod
    def parse(vg):
        parts = vg.split(',')
        description = parts[0]
        note = parts[1]
        if parts[2] != 'I':
            raise Exception('Unrecognized type value: ' + parts[2])
        round_type = parts[2]  # TODO: what is this?
        start_deal = int(parts[3])
        end_deal = int(parts[4])
        team1 = parts[5]
        team1_points = int(parts[6])  # TODO: are these points?
        team2 = parts[7]
        team2_points = int(parts[8])
        return VugraphVG(description, note, round_type, start_deal, end_deal, team1, team1_points, team2, team2_points)
