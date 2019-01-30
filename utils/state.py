class State:
    state = {}

    @staticmethod
    def init():
        State.state = {
            "lowres_frames": None,
            "highres_frames": None,
            "photopath": "",
            "frame": 0,
            "current_photo": None,
            "share_code": "",
            "preview_image_width": 0,
            "photo_countdown": 0,
            "reset_time": 0,
            "upload_url": "",
            "photo_url": "",
            "api_key": ""
        }
        return State.state

    @staticmethod
    def set(value):
        State.state[value[0]] = value[1]
        return State.state

    @staticmethod
    def set_dict(value):
        State.state = {**State.state, **value}
        return State.state

    @staticmethod
    def get(key):
        try:
            return State.state.get(key)
        except KeyError:
            print("No key found")
            return None

    @staticmethod
    def print():
        print(State.state)
