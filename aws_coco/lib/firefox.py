import urllib

# https://github.com/mozilla/multi-account-containers/blob/00a1ce9dca2c4f54c9622515a7a86b56442eb9f2/src/js/popup.js#L1302
colors = ["blue", "turquoise", "green", "yellow", "orange", "red", "pink", "purple"]

# https://github.com/mozilla/multi-account-containers/blob/00a1ce9dca2c4f54c9622515a7a86b56442eb9f2/src/js/popup.js#L1316
icons = [
    "fingerprint",
    "briefcase",
    "dollar",
    "cart",
    "vacation",
    "gift",
    "food",
    "fruit",
    "pet",
    "tree",
    "chill",
    "circle",
    "fence",
]


def format_for_container(url, name, color, icon):
    return f"ext+container:name={name}&color={color}&icon={icon}&url={urllib.parse.quote_plus(url)}"
