"""
Look up a state in a dictionary and find the corresponding bool.
"""

import sys

states = {
    "Alabama":        True,
    "Alaska":         True,
    "Arizona":        True,
    "Arkansas":       True,
    "California":     False,
    "Colorado":       False,
    "Connecticut":    False,
    "Delaware":       False,
    "DC":             False,
    "Florida":        True,
    "Georgia":        True,
    "Hawaii":         False,
    "Idaho":          True,
    "Illinois":       False,
    "Indiana":        True,
    "Iowa":           True,
    "Kansas":         True,
    "Kentucky":       True,
    "Louisiana":      True,
    "Maine":          False,
    "Maryland":       False,
    "Massachusetts":  False,
    "Michigan":       True,
    "Minnesota":      True,
    "Mississippi":    True,
    "Missouri":       True,
    "Montana":        True,
    "Nebraska":       True,
    "Nevada":         False,
    "New Hampshire":  False,
    "New Jersey":     False,
    "New Mexico":     False,
    "New York":       False,
    "North Carolina": True,
    "North Dakota":   True,
    "Ohio":           True,
    "Oklahoma":       True,
    "Oregon":         False,
    "Pennsylvania":   True,
    "Rhode Island":   False,
    "South Carolina": True,
    "South Dakota":   True,
    "Tennessee":      True,
    "Texas":          True,
    "Utah":           True,
    "Vermont":        False,
    "Virginia":       False,
    "Washington":     False,
    "West Virginia":  True,
    "Wisconsin":      True,
    "Wyoming":        True
}

try:
    state = input("What state are you interested in? ")
except BaseException:
    sys.exit(1)

try:
    isRed = states[state]
except KeyError:
    print(f'Sorry, "{state}" is not a state.')
    sys.exit(1)

if isRed:
    print(f"{state} voted for Republican Donald Trump in 2016. Boo.")
else:
    print(f"{state} voted for Democrat Hilary Clinton in 2016. Yay")

sys.exit(0)
