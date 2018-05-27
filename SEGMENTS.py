#This script contains the level segment objects for level generation.
import SETTINGS

class Segment:

    def __init__(self, stats):
        self.stats = stats
        self.ID = stats['id']
        self.array = stats['array']
        self.width = len(self.array[0])
        self.height = len(self.array)
        self.doors = stats['doors']
        self.items = stats['items']
        self.npcs = stats['npcs']
        self.type = stats['type']
        self.level_pos = None
        if 'player_pos' in stats:
            self.player_pos = stats['player_pos']
        else:
            self.player_pos = None
    



SETTINGS.segments_list.append(Segment({
        'items' : [((2, 1), 2), ((7, 1), 1)],
        'array' : [[0, 5, 5, 5, 3, 1, 2, 1, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 8, 1, 1, 1, 8, 0, 1],
                   [0, 0, 0, 1, 0, 0, 0, 0, 1],
                   [1, 1, 1, 1, 0, 0, 0, 7, 1],
                   [0, 0, 0, 1, 10, 1, 1, 1, 0],
                   [0, 0, 0, 1, 0, 1, 0, 0, 0],
                   [0, 0, 0, 1, 0, 1, 0, 0, 0]],
        'doors' : [270, 180],
        'npcs' : [],
        'id' : 0,
        'type' : 'normal',
        }))

SETTINGS.segments_list.append(Segment({
        'items' : [((5, 2), 8), ((3, 6), 0)],
        'array' : [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 0, 5, 0, 5, 0, 1, 0],
                   [1, 7, 5, 0, 5, 0, 5, 0, 1],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [0, 0, 8, 0, 6, 0, 8, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 0, 5, 0, 5, 0, 5, 0, 1],
                   [0, 1, 0, 5, 0, 5, 0, 1, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]],
        'doors' : [360, 180],
        'npcs' : [((7, 6), 90, 1)],
        'id' : 1,
        'type' : 'normal',
        }))

SETTINGS.segments_list.append(Segment({
        'items' : [((6, 2), 6)],
        'array' : [[0, 0, 1, 1, 0, 1, 1, 1, 0],
                   [0, 0, 1, 0, 0, 0, 0, 5, 0],
                   [0, 0, 1, 0, 8, 0, 0, 5, 0],
                   [1, 1, 1, 1, 10, 1, 1, 1, 1],
                   [8, 0, 9, 0, 0, 0, 0, 0, 1],
                   [1, 1, 1, 6, 7, 6, 0, 0, 3],
                   [0, 0, 2, 0, 8, 0, 0, 0, 1],
                   [0, 0, 1, 0, 0, 0, 0, 0, 1],
                   [0, 0, 1, 1, 0, 1, 1, 1, 1]],
        'doors' : [270, 90, 180],
        'npcs' : [((7, 7), 180, 2)],
        'id' : 2,
        'type' : 'normal',
        }))

SETTINGS.segments_list.append(Segment({
        'items' : [((1, 1), 2), ((2, 1), 5)],
        'array' : [[1, 5, 5, 1, 3, 1, 5, 5, 1],
                   [1, 0, 0, 0, 0, 0, 0, 0, 1],
                   [5, 0, 6, 0, 8, 0, 6, 0, 5],
                   [1, 0, 0, 0, 0, 0, 0, 0, 1],
                   [1, 1, 1, 1, 1, 10, 1, 1, 1],
                   [0, 0, 1, 7, 0, 0, 0, 1, 0],
                   [0, 0, 1, 0, 8, 0, 0, 2, 0],
                   [0, 0, 1, 0, 0, 0, 0, 1, 0],
                   [0, 0, 1, 1, 0, 1, 1, 1, 0]],
        'doors' : [270],
        'npcs' : [],
        'id' : 3,
        'type' : 'normal',
        }))

