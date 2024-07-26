from typing import List, Dict

"""
Hi there! Here is a quick example.

    TRANSPILE: List[Dict[str, str]] = [
        {
            'filename': 'default',  # if default, a UUID will be used.
            '#ffea4a': '#321623',   # Void: Yellow
            '#320a46': '#283405',   # Darkest: Dark-Purple
            '#551937': '#3c6e14',   # Darker: Brown-Purple
            '#a01982': '#6aa805',   # Dark: Purple
            '#c80078': '#00c514',   # Light: Pink
            '#ff50bf': '#4bf05a',   # Lighter: Light-Pink
            '#ff6ac5': '#7dff73',   # Lightest: Extreme-Pink
        },
    ]

In this example, when compile.py is started, one new image will be created in the output folder.
Because there is one object,.

The filename can be manually set for each record. If the value is set to 'default', a unique indentifier will be used instead.

Lets take the second key/value pair.
'#ffea4a': '#321623',  # Void: Yellow

Which basically means
Change all pixels that are #ffea4a (Yellow) to #ff0000 (Red).

One additional sidenote. Transparancy is supported and can be utilized only as value.
'#ffea4a': 'transparent', 
"""

TRANSPILE: List[Dict[str, str]] = [
    {
        'filename': 'inStone',  # if default, a UUID will be used.
        '#ffea4a': '#321623',   # Void: Yellow
        '#320a46': '#283405',   # Darkest: Dark-Purple
        '#551937': '#3c6e14',   # Darker: Brown-Purple
        '#a01982': '#6aa805',   # Dark: Purple
        '#c80078': '#00c514',   # Light: Pink
        '#ff50bf': '#4bf05a',   # Lighter: Light-Pink
        '#ff6ac5': '#7dff73',   # Lightest: Extreme-Pink
    },
]
