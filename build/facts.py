"""Level metadata + sourced facts. Every factual string carries source ids (see SOURCES)."""

SOURCES = {
    1: dict(t="Congressional Research Service, Admission of States to the Union: A Historical Reference Guide (R47747, updated Jan. 6, 2026)",
            u="https://www.everycrsreport.com/files/2026-01-06_R47747_3953c5c92f2090c240242b5d4ddff8c6863ca1cd.html"),
    2: dict(t="Ballotpedia, Original thirteen states (year each colony was settled)", u="https://ballotpedia.org/Original_thirteen_states"),
    3: dict(t="National Archives, Treaty of Guadalupe Hidalgo (1848)", u="https://www.archives.gov/milestone-documents/treaty-of-guadalupe-hidalgo"),
    4: dict(t="National Archives, Louisiana Purchase Treaty (1803)", u="https://www.archives.gov/milestone-documents/louisiana-purchase-treaty"),
    5: dict(t="National Archives, American Originals: Louisiana Purchase Treaty, 1803 (828,000 square miles)",
            u="https://www.archives.gov/exhibits/american_originals_iv/sections/text_purchase_treaty.html"),
    6: dict(t="National Park Service, Louisiana Territory Officially Transferred (Dec. 20, 1803)",
            u="https://www.nps.gov/articles/000/louisiana-territory-officially-transferred.htm"),
    7: dict(t="U.S. Department of State, Office of the Historian, Louisiana Purchase, 1803 (archived copy; $15 million)",
            u="https://webarchive.library.unt.edu/web/20130220125104/http://history.state.gov/milestones/1801-1829/LouisianaPurchase"),
    8: dict(t="Encyclopedia.com, Thirteen Colonies (founded between 1607 and 1732)",
            u="https://www.encyclopedia.com/history/united-states-and-canada/us-history/thirteen-colonies"),
    9: dict(t="USGS National Atlas, Territorial Acquisitions of the United States (archived copy)",
            u="https://webarchive.library.unt.edu/web/20140922205843/http:/nationalatlas.gov/articles/history/a_expansion.html"),
    10: dict(t="Map boundaries: Michael Porath, us-history-maps (GeoJSON, 2012). Files used: 1789030, 1803040, 1848080, 1912080",
             u="https://github.com/poezn/us-history-maps"),
}

# state: (order, date string, year)  -- all from source 1
ADMIT = {
 'Delaware': (1, 'December 7, 1787'), 'Pennsylvania': (2, 'December 12, 1787'), 'New Jersey': (3, 'December 18, 1787'),
 'Georgia': (4, 'January 2, 1788'), 'Connecticut': (5, 'January 9, 1788'), 'Massachusetts': (6, 'February 6, 1788'),
 'Maryland': (7, 'April 28, 1788'), 'South Carolina': (8, 'May 23, 1788'), 'New Hampshire': (9, 'June 21, 1788'),
 'Virginia': (10, 'June 25, 1788'), 'New York': (11, 'July 26, 1788'), 'North Carolina': (12, 'November 21, 1789'),
 'Rhode Island': (13, 'May 29, 1790'), 'Vermont': (14, 'March 4, 1791'), 'Kentucky': (15, 'June 1, 1792'),
 'Tennessee': (16, 'June 1, 1796'), 'Ohio': (17, 'March 1, 1803'), 'Louisiana': (18, 'April 30, 1812'),
 'Indiana': (19, 'December 11, 1816'), 'Mississippi': (20, 'December 10, 1817'), 'Illinois': (21, 'December 3, 1818'),
 'Alabama': (22, 'December 14, 1819'), 'Maine': (23, 'March 15, 1820'), 'Missouri': (24, 'August 10, 1821'),
 'Arkansas': (25, 'June 15, 1836'), 'Michigan': (26, 'January 26, 1837'), 'Florida': (27, 'March 3, 1845'),
 'Texas': (28, 'December 29, 1845'), 'Iowa': (29, 'December 28, 1846'), 'Wisconsin': (30, 'May 29, 1848'),
 'California': (31, 'September 9, 1850'), 'Minnesota': (32, 'May 11, 1858'), 'Oregon': (33, 'February 14, 1859'),
 'Kansas': (34, 'January 29, 1861'), 'West Virginia': (35, 'June 20, 1863'), 'Nevada': (36, 'October 31, 1864'),
 'Nebraska': (37, 'March 1, 1867'), 'Colorado': (38, 'August 1, 1876'), 'North Dakota': (39, 'November 2, 1889'),
 'South Dakota': (40, 'November 2, 1889'), 'Montana': (41, 'November 8, 1889'), 'Washington': (42, 'November 11, 1889'),
 'Idaho': (43, 'July 3, 1890'), 'Wyoming': (44, 'July 10, 1890'), 'Utah': (45, 'January 4, 1896'),
 'Oklahoma': (46, 'November 16, 1907'), 'New Mexico': (47, 'January 6, 1912'), 'Arizona': (48, 'February 14, 1912'),
}
SETTLED = {'Connecticut': 1633, 'Delaware': 1631, 'Georgia': 1732, 'Maryland': 1634, 'Massachusetts': 1620,
           'New Hampshire': 1623, 'New Jersey': 1660, 'New York': 1624, 'North Carolina': 1663, 'Pennsylvania': 1682,
           'Rhode Island': 1636, 'South Carolina': 1670, 'Virginia': 1607}  # source 2