SETTINGS.segments_list.append(Segment({
        'items' : [],
        'array' : [[0, 0, 0, 0, 1, 1, 1, 1, 0],
                   [0, 1, 3, 1, 7, 0, 0, 5, 0],
                   [1, 0, 0, 0, 1, 0, 0, 5, 0],
                   [1, 0, 0, 0, 1, 0, 0, 1, 1],
                   [8, 0, 6, 0, 9, 0, 0, 8, 0],
                   [1, 0, 0, 0, 1, 0, 0, 1, 1],
                   [1, 0, 0, 0, 1, 0, 0, 1, 0],
                   [0, 1, 2, 1, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1, 1, 1, 1, 0]],
        'doors' : [360, 180],
        'id' : 4,
        'npcs' : [],
        'type' : 'normal',
        }))

SETTINGS.segments_list.append(Segment({
        'items' : [((1, 1), 1), ((7, 5), 2)],
        'array' : [[0, 1, 1, 0, 0, 0, 0, 0, 0],
                   [1, 0, 0, 1, 0, 0, 0, 0, 0],
                   [3, 0, 8, 1, 0, 0, 0, 0, 0],
                   [1, 0, 0, 1, 5, 5, 5, 5, 0],
                   [1, 0, 0, 9, 0, 0, 0, 7, 1],
                   [0, 1, 1, 1, 0, 0, 0, 0, 1],
                   [0, 0, 0, 1, 10, 1, 1, 1, 0],
                   [0, 0, 1, 0, 0, 0, 2, 0, 0],
                   [0, 0, 1, 0, 8, 0, 1, 0, 0]],
        'doors' : [270],
        'id' : 5,
        'npcs' : [((1, 4), 0, 3)],
        'type' : 'normal',
        }))

SETTINGS.segments_list.append(Segment({
        'items' : [((5, 6), 0), ((1, 7), 3)],
        'array' : [[0, 0, 1, 0, 0, 0, 1, 0, 0],
                   [0, 0, 1, 0, 6, 0, 1, 0, 0],
                   [0, 0, 1, 0, 0, 0, 1, 0, 0],
                   [1, 1, 1, 0, 0, 0, 1, 1, 1],
                   [0, 0, 1, 1, 10, 1, 0, 0, 0],
                   [1, 0, 1, 0, 0, 0, 0, 0, 1],
                   [1, 0, 9, 0, 0, 8, 0, 0, 1],
                   [1, 0, 1, 0, 0, 0, 0, 7, 1],
                   [0, 1, 1, 1, 1, 1, 1, 1, 0]],
        'doors' : [360, 180, 90],
        'id' : 6,
        'npcs' : [],
        'type' : 'normal',
        }))

SETTINGS.segments_list.append(Segment({
        'items' : [((1, 2), 2), ((2, 2), 3), ((5, 4), 5)],
        'array' : [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 1, 0, 5, 5, 5, 0, 0],
                   [1, 0, 0, 1, 6, 0, 6, 1, 0],
                   [1, 0, 0, 9, 0, 0, 0, 1, 1],
                   [1, 7, 0, 1, 0, 8, 0, 9, 0],
                   [0, 1, 1, 1, 0, 0, 0, 1, 1],
                   [0, 0, 0, 1, 6, 0, 6, 1, 0],
                   [0, 0, 0, 0, 5, 5, 5, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0]],
        'doors' : [360],
        'id' : 7,
        'npcs' : [((1, 3), 0, 0)],
        'type' : 'normal',
        }))

SETTINGS.segments_list.append(Segment({
        'items' : [((5, 4), 1)],
        'array' : [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 4, 0, 0, 0, 0],
                   [0, 0, 0, 1, 0, 1, 0, 0, 0],
                   [0, 0, 1, 1, 10, 1, 1, 0, 0],
                   [0, 1, 0, 0, 0, 0, 0, 1, 0],
                   [0, 3, 0, 0, 8, 0, 0, 2, 0],
                   [0, 1, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 2, 1, 0, 1, 1, 0, 0],
                   [0, 0, 0, 1, 0, 1, 0, 0, 0]],
        'doors' : [270],
        'id' : 8,
        'npcs' : [],
        'type' : 'end',
        }))

