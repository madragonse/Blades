from engine_2d.shape2D import Shape2D
from models.player_model import player_model
from engine_2d.line2D import Line2D
import copy


def __load_model(model_raw, origin, xr = 1, yr = 1) -> Shape2D:
    player_model = copy.deepcopy(model_raw)
    player_left_origin = copy.deepcopy(origin)

    player_left_origin[0] *= xr
    player_left_origin[1] *= yr
    player_left = Shape2D([0, 0])

    for line in player_model:
        for i in range(0, len(line)):
            line[i][0] *= xr
            line[i][1] *= yr

        if len(line) == 2:
            for p in range(0, len(line)):
                line[p][0] = line[p][0] - player_left_origin[0]
                line[p][1] = line[p][1] - player_left_origin[1]
            player_left.addLine(Line2D(line))
        else:
            const_line = []
            const_line.append([line[0][0] - player_left_origin[0], line[0][1] - player_left_origin[1]])
            for i in range(1, len(line)):
                const_line.append([const_line[i-1][0] + line[i][0], const_line[i-1][1] + line[i][1]])
            const_line.append(const_line[0])
            player_left.addLine(Line2D(const_line))
        
        
    return player_left


def get_player_l():
    return __load_model(player_model['model'], player_model['origin'], 1, -1) 


def get_player_r():
    return __load_model(player_model['model'], player_model['origin'], -1, -1) 