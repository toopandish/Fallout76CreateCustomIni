""" This module creates a fallout76Custom.ini file from the installed mods in the data directory """

import os
from os import walk

# Configuration arrays, these are mods that should go in specific
# lists, all other go in sResourceArchive2List
RESOURCE_MAP = [
    {
        'filename': 'sResourceStartUpArchiveList',
        'mods': [
            'IconTag.ba2',
            'IconSortingRatmonkeys.ba2',
            'MMM - Country Roads.ba2',
            ],
        'default_mods': [
            'SeventySix - Interface.ba2',
            'SeventySix - Localization.ba2',
            'SeventySix - Shaders.ba2',
            'SeventySix - Startup.ba2'
            ],
        'found_mods': []
    },
    {
        'filename': 'sResourceArchiveList2',
        'mods': [
            'ShowHealth.ba2',
            'MoreWhereThatCameFrom.ba2',
            'Prismatic_Lasers_76_Lightblue.ba2',
            'OptimizedSonar.ba2',
            'Silentchameleon.ba2',
            'CleanPip.ba2',
            'classicFOmus_76.ba2',
            'nootnoot.ba2',
            'MenuMusicReplacer.ba2',
            'BullBarrel.ba2'
            ],
        'default_mods': [
            'SeventySix - Animations.ba2',
            'SeventySix - EnlightenInteriors.ba2',
            'SeventySix - GeneratedTextures.ba2',
            'SeventySix - EnlightenExteriors01.ba2',
            'SeventySix - EnlightenExteriors02.ba2'
            ],
        'found_mods': []
    },
    {
        'filename': 'sResourceIndexFileList',
        'mods': [
            'UHDmap.ba2',
            'EnhancedBlood - Textures.ba2',
            'EnhancedBlood - Meshes.ba2',
            'MapMarkers.ba2',
            'Radiant_Clouds.ba2',
            'SpoilerFreeMap.ba2',
            ],
        'default_mods': [
            'SeventySix - Textures01.ba2',
            'SeventySix - Textures02.ba2',
            'SeventySix - Textures03.ba2',
            'SeventySix - Textures04.ba2',
            'SeventySix - Textures05.ba2',
            'SeventySix - Textures06.ba2'
            ],
        'found_mods': []
    },
    {
        'filename': 'sResourceArchive2List',
        'mods': [],
        'default_mods': [
            'SeventySix - ATX_Main.ba2',
            'SeventySix - ATX_Textures.ba2'
            ],
        'found_mods': []
    },
]
#The array index from the RESOURCE_MAP for sResourceArchive2List
SR_2LIST_INDEX = 3

# Get the home directory of the current user
HOME_DIR = os.path.expanduser("~") + "\\Documents\\My Games\\Fallout 76\\fallout76Custom.ini"

# Open the Custom.ini file for writing
CUSTOM_INI_FILE = open(HOME_DIR, "w+")

# write the section header to the file
CUSTOM_INI_FILE.write("[Archive]\r\n")

# Loop through the resource map and add mods to the correct places
for (dirpath, dirnames, filenames) in walk('data'):
    for file in filenames:
        # Make sure the file is not an official file (starts with "SeventySix")
        # and is a ba2 (file extension)
        if (file[0:10] != 'SeventySix' and file[-4:] == '.ba2'):
            FOUND = False
            for RESOURCE in RESOURCE_MAP:
                if file in RESOURCE['mods']:
                    RESOURCE['found_mods'].append(file)
                    FOUND = True

            # If a mod doesn't appear in the one of the other mod lists, add it to the default
            if not FOUND:
                RESOURCE_MAP[SR_2LIST_INDEX]['found_mods'].append(file)
    break

# Loop through the resource map and add the correct lines to the ini file
for RESOURCE in RESOURCE_MAP:
    if RESOURCE['found_mods']:
        CUSTOM_INI_FILE.write(
            RESOURCE['filename'] + " = %s\r\n"
            % ', '.join(RESOURCE['default_mods'] + RESOURCE['found_mods'])
        )

CUSTOM_INI_FILE.close()
