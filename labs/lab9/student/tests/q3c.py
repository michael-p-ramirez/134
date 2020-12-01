test = {   'name': 'q3c',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> \n'
                                               ">>> print('\\n'.join(aqi_table))\n"
                                               '"State"    "County"   "Year"  "Days with AQI"  "Good Days"  "Moderate Days"  "Unhealthy for Sensitive Groups Days"\n'
                                               '"Alabama"  "Baldwin"  2019    271              237          34               0\n'
                                               '"Alabama"  "Clay"     2019    107              97           10               0\n'
                                               '"Alabama"  "Colbert"  2019    263              252          11               0\n'
                                               '"Alabama"  "DeKalb"   2019    361              324          37               0\n',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> \n>>> len(aqi_table)\n5', 'hidden': False, 'locked': False},
                                   {   'code': '>>> \n>>> print(aqi_table[0])\n"State"    "County"   "Year"  "Days with AQI"  "Good Days"  "Moderate Days"  "Unhealthy for Sensitive Groups Days"\n',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': ">>> \n>>> len(','.join(aqi_table[1].split()).split(','))\n7", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