SETTINGS.segments_list.append(Segment({
        'items' : [((1, 3), 3), ((1, 4), 7)],
        'array' : [[0, 0, 0, 1, 0, 1, 1, 1, 0],
                   [0, 0, 1, 0, 0, 0, 0, 0, 1],
                   [0, 1, 1, 7, 0, 0, 8, 0, 1],
                   [5, 0, 1, 1, 1, 1, 0, 0, 1],
                   [5, 0, 0, 0, 0, 9, 0, 0, 1],
                   [5, 0, 1, 1, 1, 1, 0, 0, 1],
                   [0, 1, 2, 0, 0, 0, 8, 0, 3],
                   [0, 0, 1, 0, 0, 0, 0, 0, 1],
                   [0, 0, 0, 1, 0, 1, 1, 1, 0]],
        'doors' : [270, 90],
        'id' : 9,
        'npcs' : [((1, 5), 90, 0)],
        'type' : 'normal',
        }))

SETTINGS.segments_list.append(Segment({
        'items' : [((4, 2), 1), ((6, 2), 8), ((1, 5), 2), ((6, 5), 0)],
        'array' : [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 1, 1, 1, 1, 1, 1, 0],
                   [1, 7, 0, 1, 0, 1, 0, 0, 1],
                   [1, 0, 0, 9, 0, 9, 0, 0, 1],
                   [0, 1, 1, 1, 0, 1, 1, 1, 0],
                   [1, 0, 0, 1, 8, 1, 0, 7, 1],
                   [1, 6, 0, 9, 0, 9, 0, 0, 1],
                   [0, 1, 1, 1, 0, 1, 1, 1, 0],
                   [0, 0, 0, 1, 0, 1, 0, 0, 0]],
        'doors' : [270],
        'id' : 10,
        'npcs' : [],
        'type' : 'start',
        'player_pos' : [2,3],
        }))

SETTINGS.segments_list.append(Segment({
        'doors' : [],
        'items' : [],
        'array' : [[1, 1, 1, 1, 1, 1, 1, 1, 1],
                   [1, 3, 0, 0, 0, 0, 0, 3, 1],
                   [1, 0, 3, 0, 0, 0, 3, 0, 1],
                   [1, 0, 0, 3, 0, 3, 0, 0, 1],
                   [1, 0, 0, 0, 3, 0, 0, 0, 1],
                   [1, 0, 0, 3, 0, 3, 0, 0, 1],
                   [1, 0, 3, 0, 0, 0, 3, 0, 1],
                   [1, 3, 0, 0, 0, 0, 0, 3, 1],
                   [1, 1, 1, 1, 1, 1, 1, 1, 1]],
        'npcs' : [],
        'id' : 11,
        'type' : 'normal',
        }))

SETTINGS.segments_list.append(Segment({
        'array' : [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 1, 1, 1, 1, 0],
                   [0, 1, 1, 1, 0, 0, 0, 0, 1],
                   [1, 0, 0, 1, 0, 8, 0, 0, 1],
                   [0, 0, 0, 1, 0, 0, 0, 0, 1],
                   [1, 0, 0, 1, 1, 1, 10, 1, 0],
                   [1, 0, 0, 9, 0, 0, 0, 0, 1],
                   [1, 7, 0, 1, 0, 8, 0, 0, 1],
                   [0, 1, 1, 1, 0, 1, 1, 1, 0]],
        'npcs' : [((6, 2), 270, 3)],
        'type' : "normal",
        'id' : 12,
        'doors' : [180, 270],
        'items' : [((4, 2), 0), ((2, 7), 4)],
        }))


