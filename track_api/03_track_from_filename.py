# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import track

c_major = track.track_from_filename('c_major.mp3', filetype='mp3')

for attr in ['analysis_channels', 'analysis_sample_rate', 'analysis_url', 'artist', 'audio_md5', 'catalog', 'danceability', 'duration', 'end_of_fade_in', 'energy', 'foreign_id', 'foreign_release_id', 'id', 'key', 'key_confidence', 'loudness', 'md5', 'meta', 'mode', 'mode_confidence', 'num_samples', 'preview_url', 'release_image', 'sample_md5', 'song_id', 'start_of_fade_out', 'status', 'tempo', 'tempo_confidence', 'time_signature', 'time_signature_confidence', 'title']:
    if hasattr(c_major, attr):
        print '%-30s %s' % (attr, getattr(c_major, attr))
    else:
        print '%-30s *No such attribute*' % (attr,)

print ''

for dicts_attr in ['bars', 'beats', 'sections', 'segments', 'tatums']:
    print '"%s" example dict:' % (dicts_attr)
    if getattr(c_major, dicts_attr):
        for key, val in getattr(c_major, dicts_attr)[0].iteritems():
            print '    %-26s %s' % (key, val)
    print ''

print 'segment pitches:'
print ('%8s    ' + '%-4s ' * 12) % ('start', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
for a_dict in c_major.segments:
    print ('%8.2f    ' + '%4.2f ' * 12) % ((a_dict['start'], ) + tuple(a_dict['pitches']))
