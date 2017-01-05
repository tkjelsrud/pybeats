# pybeats

# All segments of music currently loaded
# collection = []

# Configuration is good
# but maybe better to land on a format for now, 8 micro steps pr beat? (32 steps)
# 
# doodle = Doodle()
# doodle.setTiming(4, 4)
# doodle.setMicroResolution(8) #Number of micro steps in beat

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

#
# BD 1 0 1 0
# SD 0 1 0 1
#