NO_TERR = {'Kentucky', 'Maine', 'Texas', 'West Virginia'}  # source 1 notes: "joined without a territorial government"

RENAME = {
    'Mexican Cession (Unorganized territory)': 'Mexican Cession',
    'Unorganized Territory': 'Unorganized Territory',
    'Unorganized territory': 'Unorganized Territory',
    'Disputed between Massachusetts and Colony of New Brunswick': 'Disputed land',
    'Disputed between United States and West Florida': 'Disputed land',
    "Disputed between Northwest Territory and Rupert's Land": 'Disputed land',
    'D.C.': 'D.C.',
}

ABBR = {'Alabama': 'AL', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA', 'Colorado': 'CO', 'Connecticut': 'CT',
        'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA',
        'Kansas': 'KS', 'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
        'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT', 'Nebraska': 'NE',
        'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM', 'New York': 'NY',
        'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK', 'Oregon': 'OR', 'Pennsylvania': 'PA',
        'Rhode Island': 'RI', 'South Carolina': 'SC', 'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT',
        'Vermont': 'VT', 'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY',
        'Wisconsin ': 'WI'}

TERR_FACTS = {
    'Louisiana Purchase': ("Treaty signed April 30, 1803. The U.S. paid $15 million for about 828,000 square miles west of the "
                           "Mississippi River. France formally handed the territory over on December 20, 1803.", [5, 7, 6]),
    'Mississippi Territory': ("A U.S. territory in 1803, not yet a state. The map data shows it as its own territory.", [10]),
    'Indiana Territory': ("A U.S. territory in 1803, not yet a state. The map data shows it as its own territory.", [10]),
    'Unorganized Territory': ("Land the map data shows as not yet organized into a state or territory at this date.", [10]),
    'Mexican Cession': ("The Treaty of Guadalupe Hidalgo (signed February 2, 1848) annexed more than 525,000 square miles. Mexico "
                        "ceded 55 percent of its territory and the U.S. paid $15 million. The land covers present-day California, "
                        "Nevada, Utah, New Mexico, most of Arizona and Colorado, and parts of Oklahoma, Kansas and Wyoming.", [3]),
    'Oregon Territory': ("American title to the Oregon country was established in 1846. The map data shows it organized as "
                         "Oregon Territory by August 1848.", [9, 10]),
}

LEVELS_META = [
    dict(id='colonies', tag='1789', title='The Thirteen',
         intro='Start where it started: the Atlantic seaboard. Each tile is one of the original thirteen, using the borders the map data shows in 1789.',
         notes=[("British colonies on this coast were founded between 1607 (Virginia) and 1732 (Georgia).", [8]),
                ("The 1789 borders reach farther west than today's. Some states held land that later became other states, so a few shapes will look unfamiliar. The grey pieces were not part of any of the thirteen.", [10])]),
    dict(id='louisiana', tag='1803', title='Louisiana Purchase',
         intro='Four more states have joined, and the Mississippi River is no longer the western edge. The huge tile west of it is new.',
         notes=[("On April 30, 1803 the U.S. agreed to buy Louisiana from France for $15 million, about 828,000 square miles.", [5, 7]),
                ("Ohio became the 17th state on March 1, 1803, after Vermont (1791), Kentucky (1792) and Tennessee (1796).", [1])]),
    dict(id='mexican', tag='1848', title='The Mexican Cession',
         intro='Texas, Florida and a ring of new states fill the middle. Now the country reaches the Pacific.',
         notes=[("The Treaty of Guadalupe Hidalgo (February 2, 1848) annexed more than 525,000 square miles and extended the U.S. to the Pacific.", [3]),
                ("Wisconsin was admitted on May 29, 1848 as the 30th state.", [1])]),
    dict(id='today', tag='1912', title='The Lower 48',
         intro='Forty-eight tiles, one map. These are the borders the contiguous states had after Arizona joined in 1912.',
         notes=[("The 1853 Gadsden Purchase bought land from Mexico for $10 million.", [9]),
                ("The Gadsden Purchase solidified the present-day borders of the contiguous United States.", [4]),
                ("New Mexico (January 6, 1912) and Arizona (February 14, 1912) were the 47th and 48th states.", [1])]),
]


def fact_for(name):
    """Return (text, srcs, year or None) for a display name."""
    if name in TERR_FACTS:
        t, s = TERR_FACTS[name]
        return t, s, None
    if name in ADMIT:
        n, d = ADMIT[name]
        year = int(d[-4:])
        srcs = [1]
        txt = ''
        if name in SETTLED:
            extra = ''
            if name == 'Virginia':
                extra = ', the first of the thirteen colonies'
            if name == 'Georgia':
                extra = ', the last of the thirteen colonies'
            txt = f"Settled {SETTLED[name]}{extra}. Joined the Union {d} as state #{n}."
            srcs = [2, 1] + ([8] if extra else [])
        else:
            txt = f"Admitted {d} as state #{n}."
        if name in NO_TERR:
            txt += " It joined without first being a territory."
        if name == 'Arizona':
            txt += " It was the last of the lower 48 to join."
        return txt, srcs, year
    return None, [], None
