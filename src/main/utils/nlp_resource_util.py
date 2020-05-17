import json
import pickle

from src.main.utils.config_util import SportsConfig


class NLPResourceUtil(SportsConfig):

    def __init__(self):
        self.sports_team_dict = self.set_team_dict(self.sports_reference_dir)
        self.sports_player_dict = self.set_player_dict(self.sports_reference_dir)
        self.individual_sports_dict = self.set_individual_sport_dict(self.sports_reference_dir)
        self.sports_terms_dict = self.set_sports_terms_dict(self.sports_reference_dir)
        self.sports_coach_dict = self.set_coach_dict(self.sports_reference_dir)
        self.sports_nickname_dict = self.set_nickname_dict(self.sports_reference_dir)

    def set_team_dict(self, file_path):
        """
        Set team dictionary for class
        """
        tmp_dict = {}
        for league in self.sports_leagues:
            # Dont have football team info (soccer)
            if league in self.sports_leagues_no_team_ref:
                pass
            else:
                tmp_dict[league] = self.read_json_file(file_path=file_path,
                                                       file_name=f"{league}_team_dict.json")
        return tmp_dict

    def set_player_dict(self, file_path):
        tmp_dict = {}
        for league in self.sports_leagues:
            # Dont have football (soccer) , ncaab, ncaafb player info
            if league in self.sports_leagues_no_player_ref:
                pass
            else:
                tmp_dict[league] = self.read_json_file(file_path=file_path,
                                                       file_name=f"{league}_player_dict.json")
        return tmp_dict

    def set_sports_terms_dict(self, file_path):
        tmp_dict = {}
        for sport in self.sports_with_references:
            tmp_dict[sport] = self.read_pickled_file(file_path=file_path,
                                                     file_name=f"{sport}_terms.data")
        return tmp_dict

    def set_nickname_dict(self, file_path):
        tmp_dict = {}
        for sport in self.sports_leagues_with_nickname_and_coaches:
            tmp_dict[sport] = self.read_json_file(file_path=file_path,
                                                  file_name=f"{sport}_nickname_dict.json")
        return tmp_dict

    def set_coach_dict(self, file_path):
        tmp_dict = {}
        for sport in self.sports_leagues_with_nickname_and_coaches:
            tmp_dict[sport] = self.read_json_file(file_path=file_path,
                                                  file_name=f"{sport}_coach_dict.json")
        return tmp_dict

    def set_individual_sport_dict(self, file_path):
        tmp_dict = {}
        for sport in self.individual_sports:
            tmp_dict[sport] = self.read_pickled_file(file_path=file_path, file_name=f"{sport}_athlete_set.data")
        return tmp_dict

    def read_json_file(self, file_path, file_name):
        # C:\Users\runni_000\PycharmProjects\podcastProject\resources\reference_dict\nba_team_dict.json
        with open(f'{file_path}/{file_name}') as json_file:
            # with open(f'../{file_name}') as json_file:
            return json.load(json_file)

    def read_pickled_file(self, file_path, file_name):
        with open(f'{file_path}/{file_name}', 'rb') as filehandle:
            # read the data as binary data stream
            return pickle.load(filehandle)

    def save_dict(self, dictionary, file_path, file_name):
        tmp_json = json.dumps(dictionary)
        with open(f'{file_path}/{file_name}', "w") as json_file:
            json_file.write(tmp_json)
            json_file.close()

    # TODO revisit these tests
    def save_to_existing_dict_tags(self, appended_dict: dict, file_path: str, file_name: str):
        """
        :param appended_dict:
        :param file_path: r"%s\data\tag_generation_pending_validation" % self.parent_dir,
        :param file_name: "tags.json"
        :return:
        """
        existing_dict: dict = self.read_json_file(file_path=file_path, file_name=file_name)
        existing_dict.update(appended_dict)
        self.save_dict(existing_dict, file_path, file_name)
        return

    def save_to_existing_dict_summary(self, summary_list: list, file_path: str, file_name: str):
        """
        :param summary_list:
        :param file_path: r"%s\data\tag_generation_pending_validation" % self.parent_dir,
        :param file_name: "summary_tag__pending_validation.json"
        :return:
        """
        existing_dict: dict = self.read_json_file(file_path=file_path, file_name=file_name)

        for index, summary in enumerate(summary_list):
            existing_dict["SummaryList"].append(summary)
        self.save_dict(existing_dict, file_path, file_name)
        return
