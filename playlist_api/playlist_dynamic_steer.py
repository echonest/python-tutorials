# Uncomment to set the API key explicitly. Otherwise Pyechonest will
# look in the ECHO_NEST_API_KEY environment variable for the key.
#from pyechonest import config
#config.ECHO_NEST_API_KEY='YOUR API KEY'

from pyechonest import playlist

prc = playlist.Playlist(type='artist-description', description=['style:progressive+rock', 'country'])

print 'First three songs for description: "%s" with no steering:' % (', '.join(prc.info['description']))
print '    "%s" by %s' % (prc.song.title, prc.song.artist_name)
for i in range(0,2):
    prc.get_next_song()
    print '    "%s" by %s' % (prc.song.title, prc.song.artist_name)

print '\nNext five songs, increasing tempo:'
for i in range(0,5):
    prc.get_next_song(steer='tempo^1.1')
    if prc.song.audio_summary:
        print '    "%s" by %s, tempo: %s' % (prc.song.title, prc.song.artist_name, prc.song.audio_summary['tempo'])

def get_frequency(dyn_playlist, term_name):
    for a_term in dyn_playlist.info['terms']:
        if a_term['name'] == term_name:
            return a_term['frequency']
    return None

print '\nCurrent playlist:'
print '    "country" frequency: %s' % (get_frequency(prc, 'country'),)
print '    "jazz" frequency: %s' % (get_frequency(prc, 'jazz'),)

print '\nGetting another song while removing "country," adding "mood:happy," and excluding "style:jazz"'
prc.get_next_song(steer_description=['country^0', 'mood:happy', '-style:jazz'])

print '\nUpdated playlist:'
print '    description: "%s"' % (', '.join(prc.info['description']),)
print '    "country" frequency: %s' % (get_frequency(prc, 'country'),)
print '    "jazz" frequency: %s' % (get_frequency(prc, 'jazz'),)

print '\nNext song:'
print '    "%s" by %s' % (prc.song.title, prc.song.artist_name)
