
class PlayerStats:
    def __init__(self):
        self.total_frames = 0
        self.smash_count = 0
        self.volley_count = 0
        self.lob_count = 0

    def update(self, shot_type):
        self.total_frames += 1
        if shot_type == "Smash":
            self.smash_count += 1
        elif shot_type == "Volley":
            self.volley_count += 1
        elif shot_type == "Lob":
            self.lob_count += 1

    def summary(self):
        return {
            "Smashes": self.smash_count,
            "Volleys": self.volley_count,
            "Lobs": self.lob_count,
            "Frames Analyzed": self.total_frames
        }
