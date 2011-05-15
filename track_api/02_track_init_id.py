# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import song, track

rof_results = song.search(title='Ring of Fire', artist='Johnny Cash', buckets=['id:7digital'], limit=True)

if rof_results:
    rof = rof_results[0]
    rof_tracks = rof.get_tracks('7digital')
    if rof_tracks:
        roft = track.track_from_id(rof_tracks[0]['id'])
        for attr in ['analysis_channels', 'analysis_sample_rate', 'analysis_url', 'artist', 'audio_md5', 'catalog', 'danceability', 'duration', 'end_of_fade_in', 'energy', 'foreign_id', 'foreign_release_id', 'id', 'key', 'key_confidence', 'loudness', 'md5', 'meta', 'mode', 'mode_confidence', 'num_samples', 'preview_url', 'release_image', 'sample_md5', 'song_id', 'start_of_fade_out', 'status', 'tempo', 'tempo_confidence', 'time_signature', 'time_signature_confidence', 'title']:
            print '%-30s %s' % (attr, getattr(roft, attr))
        print ''
        for dicts_attr in ['bars', 'beats', 'sections', 'segments', 'tatums']:
            print '"%s" example dict:' % (dicts_attr)
            for key, val in getattr(roft, dicts_attr)[0].iteritems():
                print '    %-26s %s' % (key, val)
            print ''
    else:
        print 'No tracks found.'
else:
    print 'No songs found.'
