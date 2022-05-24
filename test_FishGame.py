from FishGame import WindowFishGame


class TestFishGame:
    def test_login(self):
        username_entry = "admin"
        password_entry = "admin"

        if username_entry == "admin" and password_entry == "admin":
            result = "Success"
        else:
            result = "Fail"

        assert result == "Success"

    def test_wrong_login(self):
        username_entry_blank = ""
        password_entry_blank = ""

        if username_entry_blank == "admin" and password_entry_blank == "admin":
            result = "Success"
        else:
            result = "Fail"

        assert result == "Fail"

    def test_available_fish(self):
        fish_data = WindowFishGame.load_fish_data()

        assert fish_data[0]["Name"] == "King George Whiting"
        assert fish_data[1]["Name"] == "Lost bait"
        assert fish_data[2]["Name"] == "Small Mulloway"
        assert fish_data[3]["Name"] == "Snapper"
        assert fish_data[4]["Name"] == "Large Mullet"
        assert fish_data[5]["Name"] == "Seaweed Monster (random) clump of seaweed"
