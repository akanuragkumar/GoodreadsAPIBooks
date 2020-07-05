class InvalidGoodreadsURL(Exception):
    pass


class MissingArguementError(Exception):
    pass


class MissingAPIKey(Exception):
    pass


errors = {
    "InvalidGoodreadsURL": {
        "message": "InvalidGoodreadsURL"
    },

    "MissingArguementError": {
        "message": "Arguement missing in command"
    },

    "MissingAPIKey": {
        "message": "Missing API key in env variable"
    }
}
