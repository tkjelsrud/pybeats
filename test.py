# pybeats

# All segments of music currently loaded
# collection = []

# Configuration is good
# but maybe better to land on a format for now, 8 micro steps pr beat? (32 steps)
# 
# doodle = Doodle()
# doodle.setTempo(118)
# doodle.setTiming(4, 4)
# doodle.setMicroRes(8) #Number of micro steps in beat

## A track, instruments/voice within the composition
# t1 = Track("BD")
# t2 = Track("SD")
# doodle.addTracks([t1, t2])

# A segment of "music" (several bars, usually 4, 8, 16)
# phrase = Phrase()

## A section of music (a measure, divided in beats)
# bar = Bar()

# NotePainter
# np.setTemplate("BD", "101?") # first and third beat
# np.setTemplate("SD", "0???") # nothing on the first step
# np.swing("sine", "0101", 0.5, doodle.getMicroRes()) # Factor of swing, guide, amount and speed (size of cycle)
# # Some ideas
# Destinations: timing (default), velocity, duration, repeating
# Type of modifiers: sine (bipolar), pos sine (just the positive values), abssine, tri, random
#
# Don't try everything at once - the modifier is all that needs to be rated, the note grid/template can be static!
#
# np.randomize()
# np.drawInBar(bar)

# Next steps...
#   Play the bar (test it)
#   Rate the bar (1, 0, -1)
#   (Repeat)
#
# Analyse...
#   What positions are rated +1
#   What positions are rated -1
#   What swing guides are rated +1 or -1

#
## Separate thread responsisble for
# Start playback
# Suspend playback
# While playback
#   using timing, play notes
#   mido.Message('note_on', note=100, velocity=3, time=6.2)
#