# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import song, track

sth_results = song.search(title='Stairway to Heaven', artist='Led Zeppelin')
sth = sth_results[0]

sth_track = track._track_from_response(
    {'response': {
        'track': {
            'status': 'complete', 
            'id': 'StairwayID', 
            'audio_summary': sth.audio_summary 
        }
    }})

for attr in ['analysis_channels', 'analysis_sample_rate', 'analysis_url', 'artist', 'audio_md5', 'catalog', 'danceability', 'duration', 'end_of_fade_in', 'energy', 'foreign_id', 'foreign_release_id', 'id', 'key', 'key_confidence', 'loudness', 'md5', 'meta', 'mode', 'mode_confidence', 'num_samples', 'preview_url', 'release_image', 'sample_md5', 'song_id', 'start_of_fade_out', 'status', 'tempo', 'tempo_confidence', 'time_signature', 'time_signature_confidence', 'title']:
    if hasattr(sth_track, attr):
        print '%-30s %s' % (attr, getattr(sth_track, attr))
    else:
        print '%-30s *No such attribute*' % (attr,)

print ''

for dicts_attr in ['bars', 'beats', 'sections', 'segments', 'tatums']:
    print '"%s" example dict:' % (dicts_attr)
    if getattr(sth_track, dicts_attr):
        for key, val in getattr(sth_track, dicts_attr)[0].iteritems():
            print '    %-26s %s' % (key, val)
    print ''

print 'pitches for first 20 segments:'
print ('%8s    ' + '%-4s ' * 12) % ('start', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
for a_dict in sth_track.segments[0:20]:
    print ('%8.2f    ' + '%4.2f ' * 12) % ((a_dict['start'], ) + tuple(a_dict['pitches']))
