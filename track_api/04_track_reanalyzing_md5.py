# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import track

c_major_file = track.track_from_filename('c_major.mp3', filetype='mp3')
c_major_md5 = track.track_from_md5(c_major_file.md5)
c_major_ra_md5 = track.track_from_reanalyzing_md5(c_major_file.md5)

for c_major in (c_major_md5, c_major_ra_md5):
    print 'track ID: %s' % c_major.id
    print 'segment pitches:'
    print ('%8s    ' + '%-4s ' * 12) % ('start', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
    for a_dict in c_major.segments:
        print ('%8.2f    ' + '%4.2f ' * 12) % ((a_dict['start'], ) + tuple(a_dict['pitches']))
    print ''

