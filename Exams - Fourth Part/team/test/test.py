from space.team import Team
import unittest

class TestTeam(unittest.TestCase):

    def test_correct_initialization(self):
        team = Team('team')
        self.assertEqual(team.name, 'team')
        self.assertEqual(team.members, {})

    def test_name(self):
        team = Team('team')
        with self.assertRaises(ValueError) as ex:
            team.name = 'team5'
        self.assertEqual(str(ex.exception), "Team Name can contain only letters!")

    def test_add_member(self):
        team = Team('team')
        team.members = {'a': 15, 'b': 18}
        name_age = {'c': 18, 'd': 17, 'a': 15}
        result = team.add_member(**name_age)
        self.assertEqual(team.members, {'a': 15, 'b': 18, 'c': 18, 'd': 17})
        self.assertEqual(result, "Successfully added: c, d")

        another_team = Team('team')
        another_team.members = {'a': 15, 'b': 18}
        other_name_age = {'a': 18, 'b': 17}
        other_result = another_team.add_member(**other_name_age)
        self.assertEqual(another_team.members, {'a': 15, 'b': 18})
        self.assertEqual(other_result, "Successfully added: ")

    def test_remove_member_if_name_exists(self):
        team = Team('team')
        name_age = {'a': 15, 'b': 18}
        team.add_member(**name_age)
        result = team.remove_member('a')
        self.assertEqual(team.members, {'b': 18})
        self.assertEqual(result, "Member a removed")

    def test_remove_member_if_name_doesnt_exist(self):
        team = Team('team')
        name_age = {'a': 15, 'b': 18}
        team.add_member(**name_age)
        result = team.remove_member('c')
        self.assertEqual(team.members, {'a': 15, 'b': 18})
        self.assertEqual(result, "Member with name c does not exist")

    def test_gt(self):
        team = Team('team')
        team.members = {'a': 15, 'b': 18}
        other = Team('team')
        other.members = {'a': 15, 'b': 18, 'c': 18}
        result = team > other
        self.assertEqual(result, False)

        team_second = Team('team')
        team_second.members = {'a': 15, 'b': 18}
        other_second = Team('team')
        other_second.members = {'a': 15}
        result_new = team_second > other_second
        self.assertEqual(result_new, True)

    def test_len(self):
        team = Team('team')
        team.members = {'a': 15, 'b': 18}
        result = len(team)
        self.assertEqual(result, 2)

    def test_add(self):
        team = Team('team')
        members = {'a': 15, 'b': 18}
        team.add_member(**members)
        other = Team('otherteam')
        other_members = {'c': 15, 'd': 18, 'e': 18}
        other.add_member(**other_members)
        new_team = team + other
        self.assertEqual(new_team.name, 'teamotherteam')
        self.assertEqual(new_team.members, {'a': 15, 'b': 18, 'c': 15, 'd': 18, 'e': 18})

    def test_string_representation(self):
        team = Team('team')
        team.members = {'a': 15, 'b': 18}
        result = str(team)
        self.assertEqual(result, 'Team name: team\nMember: b - 18-years old\nMember: a - 15-years old')


if __name__ == "__main__":
    unittest.main()