SETTINGS.segments_list.append(Segment({
        'array' : [[0, 5, 5, 5, 3, 5, 5, 0, 0],
                   [2, 0, 0, 0, 0, 0, 7, 5, 0],
                   [1, 1, 1, 0, 0, 0, 0, 5, 0],
                   [0, 0, 9, 0, 0, 0, 0, 5, 0],
                   [0, 0, 1, 1, 10, 1, 1, 0, 0],
                   [1, 1, 1, 6, 0, 6, 1, 0, 0],
                   [0, 0, 1, 0, 8, 0, 1, 0, 0],
                   [0, 0, 1, 0, 0, 0, 2, 0, 0],
                   [0, 0, 1, 0, 0, 0, 1, 0, 0]],
        'npcs' : [],
        'type' : "normal",
        'id' : 13,
        'doors' : [270, 180],
        'items' : [((1, 1), 2), ((6, 3), 3)],
        }))

SETTINGS.segments_list.append(Segment({
        'array' : [[1, 1, 3, 1, 1, 1, 0, 0, 0],
                   [2, 7, 0, 0, 7, 2, 0, 0, 0],
                   [5, 0, 0, 8, 0, 5, 0, 0, 0],
                   [2, 7, 0, 0, 7, 2, 0, 0, 0],
                   [1, 1, 1, 10, 1, 1, 1, 1, 0],
                   [0, 1, 7, 0, 0, 0, 7, 1, 0],
                   [0, 2, 0, 0, 8, 0, 0, 2, 0],
                   [0, 1, 7, 0, 0, 0, 7, 1, 0],
                   [0, 1, 1, 0, 0, 0, 1, 1, 0]],
        'npcs' : [],
        'type' : "start",
        'id' : 14,
        'doors' : [270],
        'player_pos' : (2, 1),
        'items' : [((1, 2), 0), ((4, 2), 4), ((6, 6), 1)],
        }))

SETTINGS.segments_list.append(Segment({
        'items' : [((5, 5), 2)],
        'npcs' : [((4, 5), 270, 0)],
        'id' : 15,
        'name' : None,
        'type' : 'normal',
        'array' : [[0, 0, 0, 11, 0, 11, 0, 0, 0],
                   [0, 0, 11, 11, 0, 11, 11, 0, 0],
                   [0, 11, 0, 0, 0, 0, 0, 11, 0],
                   [0, 11, 0, 0, 11, 0, 0, 11, 0],
                   [0, 11, 0, 0, 0, 0, 0, 11, 0],
                   [0, 11, 0, 0, 0, 0, 0, 11, 0],
                   [0, 11, 0, 11, 0, 11, 0, 11, 0],
                   [0, 11, 0, 0, 0, 0, 0, 11, 0],
                   [0, 0, 11, 11, 0, 11, 11, 0, 0]],
        'doors' : [270, 90],
        }))

SETTINGS.segments_list.append(Segment({
        'items' : [((5, 4), 2)],
        'npcs' : [],
        'name' : None,
        'array' : [[0, 0, 11, 11, 12, 11, 11, 0, 0],
                   [0, 11, 0, 0, 0, 0, 6, 11, 0],
                   [0, 11, 0, 0, 0, 0, 0, 11, 0],
                   [0, 11, 10, 11, 0, 8, 0, 11, 0],
                   [0, 11, 0, 11, 7, 0, 0, 11, 0],
                   [0, 12, 0, 11, 11, 12, 11, 0, 0],
                   [0, 11, 0, 0, 0, 11, 0, 0, 0],
                   [0, 0, 11, 11, 0, 11, 0, 0, 0],
                   [0, 0, 0, 11, 0, 11, 0, 0, 0]],
        'type' : 'normal',
        'id' : None,
        'doors' : [270],
        }))


#SETTINGS.segments_list.append(Segment({
        #'id' : Unique ID,
        #'npcs' : [([x,y], face, id)],
        #'items' : [([x,y], id)]),
        #'array' : [array],
        #'doors' : [Entrances to the segment in degrees],
        #}))

